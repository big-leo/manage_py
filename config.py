import configparser

def add_ftp(host):
    hosts(host, 'ftp')
    print('added ftp', host)

def add_ssh(host):
    hosts(host, 'ssh')
    print('added ssh', host)

def add_smb(host):
    hosts(host, 'smb')
    print('added smb', host)

def del_host(host):
    hosts.del_host(host)
    print('deleted host', host)

def add_user(user):
    hosts.set_user(user)
    print('added user', user)

def add_password(password):
    hosts.set_password(password)
    print('added password')

def add_path(path):
    hosts.set_path(path)
    print('added path', path)

def check_host(host):
    print('check host', host)

def load_cfg():
    config = configparser.ConfigParser()
    config.read('setup/config.ini')
    for section in config.sections():
        if config[section]['type'] == 'ftp':
            add_ftp(section)
        if config[section]['type'] == 'smb':
            add_smb(section)
        if config[section]['type'] == 'ssh':
            add_ssh(section)
        for key in config[section]:
            if key == 'type':
                pass
            if key == 'user':
                add_user(config[section][key])
            if key == 'password':
                add_password(config[section][key])
            if key == 'path':
                add_path(config[section][key])
    print('load from config file')

def save_cfg():
    config = configparser.ConfigParser()
    for host in hosts.get_hosts():
        dic = {}
        if host.type_host != None:
            dic['type'] = str(host.type_host)
        if host.user != None:
            dic['user'] = str(host.user)
        if host.password != None:
            dic['password'] = str(host.password)
        if host.path != None:
            dic['path'] = str(host.path)
        config[host.addr] = dic
    with open('setup/config.ini', 'w') as configfile:
        config.write(configfile)
    print('save to config file')

class hosts(object):
    """
    class for include all hosts with user and password for it
    """

    list_hosts = []

    def __init__(self, addr, type_host):
        self.addr = addr
        self.type_host = type_host
        self.user = None
        self.password = None
        self.path = None
        hosts.list_hosts.append(self)

    def __str__(self):
        result = ''
        result = ('\n%s: %s') % (self.type_host, self.addr)
        if self.user != None:
            result += ('\nuser: %s') % (self.user)
        if self.password != None:
            result += ('\npassword: %s') % (self.password)
        if self.path != None:
            result += ('\npath: %s') % (self.path)
        return result

    @staticmethod
    def get_hosts():
        return hosts.list_hosts

    @staticmethod
    def set_user(user):
        for host in hosts.get_hosts():
            if ((host.user == None) or (host.user == 'None')):
                host.user = user

    @staticmethod
    def set_password(password):
        for host in hosts.get_hosts():
            if ((host.password == None) or (host.password == 'None')):
                host.password = password

    @staticmethod
    def set_path(path):
        for host in hosts.get_hosts():
            if ((host.path == None) or (host.path == 'None')):
                host.path = path

    @staticmethod
    def del_host(host):
        new_hosts = []
        for host in self.get_hosts():
            if host.addr != host:
                new_hosts.append(hosts(host))
        self.list_hosts = new_hosts
