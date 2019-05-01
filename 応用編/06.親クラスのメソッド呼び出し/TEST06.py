#06.親クラスのメソッド呼び出し

#新スタイルの継承
#Python2の場合
## -*- config: utf-8 -*-
#新クラスのスタイル
#class NewStlyeClassBase(object):
#    def test_method(self,msg):
#        print 'NewStlyeClassBase: {}'.format(msg)
#
##新スタイルのクラス継承
#class NewStlyeClass(NewStlyeClassBase):
#    def test_method(self,msg):
#        print 'NewStlyeClass: {}'.format(msg)
#        super(NewStlyeClassBase,self).test_method(msg)
#        #NewStlyeClassBase.test_method(self,msg)
#
#new = NewStlyeClass()
#new.test_method('method call')

#Python3の場合
class NewStlyeClassBase(object):
    def test_method(self,msg):
        print('NewStlyeClassBase: {}'.format(msg))

class NewStlyeClass(NewStlyeClassBase):
    def test_method(self,msg):
        print('NewStlyeClass: {}'.format(msg))
        super().test_method(msg)
        #super(NewStlyeClassBase,self).test_method(msg)
        #NewStlyeClassBase.test_method(self,msg)

new= NewStlyeClass()
new.test_method('method call')

#旧スタイルの継承
##Python2の場合
## -*- config: utf-8 -*-
##旧スタイルクラス
#class OldStyleClassBase:
#    def test_method(self, msg):
#        print 'OldStlyeClassBase: {}'.format(msg)
#
##旧スタイルのクラス継承
#class OldStlyeClass(OldStyleClassBase):
#    def test_method(self,msg):
#        print 'OldStlyeClassBase: {}'.format(msg)
#        OldStlyeClassBase.test_method(msg)
#old=OldStlyeClass()
#old.test_method("method call")
