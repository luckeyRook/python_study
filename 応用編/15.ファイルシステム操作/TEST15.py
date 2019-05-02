#15.ファイルシステム操作
#ファイル・ディレクトリの存在チェック
import os

filepath ='c:\python'

if os.path.exists(filepath):
    print('指定のファイル、またはディレクトリが存在しています')

    if os.path.isfile(filepath):
        print('指定のパスはファイルです')
    if os.path.isdir:
        print('指定のパスはディレクトリです')
else :
    print('指定のファイル、またはディレクトリは存在しません')

#ディレクトリの作成と削除
import os
import shutil

def show_dir(path):
    print('=========================')
    for dirpath,dirnames,filenames in os.walk(path):
        for dirname in dirnames :
            print(os.path.join(dirpath,dirname))

timdir='c:\python\\tmp'

#ディレクトリの作成
os.mkdir(timdir)
os.makedirs('c:\python\\tmp\makedirs1\makedirs2\makedirs3')
show_dir(timdir)

#ディレクトリの削除
#os.removedirs(timdir)
shutil.rmtree(timdir)

#ファイル、ディレクトリのコピー
import os
import shutil
shutil.copy('c:\python\src.txt','c:\python\dest.txt')
shutil.copytree('c:\python','c:\python_backup')