import os
from my_units.myfile import MyFile

def local_list_files(dir):
    """func for create list files for check"""
    result = []
    files = os.listdir(dir)
    for file in files:
        if (os.path.isfile(dir + "/" + file)):
            result.append(MyFile(dir, dir + "/" + file, 0))
        elif (os.path.isdir(dir + "/" + file)):
            result = result + local_list_files(dir + "/" + file)
    return result

def del_root_path(dir, files):
    result = []
    #if (len(files) > 0):
        #root_dir = files[0].split("/")[0]
        #print("root_dir: " + root_dir)
    for file in files:
        result.append(MyFile(dir, file.name[len(dir)+1:], 0))
    return result

def remote_list_files(dir):
    """func for create list files on remote server for check"""
    result_list = []
    result_list.append("file1")
    result_list.append("file2")
    return result_list
