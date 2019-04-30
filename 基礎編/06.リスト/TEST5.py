#リストの作成
#リストの基本
#リストの場合は[]でくくる
test_list_1 = ['python','-','izm','.','com']
print(test_list_1)

print('-----------------')
for i in test_list_1:
    print(i)

#要素の追加
test_list_2=[]
print(test_list_2)
print('-----------------')
test_list_2.append('python')
test_list_2.append('-')
test_list_2.append('izm')
test_list_2.append('.')
test_list_2.append('com')

print(test_list_2)

#インデックスを利用して追加
test_list_3 = ['python','izm','com']
print(test_list_3)
print('-----------------')
test_list_3.insert(1,'-')
test_list_3.insert(3,'.')
print(test_list_3)
print('-----------------')
test_list_3.insert(0,'https://www.')
print(test_list_3)

#要素の削除
test_list_4 = ['1','2','3','2','1']
print(test_list_4)
print('-----------------')
test_list_4.remove('2')
print(test_list_4)

#要素の削除2
test_list_5 = ['1','2','3','2','1']
print(test_list_5)
print('-----------------')
print(test_list_5.pop(1))
print(test_list_5)

print(test_list_5.pop())
print(test_list_5)


#要素のインデックスを取得
test_list_6 = ['100','200','300','200','100']

print(test_list_6.index('200'))

#要素の数を取得
test_list_7 = ['100','200','300','200','100']

print(test_list_7.count('200'))

