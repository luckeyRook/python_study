#34.モジュールの属性取得
#dir
print('--------------------------------')
print(dir())

python_dir='python-izm'

print('--------------------------------')
print(dir())

print('--------------------------------')
import sys
for one in dir(sys):
    print(one)
