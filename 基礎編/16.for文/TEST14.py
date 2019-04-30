#for文

#for文の基礎
for_sample = []

for_sample.append("python")
for_sample.append("-")
for_sample.append("izm")
for_sample.append("for")
for_sample.append("statement")
for_sample.append("sample")

for value in for_sample:
    print(value)

#配列を利用せずとも使える
for value in 'ABCDEF':
    print(value)

#分割して取得することも可能
test_list_1=[['https','www'],['python-izm','com']]

for value in test_list_1:
    print(value)

for value_1,value_2 in test_list_1:
    print(value_1,value_2)
