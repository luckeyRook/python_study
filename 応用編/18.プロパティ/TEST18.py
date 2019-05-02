#18.プロパティ
#プロパティ関数

class PropertyTest(object):

    def __init__(self,url):
        self._url=url

    def get_url(self):
        print('---get url---')
        return self._url
    
    url=property(get_url)

prop=PropertyTest('https://www.python-izm.com/')

#プロパティ「url」を取得
print(prop.url)

print('==========================================-')

class PropertyTest2(object):

    def __init__(self,url):
        self._url=url

    def get_url(self):
        print('---get url---')
        return self._url

    def set_url(self,url):
        print('---set url---')
        self._url = url
    
    def del_url(self):
        print('---del url---')
        del self._url
    
    url=property(get_url,set_url,del_url,'url Property')

prop2 = PropertyTest2('https://www.python-izm.com/')

#setter(set_url)にアクセス
prop2.url = 'python-izm'

#getter(get_url)にアクセス
print(prop2.url)

print('==========================================-')

class PropertyTest3(object):

    def __init__(self,schema,host):
        self.schema=schema
        self.host=host
    def get_url(self):
        print('---get url---')
        return ('{}://{}/'.format(self.schema,self.host))

    url=property(get_url)

prop3 = PropertyTest3('https','www.python-izm.com')

print(prop3.url)

#プロパティデコレーター
print('==========================================-')

class PropertyTest4(object):

    def __init__(self,url):
        self._url=url

    @property
    def url(self):
        print('---get url---')
        return self._url

    
prop4 = PropertyTest4('https://www.python-izm.com/')

#setter(set_url)にアクセス
print(prop4.url)

print('==========================================-')

class PropertyTest5(object):

    def __init__(self,url):
        self._url=url

    @property
    def url(self):
        print('---get url---')
        return self._url

    @url.setter
    def url(self,url):
        print('---set url---')
        self._url = url

    @url.deleter
    def url(self):
        print('---del url---')
        del self._url
    

prop5 = PropertyTest5('https://www.python-izm.com/')

#setter(set_url)にアクセス
prop5.url = 'python-izm'

#getter(get_url)にアクセス
print(prop5.url)

print('==========================================-')

class PropertyTest6(object):

    def __init__(self,schema,host):
        self.schema=schema
        self.host=host

    @property
    def url(self):
        print('---get url---')
        return ('{}://{}/'.format(self.schema,self.host))


prop6 = PropertyTest6('https','www.python-izm.com')

print(prop6.url)

#旧スタイルは無視
'''
class PropertyTest:
    def __init__(self,url):
        self._url=url

    @property
    def url(self):
        print('---get_url---')
        return self.url

prop=PropertyTest('https','www.python-izm.com')
print(prop.url)

prop.url='python-izm'
print(prop.url)
'''