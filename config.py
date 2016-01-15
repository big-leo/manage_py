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
    for host in hosts.get_hosts():
        host.set_user(user)
    print('added user', user)

def add_password(password):
    hosts.set_password(password)
    print('added password')

def check_host(host):
    print('check host', host)

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
        hosts.list_hosts.append(self)

    def __str__(self):
        result = ''
        result = ('\n%s: %s') % (self.type_host, self.addr)
        try:
            result += ('\nuser: %s') % (self.user)
        except AttributeError:
            pass
        try:
            result += ('\npassword: %s') % (self.password)
        except AttributeError:
            pass
        return result

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @staticmethod
    def get_hosts():
        return hosts.list_hosts

    @staticmethod
    def set_user(user):
        for host in hosts.get_hosts():
            if host.user == None:
                host.user = user

    @staticmethod
    def set_password(password):
        for host in self.get_hosts():
            if host.password == None:
                host.password = password

    @staticmethod
    def del_host(host):
        new_hosts = []
        for host in self.get_hosts():
            if host.addr != host:
                new_hosts.append(hosts(host))
        self.list_hosts = new_hosts
