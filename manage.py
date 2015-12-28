#!/usr/bin/env python3
import sys
import os
from lists import *

if __name__ == "__main__":
#    os.system("ls")
    print("main")
    path = "dir"
    files = local_list_files(path)
    for file in files:
        print(file)
        os.system("cp " + file + " dir2/")
