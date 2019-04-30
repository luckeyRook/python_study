#if文
#if文の基礎

value = 2

if value == 1 :
    print("valueの値は1です")
elif value == 2 :
    print("valueの値は2です")
elif value == 3 :
    print("valueの値は3です")
else:
    print("該当する値はありません")

#条件の組み合わせ
value_1 = 'python'
value_2 = 'izm'

if value_1 == 'Python' :
    #passは何もしないという命令
    #条件を設定し何も記述しないとerrorが発生する。
    pass
elif value_1 == 'python' and value_2=='izm':
    print("条件2がTure")
elif value_1 == 'python' and value_2=='PYTHON':
    print("条件3がTure")
