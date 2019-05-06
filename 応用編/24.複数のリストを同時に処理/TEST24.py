#24.複数のリストを同時に処理
#zip(圧縮のことではない)
item_list=['desktop','laptop','tablet','smartphone']
stok_list=[12,83,55,0]
for item_name,stok_count in zip(item_list,stok_list):
    print('{}/{}'.format(item_name,stok_count))


print('=====================================')
#zip_logest
#要素数が異なる場合
#例)zipで行った場合
item_list2=['desktop','laptop','tablet','smartphone']
stok_list2=[12,83,55]
for item_name,stok_count in zip(item_list2,stok_list2):
    print('{}/{}'.format(item_name,stok_count))

print('=====================================')
#python3系
from itertools import zip_longest

item_list3=['desktop','laptop','tablet','smartphone']
stok_list3=[12,83,55]
for item_name,stok_count in zip_longest(item_list3,stok_list3):
    print('{}/{}'.format(item_name,stok_count))

#python2系
'''
# _*_ coding: utf-8 _*_
from itertools import izip_longest

item_list3=['desktop','laptop','tablet','smartphone']
stok_list3=[12,83,55]
for item_name,stok_count in izip_longest(item_list3,stok_list3):
    print '{}/{}'.format(item_name,stok_count) 
'''

print('=====================================')
#fillvalueで補った場合
#python3系
from itertools import zip_longest

item_list4=['desktop','laptop','tablet','smartphone']
stok_list4=[12,83,55]
for item_name,stok_count in zip_longest(item_list4,stok_list4,fillvalue='no stock'):
    print('{}/{}'.format(item_name,stok_count))
