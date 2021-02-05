# OS Module

import os
dir(os) #show all attribute and methods
#current directory
os.getcwd()
#navigate to new path
os.chdir('new directary/ /') #getcwd 为新的地址

os.listdir() #list files and folders in current directary
#create a new folder on current directary
os.mkdir('new folder') #只能一级
os.makedirs('new folder') # 可以深入几级
os.makedirs('new folder/book')
#delete folders
os.rmdir('new folder')
os.removedirs('new folder/book') #删除folder 及里面的file
# rename a file or folder
os.rename('original name.txt','new name.txt')
# get all the information about a file
os.stat('test.txt')
st_mtime # modification time, not readable
mod_time = os.stat('decorate.py').st_mtime
from datetime import datetime
datetime.fromtimestamp(mod_time)

# show directary tree
os.walk() # a generator that yields three values: directory path, directories within that path, and files within that path
# 显示路径名，所有文件夹，所有文件，结果是有三个值的tuple，故可以用for
for dirpath, dirnames, filenames in os.walk(' ') #显示该路径下所有的文件夹和文件名，然后一级一级显示每个文件夹里面的内容 直到全部文件都被显示为止

# show environment





>>> os.getcwd()
'C:\\Python'
>>> os.chdir('C:\Python\examples')
>>> os.getcwd()
'C:\\Python\\examples'
>>> os.listdir()
['decorate.py', 'dictionaries.py', 'example.py', 'function.py', 'generator.py',
 'integer and float.py', 'iteration.py', 'modules.py', 'name=main.py',
 'nameeqaulsmain.py', 'OS.py', 'string.py', 'try-except.py', '__pycache__']
>>> os.makedirs('new-folder/test')
>>> os.listdir()
['decorate.py', 'dictionaries.py', 'example.py', 'function.py', 'generator.py', 'integer and float.py', 'iteration.py', 'modules.py', 'name=main.py', 'nameeqaulsmain.py', 'new-folder', 'OS.py', 'string.py', 'try-except.py', '__pycache__']
>>> os.removedirs('new-folder/test')
>>> os.listdir()
['decorate.py', 'dictionaries.py', 'example.py', 'function.py', 'generator.py', 'integer and float.py', 'iteration.py', 'modules.py', 'name=main.py', 'nameeqaulsmain.py', 'OS.py', 'string.py', 'try-except.py', '__pycache__']
>>> os.stat('decorate.py')
os.stat_result(st_mode=33206, st_ino=92886742314526967, st_dev=3025129132, st_nlink=1, st_uid=0, st_gid=0, st_size=899, st_atime=1525828771, st_mtime=1525829216, st_ctime=1525828771)
>>> datetime.fromtimestamp(mod_time)
datetime.datetime(2018, 5, 8, 19, 26, 56, 793435)

>>> for dirpath, dirnames, filenames in os.walk('C:\Python\examples'):
	print('current path:', dirpath)
	print('directories:', dirnames)
	print('files:', filenames)
	print()

current path: C:\Python\examples
directories: ['__pycache__']
files: ['decorate.py', 'dictionaries.py', 'example.py', 'function.py', 'generator.py', 'integer and float.py', 'iteration.py', 'modules.py', 'name=main.py', 'nameeqaulsmain.py', 'OS.py', 'string.py', 'try-except.py']

current path: C:\Python\examples\__pycache__
directories: []
files: ['example.cpython-36.pyc']
