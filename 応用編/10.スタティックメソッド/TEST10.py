#10.スタティックメソッド
#@staticmethod

class TestClass:

    #スタティックメソッド
    @staticmethod
    def sample_staticmethod(x,y):
        return(x + y)

#インスタンス化せずに呼び出し
print(TestClass.sample_staticmethod(10,100))

#インスタンス化しても呼び出せる
test_class=TestClass()
print(test_class.sample_staticmethod(100,1000))