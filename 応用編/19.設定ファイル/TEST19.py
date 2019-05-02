#19.設定ファイル
#設定ファイルの読み込み

#python3系
import configparser

inifile=configparser.ConfigParser()
inifile.read('./config.ini','UTF-8')

print(inifile.get('settings','host'))
print(inifile.get('settings','port'))

print(inifile.get('system','os'))
print(inifile.get('system','version'))
print(inifile.get('system','path'))

print(inifile.get('user','name'))
print(inifile.get('user','password'))
print(inifile.get('user','mail'))


#python2系
'''
# _*_ coding: utf-8 _*_
import configparser

inifile=configparser.ConfigParser()
inifile.read('./config.ini')

print inifile.get('settings','host')
print inifile.get('settings','port')

print inifile.get('system','os')
print inifile.get('system','version')
print inifile.get('system','path')

print inifile.get('user','name')
print inifile.get('user','password')
print inifile.get('user','mail')
'''

print('=====================================')

#ファイルに日本語名が含まれる場合
#python3系
import configparser

inifile=configparser.ConfigParser()
inifile.read('./config2.ini','UTF-8')

print(inifile.get('ユーザー','name'))
print(inifile.get('ユーザー','name_kana'))
print(inifile.get('ユーザー','備考'))

#python2系
'''
# _*_ coding: utf-8 _*_
import configparser

inifile=configparser.ConfigParser()
inifile.read('./config.ini')

#出力項目が日本語の時にユニコード変換
print inifile.get('ユーザー','name')
print unicode(inifile.get('ユーザー','name_kana'),'UTF-8')
print unicode(inifile.get('ユーザー','備考'),'UTF-8')
'''

