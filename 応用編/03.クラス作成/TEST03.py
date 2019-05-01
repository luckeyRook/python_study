#03.クラス作成
#クラスの基礎
class TestClass:
    #クラスの初期化
    #initは必ず書くこと
    def __init__(self,code,name):
        #引数を自身のインスタンス属性へ引き渡す
        self.code=code
        self.name=name

classes=[]
#クラスの利用
classes.append(TestClass(1,'テスト１'))
classes.append(TestClass(2,'テスト２'))

for test_cls in classes:
    print("======Class=======")
    print("code ---> " + str(test_cls.code))
    print("name ---> " + test_cls.name)
