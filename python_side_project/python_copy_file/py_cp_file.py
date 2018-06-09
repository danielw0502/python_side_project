import os
import re
import shutil

status = 'pass'
dist = '/Users/wxd/Desktop/record/py_copy_file/dist'
#display the current path
current_path = '/Users/wxd/Desktop/record/py_copy_file/python_copy_file'

#check the status of file if pass
def check_file_status(file_name,status):
    f = open(file_name)
    for lines in f:
        line = lines.strip()
        if(re.search('pass',line) != None):
            f.close()
            return True
    f.close()
    return False

#check the file in the path, if status is pass, then copy it
def check_dir_file(path,status,dist):
    for root, dirs, files in os.walk(path,topdown=True):
        for name in files:
            file_name = os.path.join(root,name)
            if(check_file_status(file_name,status) == True):
                file_isf = [x for x in files if x[-4:] == '.isf']
                for isf_f in file_isf:
                    isf_f_name = os.path.join(root,isf_f)
                    shutil.copy2(isf_f_name,dist) 

if __name__ == '__main__':
    check_dir_file(current_path,status,dist)
