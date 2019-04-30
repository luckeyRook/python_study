#ディクショナリの基本
#ディクショナリは｛key:value｝で囲む
test_dict_1 ={'YEAR':'2019','month':'04','day':'29'}
print(test_dict_1)

print('--------------------------------')

for i in test_dict_1:
    print(i)
    print(test_dict_1[i])
    print('==================================')


#valueの取得
test_dict_2 ={'year':'2019','month':'04','day':'29'}
print(test_dict_2)

print('--------------------------------')
print(test_dict_2['year'])
#print(test_dict_2['years'])

print('--------------------------------')
print(test_dict_2.get('year'))
print(test_dict_2.get('years'))

print('--------------------------------')
print(test_dict_2.get('year','Not Found'))
print(test_dict_2.get('years','Not Found'))

#要素の追加
test_dict_3={}
print(test_dict_3)

print('==================================')
test_dict_3['year']='2019'
test_dict_3['month']='04'
test_dict_3['day']='29'

print(test_dict_3)

#要素の削除
test_dict_4 ={'year':'2019','month':'04','day':'29'}
print(test_dict_4)

print('--------------------------------')
del test_dict_4['day']
print(test_dict_4)

#keyやvalueのみ取得する
test_dict_5 ={'year':'2019','month':'04','day':'29'}
print('--------------------------------')
print(test_dict_5.keys())
print(test_dict_5.values())

#keyやvalueを同時に取得する
test_dict_6 ={'year':'2019','month':'04','day':'29'}
print(test_dict_6)

print('--------------------------------')
for key ,value in test_dict_6.items() :
    print(key,value)

#指定したkeyを持っているか確認
test_dict_7 ={'year':'2019','month':'04','day':'29'}
print(test_dict_7)
print('--------------------------------')
print('year' in test_dict_7)
print('years' in test_dict_7)

