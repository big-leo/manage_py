#!/usr/bin/env python3
import sys
import os
from lists import *

if __name__ == "__main__":
    print("main")
    path = "dir"
    files = local_list_files(path)
    #files = os.listdir(path)
    for file in files:
        print(file)
