import pika, logging, time, threading, json # urllib2
import urllib.request as urllib

# from warnings import simplefilter
# simplefilter("ignore", "user")


## Configurable parameters

_loglevel = logging.DEBUG
_publish_sleeptime = 60
_default_helper_conf = "local"
_default_amqp_conf = "db"

# onde: ec2-54-208-87-165.compute-1.amazonaws.com:15672
_helper_conf = { 
    "big": {
        'helper_sleeptime' : 300, # in seconds
        'ram_limit' : 25, # value in GB
        'host' : 'localhost',
        'user' : 'trb',
        'pass' : "clm28'Anglos",
        'virtual_host' :'twttr'        
    },
    "small": {
        'helper_sleeptime' : 300, # in seconds
        'ram_limit' : 3,# value in GB
        'host' : 'localhost',
        'user' : 'trb',
        'pass' : "clm28'Anglos",
        'virtual_host' :'twttr'        
    },
    "local": {
        'helper_sleeptime' : 300, # in seconds
        'ram_limit' : 1, # value in GB
        'host' : 'localhost',
        'user' : 'trb',
        'pass' : "clm28'Anglos",
        'virtual_host' :'twttr'
    }
}

_amqp_conf = {
    "db": {
        'host' : 'localhost',
        #'host' : 'stream-rabbit-2-0.sinniaws.com', # rabbit-2-0
        #'host' : '107.21.235.136', # capture
        'user' : 'trb',
        'pass' : "clm28'Anglos",
        'virtual_host' :'twttr',
        'exchange' : 'capture',
        'routing_key' :'rest.%s.no-log'
    },
    "file": {
        'host' : 'localhost',
        'user' : 'trb',
        'pass' : "clm28'Anglos",
        'virtual_host' :'twttr',
        'exchange' : 'capture_to_file',
        'routing_key' :'rest.%s.no-log'
    }
}

## Logger init
    
_instances = {}

## Class definition
class AMQPUtil():
    logging.basicConfig(level=logging.DEBUG)

    def __init__(self, with_helper=False):
        self.do_slow_down = False
        self.ram_current = None

        print('AMQPUtil.init')
        hconf = _helper_conf.get(_default_helper_conf, _helper_conf['local'])
        print('AMQPUtil.init hconf %s'%str(hconf))
        self.helper = AMQPHelper(hconf['host'],hconf['user'],hconf['pass'],
                                 hconf['helper_sleeptime'],hconf['ram_limit'])
        print('AMQPUtil.init helper %s'%str(self.helper))
        if with_helper:
            self.helper.start()
        conf = _amqp_conf.get(_default_amqp_conf, _amqp_conf['db'])
        print('AMQPUtil.init conf %s'%str(conf))
        self._parameters = pika.ConnectionParameters(
            credentials=pika.PlainCredentials(conf['user'], conf['pass']),
            host=conf['host'], virtual_host=conf['virtual_host'])
        print('AMQPUtil.init params %s'%str(self._parameters))
        self._connection = None
        self._channel = None
        logging.info("Instance of AMQPUtil initialized")
        logging.info("Credentials: %s, %s, %s" % (conf['host'], conf['user'], 
                                                  conf['pass']))
        print("AMQPUtil.init initialized")


    def _getChannel(self):
        global _publish_sleeptime
        if self._connection is None or self._channel is None \
                or self._connection.is_closed or self._channel.is_closed \
                or not self._connection.is_open:
            logging.info('Reconnecting ...')
            print('_getchannel starting connection')
            self._connection = pika.BlockingConnection(self._parameters)
            def _handleBackpressure():
                self.helper.tcp_handler()
            self._channel = self._connection.channel()
        if self.helper.do_slow_down():
            logging.warn('Sleeping ...')
            time.sleep(_publish_sleeptime)
            logging.warn('Awake ...')
        print('_getchannel getting channel %s'%str(self._channel))
        return self._channel

    @staticmethod
    def _getInstance(config_name = None):
        #global _instances
        print('getInstance from available: %s'%str(_instances))
        if not config_name: config_name = _default_amqp_conf
        print('getInstance config: %s'%config_name)
        instance = _instances.get(config_name)
        print('getInstance instance: %s'%str(instance))
        if instance is None:
            print('getInstance starting instance')
            instance = AMQPUtil()
            print('getInstance started instance: %s'%str(instance))
            _instances[config_name] = instance
        print('getInstance added instance: %s'%str(_instances[config_name]))
        return instance
        
    @staticmethod
    def publish(client, message, config = None, retry=0):
        try:
            if not client : client = "sinnia"
            print('publish client: %s'%client)
            client_key = (lambda c, m: m.get(c) if m.get(c) else c)\
                         (client, { "all": "all", 
                                    "sinnia": "sinnia"})
            print('publish client_key: %s'%client_key)
            conf = _amqp_conf.get(config, _amqp_conf[_default_amqp_conf])
            print('publish conf: %s'%conf)
            vhost = conf['virtual_host']
            print('publish vhost: %s'%vhost)
            routing_key = conf['routing_key']
            print('publish rk: %s'%routing_key)
            exchange=conf['exchange']
            print('publish exchange: %s'%exchange)
            inst = AMQPUtil._getInstance(config)
            print('publish instance: %s'%str(inst))
            chann = inst._getChannel()
            print('publish channel: %s'%str(chann))
            logging.debug("Publish to vhost: %s exchange: %s rkey: %s body: %s"
                          % (vhost, exchange, routing_key, message))
            chann.basic_publish(exchange=exchange,
                                routing_key=routing_key,
                                body=message)
            print('published')
        except:
            if retry <= 10:
                retry += 1
                logging.info("Retry .... %s" % retry)
                AMQPUtil.publish(client, message, config, retry)
            else:
                logging.error("Retries exhausted: could not connect to host")


class AMQPHelper(threading.Thread):

    def __init__(self, host, user, passwd, sleeptime, ram_limit):
        self.api_url = 'http://%s:15672/api/nodes' % host 
        self.sleeptime = sleeptime
        self.ram_limit = ram_limit * 1000000000
        self.current_ram = 0
        self.tcp_trigered = False
        print('AMQPHelper.init: url=%s usr=%s pass=%s'%(self.api_url,user,passwd))
        print('AMQPHelper.init setting auth')

        # create a password manager
        # add the username and password
        print('AMQPHelper.init starting pwdmgr')
        password_mgr = urllib.HTTPPasswordMgrWithDefaultRealm()
        print('AMQPHelper.init started pwdmgr')
        print('AMQPHelper.init adding data to pwdmgr')
        password_mgr.add_password(None, self.api_url, user, passwd)
        print('AMQPHelper.init added data to pwdmgr')
        
        print('AMQPHelper.init starting handler')
        handler = urllib.HTTPBasicAuthHandler(password_mgr)        
        print('AMQPHelper.init started handler')
        # create "opener" (OpenerDirector instance)
        # install the opener. All calls to urllib.urlopen will use it.
        print('AMQPHelper.init starting opener')
        opener = urllib.build_opener(handler)
        print('AMQPHelper.init started opener')
        print('AMQPHelper.init installing opener')
        urllib.install_opener(opener)
        print('AMQPHelper.init installed opener')
        # use the opener to fetch a URL
        # opener.open(a_url)
        
        # password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        # password_mgr.add_password(None, self.api_url, user, passwd)
        # handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        # opener = urllib2.build_opener(handler)
        # urllib2.install_opener(opener)
        print('AMQPHelper.init starting thread')
        threading.Thread.__init__(self)
        print('AMQPHelper.init started thread')

        
    def get_ram(self):
        return self.current_ram

    def is_ram_exceded(self):
        return self.ram_limit < self.get_ram()

    def is_tcp_trigered(self):
        if self.tcp_trigered:
            self.tcp_trigered = False
            return True
        return False

    def tcp_handler(self):
        self.tcp_trigered = True

    def do_slow_down(self):
        return self.is_ram_exceded() or self.is_tcp_trigered()
        
    def run(self):
        print('AMQPHelper.run starting')
        while 1:
            try:
                response = urllib.urlopen(self.api_url)
                #response = urllib2.urlopen(self.api_url)
                data = json.loads(response.read())
                max_ram = 0
                for node in data:
                    ram = node.get('mem_used', 0)
                    if max_ram < ram: max_ram = ram
                self.current_ram = int(max_ram)
                logging.info("RAM: %sG" % (self.current_ram / 1000000000.0))
            except Exception as exc:
                logging.info("Could not obtain ram: %s" % self.api_url)
                logging.exception(exc)
            time.sleep(self.sleeptime)

