#05.新旧クラススタイル
#クラススタイルの選択
#環境がPython3のため、Python2verは全てコメント化

## -*- config: utf-8 -*-
##旧スタイルクラス
#class OldStyleClass:
#    pass
##新スタイルクラス
#class NewStyleClass(object):
#    pass
#
#print(OldStyleClass)
#print(NewStyleClass)

#Python3は新クラスしかない
#新スタイルクラス
class NewStyleClass:
    pass
print(type(NewStyleClass))

