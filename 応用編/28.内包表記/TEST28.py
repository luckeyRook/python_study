#28.内包表記
#リストの内包表記
comp_list=[i for i in range(10)]
print(comp_list)

#以下のコードと同じ
comp_list=[]

for i in range(10):
    comp_list.append(i)
print(comp_list)

#本来は3行必要な処理を一行にできる
comp_list=[str(i*i) for i in range(10)]
print(comp_list)

print('=================================')
#ディクショナリの内包表記
comp_dict={str(i):i*i for i in range(10)}
print(comp_dict)

#以下のコードと同じ
comp_dict={}

for i in range(10):
    comp_dict[str(i)]=i*i
print(comp_dict)

print('=================================')

#セットの内包表記
comp_set={str(i*i) for i in range(10)}
print(comp_set)

#以下のコードと同じ
comp_set=set()

for i in range(10):
    comp_set.add(str(i*i))
print(comp_set)

print('=================================')

#forのネスト
comp_list_1=[i *ii for i in range(1,10) for ii in range(1,10)]
print(comp_list_1)

#以下のコードと同じ
comp_list_1=[]

for i in range(1,10):
    for ii in range(1,10):
        comp_list_1.append(i*ii)
print(comp_list_1)

print('=================================')

#ifとの併用
comp_list_2=[i for i in range(10) if i % 2 ==1 ]
print(comp_list_2)

#以下のコードと同じ
comp_list_2=[]

for i in range(10):
    if i %2 == 1:
        comp_list_2.append(i)
print(comp_list_2)

#タプルの内包表記
gen=(i for i in range(10))
print(gen)