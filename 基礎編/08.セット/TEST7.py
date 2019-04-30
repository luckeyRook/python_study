#セット キーのないディクショナリ
#セットの基本
test_set_1 = {'python','-','izm','.','com'}
print(test_set_1)

print('-----------------------')
for i in test_set_1 :
    print(i)

#空のセットを作る場合は、｛｝ではできない
#こっちはディクショナリ
test_dict={}
print(test_dict)
#こっちはセット
test_set_2={'python'}
print(test_set_2)
#空のセットは「set」を使用
empty_set=set()
print(empty_set)

#セットは重複した値を出さない
test_set_3 = {'python','-','izm','.','com','python','izm'}
print(test_set_3)
print('-----------------------')
for i in test_set_3 :
    print(i)

#要素の追加
test_set_4 = set()

test_set_4.add('python')
#他の配列を追加する場合はupdate()
test_set_4.update({'-','izm','.','com','python','izm'})
print(test_set_4)


#要素の削除
test_set_5 = {'python','-','izm','.','com'}
test_set_5.remove('-')
#test_set_5.remove('V')

test_set_5.discard('.')

print(test_set_5)

#特殊なセットfrozenset

test_set_6=frozenset({'python','-','izm','.','com'})

#errorになるケース
#test_set_6.remove('-')
#test_set_6.discard('.')
print(test_set_6)