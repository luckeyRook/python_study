#07.メソッドの種類
#メソッド一覧
class Test_Class:

    #インスタントメソッド
    #通常のメソッド
    def sample_instancemethod(self,arg_1):
        pass

    #クラスメソッド
    #クラスをインスタンス化せずとも呼び出せるメソッド
    @classmethod
    def sample_classmethod(self,arg_1):
        pass
    
    #スタティックメソッド
    #クラスをインスタンス化せずとも呼び出せるメソッド
    #加えて、selfのような自身を表す変数が不要
    @staticmethod
    def sample_staticmethod(arg_1,arg_2):
        pass
