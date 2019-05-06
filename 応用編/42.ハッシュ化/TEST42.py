#42.ハッシュ化
#md5 / sha
#python3系
import hashlib

print(hashlib.md5(b'python-izm').hexdigest())
print(hashlib.sha1(b'python-izm').hexdigest())

#python2系
'''
# _*_ coding: utf-8 _*_
import hashlib

print(hashlib.md5(b'python-izm').hexdigest())
print(hashlib.sha1(b'python-izm').hexdigest())
'''