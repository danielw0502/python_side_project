import os
from distutils.dir_util import copy_tree

path = os.getcwd()

index = 1

dest = '/Users/wxd/Documents/all/record/python_side_project/dist'

for dirName, subdirList, fileList in os.walk(path):
    #print dirName
    if '8kdump' in dirName:
        os.mkdir('8kdump'+str(index))
        dest_final = dest + '/'+'8kdump'+str(index)
        copy_tree(dirName,dest_final)
        index += 1
        #print dirName
        #shutil.copytree(dirName,dest)
        #os.rename(dirName,dirName+str(index))
        #index += 1
        #break
