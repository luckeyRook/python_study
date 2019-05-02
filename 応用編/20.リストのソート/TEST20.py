#20.リストのソート
#リスト自体をソートする
python_list=[]
python_list.append(100)
python_list.append(200)
python_list.append(10)
python_list.append(800)
python_list.append(60)

print('-------------------------')
print('【そのまま表示】')
for value in python_list:
    print(value)

python_list.sort()

print('-------------------------')
print('【ソート表示】')
for value in python_list:
    print(value)

#リストのソート結果を表示する
python_list2=[]
python_list2.append(100)
python_list2.append(200)
python_list2.append(10)
python_list2.append(800)
python_list2.append(60)

print('-------------------------')
print('【そのまま表示】')
for value in python_list2:
    print(value)


print('-------------------------')
print('【ソート表示】')
for value in sorted(python_list2):
    print(value)

print('-------------------------')
print('【リストの再表示】')
for value in python_list2:
    print(value)


