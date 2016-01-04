#!/usr/bin/env python3
import sys
import os
from lists import *

#sys.path.append('./my_units')
from my_units.myfile import MyFile


if __name__ == "__main__":
    if (len(sys.argv) > 2):
        if (os.path.isdir(sys.argv[1]) and os.path.isdir(sys.argv[2])):
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
