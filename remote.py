class remote(object):
    """
    interface for ssh, smb, ftp remote connect
    """
    def __init__(self, host, user, password, path):
        self.host = host
        self.user_host = user_host
        self.password = password
        self.path = path

    def connect(self):
        print('you must define this method in child class')
