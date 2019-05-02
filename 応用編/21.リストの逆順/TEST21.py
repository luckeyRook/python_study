#21.リストの逆順
#リスト自体を逆順にする
python_list=[]
python_list.append('python')
python_list.append('izm')
python_list.append('sample')
python_list.append('list')
python_list.append('reversed')

print('-------------------------')
print('【そのまま表示】')
for value in python_list:
    print(value)

python_list.reverse()

print('-------------------------')
print('【逆順表示】')
for value in python_list:
    print(value)


#リストの逆順結果を取得する
python_list2=[]
python_list2.append('python')
python_list2.append('izm')
python_list2.append('sample')
python_list2.append('list')
python_list2.append('reversed')

print('-------------------------')
print('【そのまま表示】')
for value in python_list2:
    print(value)


print('-------------------------')
print('【逆順表示】')
for value in reversed(python_list2):
    print(value)

print('-------------------------')
print('【リストの再表示】')
for value in python_list2:
    print(value)

#スライスで逆順結果に取得する
python_list3=[]
python_list3.append('python')
python_list3.append('izm')
python_list3.append('sample')
python_list3.append('list')
python_list3.append('reversed')

print('-------------------------')
print('【そのまま表示】')
for value in python_list3:
    print(value)


print('-------------------------')
print('【逆順表示】')
for value in python_list3[::-1]:
    print(value)

print('-------------------------')
print('【リストの再表示】')
for value in python_list3:
    print(value)

