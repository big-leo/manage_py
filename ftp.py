from ftplib import FTP
from remote import *

class ftp(remote):
    """
    class for read data from ftp server
    """
    def connect(self):
        ftp = FTP(remote.host)
        print(ftp.login())
