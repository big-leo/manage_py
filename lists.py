import os

def local_list_files(dir):
    """func for create list files for check"""
    result = []
    files = os.listdir(dir)
    for file in files:
        if os.path.isfile(dir + "/" + file):
            result.append(dir + "/" + file)
        elif os.path.isdir(dir + "/" + file):
            result = result + local_list_files(dir + "/" + file)
    return result

def remote_list_files(dir):
    """func for create list files on remote server for check"""
    result_list = []
    result_list.append("file1")
    result_list.append("file2")
    return result_list
