#02.可変長引数
#*arg
def test_func(*arg):
    print(arg)

test_func(1,2,3,4)

def test_func2(code,name,*arg):
    print(code,name)
    print(arg)

test_func2(100,'python-izm','us','JP')

def test_func3(code,name,*countries):
    print(code,name)
    print(countries)

test_func3(100,'python-izm','us','JP')

#**kwargs
#ディクショナリとして引数を引き渡すやり方
def test_func4(**kwargs):
    print(kwargs)

test_func4(Code=100,name='python-izm')

def test_func5(code,name,kana,*args,**kwargs):
    print(code,name,kana)
    print(args)
    print(kwargs)

test_func5(100,'python-izm',u'パイソンイズム','us','JP',email='XXX',city='Tokyo')

