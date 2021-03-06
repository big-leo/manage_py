#!/usr/bin/env python3
import sys
import os
from utils import *
from lists import *
from remote import *
from ftp import *
from ssh import *
from smb import *
from config import *
#from my_units.myfile import MyFile

def get_status():
    print('local path:', hosts.local_path)
    for host in hosts.get_hosts():
        print(host)

def print_help():
    print('full input parameter')
    print("""
    ./manage.py init
    ./manage.py add ftp 192.168.1.1
    ./manage.py add smb 192.168.1.2
    ./manage.py add ssh 192.168.1.3
    ./manage.py add user user1
    ./manage.py add password password1
    ./manage.py add path /prog/code1
    ./manage.py status
    ./manage.py del host 192.168.1.2""")

def read_argv(argv):
    """
    function for read input parameter
    """
    try:
        if (argv[1] == 'init'):
            init_setup()
        elif (argv[1] == 'status'):
            get_status()
        elif (argv[1] == 'check'):
            if (argv[2] == 'host'):
                if (is_ip_addr(argv[3])):
                    check_host(argv[3])
        elif (argv[1] == 'del'):
            if (argv[2] == 'host'):
                if (is_ip_addr(argv[3])):
                    del_host(argv[3])
        elif (argv[1] == 'add'):
            if (argv[2] == 'local'):
                if (os.path.isdir(argv[3])):
                    print(argv[3])
                    add_local_path(argv[3])
            elif (argv[2] == 'ftp'):
                if (is_ip_addr(argv[3])):
                    add_ftp(argv[3])
            elif (argv[2] == 'ssh'):
                if (is_ip_addr(argv[3])):
                    add_ssh(argv[3])
            elif (argv[2] == 'smb'):
                if (is_ip_addr(argv[3])):
                    add_smb(argv[3])
            elif (argv[2] == 'user'):
                add_user(argv[3])
            elif (argv[2] == 'password'):
                add_password(argv[3])
            elif (argv[2] == 'path'):
                add_path(argv[3])
        else:
            print_help()
    except IndexError:
        print_help()

if __name__ == "__main__":
    load_cfg()
    read_argv(sys.argv)
    save_cfg()
    """
    if (len(sys.argv) > 2 and os.path.isdir(sys.argv[1]) and os.path.isdir(sys.argv[2])):
        path1 = sys.argv[1]
        path2 = sys.argv[2]
        print(path1)
        print(path2)
        files1 = del_root_path(path1, local_list_files(path1))
        files2 = del_root_path(path2, local_list_files(path2))
        for file in files1:
            finded = False
            for f in files2:
                if (file.name == f.name):
                    finded = True
            if (finded == False):
                print("without in " + path2 + ": " + file.name)
        for file in files2:
            finded = False
            for f in files1:
                if (file.name == f.name):
                    finded = True
            if (finded == False):
                print("without in " + path1 + ": " + file.name)
    else:
        print("please enter two directories")
    """
