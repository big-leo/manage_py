#!/usr/bin/env python3
import sys
import os
from lists import *

if __name__ == "__main__":
    if (len(sys.argv) > 2):
        if (os.path.isdir(sys.argv[1]) and os.path.isdir(sys.argv[2])):
            path1 = sys.argv[1]
            path2 = sys.argv[2]
            print(path1)
            print(path2)
            files1 = local_list_files(path1)
            files1 = del_root_path(files1)
            files2 = local_list_files(path2)
            files2 = del_root_path(files2)
            for file in files1:
                if not file in files2:
                    print("without in " + path2 + ": " + file)
            for file in files2:
                if not file in files1:
                    print("without in " + path1 + ": " + file)
                #os.system("cp " + file + " " + path2 + "/" )
        else:
            print("please enter two directories")
