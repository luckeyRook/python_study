#30.属性の有無チェック
#hasattr

class AttrTest():
    def __init__(self):
        self.code = -1

attr_test=AttrTest()
attr_test.name='python-izm'

print(hasattr(attr_test,'code'))
print(hasattr(attr_test,'name'))
print(hasattr(attr_test,'kana'))

print('=============================')
#gatattr
class AttrTest2():
    def __init__(self):
        self.code = -1

attr_test=AttrTest2()
attr_test.name='python-izm'

print(getattr(attr_test,'code'))
print(getattr(attr_test,'name'))
#print(getattr(attr_test,'kana'))
print(getattr(attr_test,'kana','No Attr'))
