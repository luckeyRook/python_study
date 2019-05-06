#36.ファイル拡張子の取得
#os.path.splitext
import os.path

print(os.path.splitext('splitext.py'))
print(os.path.splitext('c:/python/splitext.py'))
print(os.path.splitext('splitext'))