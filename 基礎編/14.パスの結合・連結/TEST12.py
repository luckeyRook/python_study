#パスの結合・連結
#pythonではパスを連結するための関数が用意されている
import os

PROJECT_DIR = 'C:\python-izm'
SETTING_FILE = 'setting.ini'

print(os.path.join(PROJECT_DIR,SETTING_FILE))
print(os.path.join(PROJECT_DIR,'Setting_dir',SETTING_FILE))
