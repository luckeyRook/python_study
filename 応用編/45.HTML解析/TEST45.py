#45.HTML解析
#HTML文字列の取得
#python3系
import urllib.request

url='http://www.python-izm.com/'

htmldate=urllib.request.urlopen(url)
print(htmldate.read().decode('UTF-8'))

htmldate.close()

#python2系
'''
# _*_ coding: utf-8_*_
import urllib2

url='http://www.python-izm.com/'

htmldate=urllib2.urlopen(url)
print(htmldate.read().decode('UTF-8'))

htmldate.close()
'''

#ヘッダ情報の設定
#python3系
import urllib.request

url2='http://www.python-izm.com/'

opener=urllib.request.build_opener()

opener.add_handlers={
    (
        'User-agent',
        'Mozilla/5.0 (Windows;U;Winddows NT 5.1; ja;rv;1.9.2.3) Gecko/20100401 Fire Fox3.6.3 ( .NET CLR 3.5.30729)'
    )
}

htmldate2=opener.open(url2)
print(htmldate2.read().decode('UTF-8'))
htmldate2.close()
opener.close()

#python2系
'''
# _*_ coding: utf-8_*_
import urllib2

url2='http://www.python-izm.com/'

opener=urllib2.build_opener(url2)

opener.add_handler={
    (
        'User-agent',
        'Mozilla/5.0 (Windows;U;Winddows NT 5.1; ja;rv;1.9.2.3) Gecko/20100401 Fire Fox3.6.3 ( .NET CLR 3.5.30729)'
    )
}

htmldate2=opener.open(url2)
print(htmldate2.read().decode('UTF-8'))
htmldate2.close()
opener.close()

'''

print('=======================================-')

#タグの解析
#python3系

import urllib
from html.parser import HTMLParser

class TestParser(HTMLParser):
    def handle_starttag(self,tagname,attribute):
        if tagname.lower()=='a':
            for i in attribute:
                if i[0].lower() =='href':
                    print(i[1])

url3='http://www.python-izm.com/'
htmldate3=urllib.request.urlopen(url3)

parser=TestParser()
parser.feed(htmldate3.read().decode('UTF-8'))

parser.close()
htmldate3.close()

#python2系
'''
import urllib2
from HTMLParser import HTMLParser

class TestParser(HTMLParser):
    def handle_starttag(self,tagname,attribute):
        if tagname.lower()=='a':
            for i in attribute:
                if i[0].lower() =='href':
                    print(i[1])

url3='http://www.python-izm.com/'
htmldate3=urllib2.urlopen(url3)

parser=TestParser()
parser.feed(htmldate3.read().decode('UTF-8'))

parser.close()
htmldate3.close()
'''