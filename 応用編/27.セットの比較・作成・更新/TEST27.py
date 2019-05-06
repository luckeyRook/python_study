#27.セットの比較・作成・更新
#セットを比較
test_set_1=set({'python','-','izm','.','com'})

#共通の関数を「持たない」時にture
print(test_set_1.isdisjoint({'python','izm'}))
print(test_set_1.isdisjoint({1,2,3}))

print('--------------------------------')

#全要素が一致していればture
print(test_set_1.issubset({'python','izm'}))
print(test_set_1.issubset({'python','-','izm','.','com'}))

print('--------------------------------')

#全要素が「含まれて」いればしていればture
print(test_set_1.issuperset({'python','izm'}))
print(test_set_1.issuperset({'www','python','-','izm','.','com'}))
print('--------------------------------')

#演算子で同様の結果を得ることが可能
#issubsetと同様の結果
print(test_set_1 <= {'python','izm'})
print(test_set_1 <= {'python','-','izm','.','com'})
print('--------------------------------')
#issupersetと同様の結果
print(test_set_1 >={'python','izm'})
print(test_set_1 >= {'www','python','-','izm','.','com'})


#セットを比較して作成
print('================================')

test_set_2={'python','izm','com'}

print(test_set_2.union({'python','www'}))
print(test_set_2.intersection({'python','www'}))
print(test_set_2.difference({'python','www'}))
print(test_set_2.symmetric_difference({'python','www'}))

#演算子で同様の結果を得ることが可能
print('--------------------------------')

print(test_set_2 | {'python','www'})
print(test_set_2 & {'python','www'})
print(test_set_2 - {'python','www'})
print(test_set_2 ^ {'python','www'})

#セットを比較して更新
print('================================')

test_set_3=set({'python','izm','com'})
test_set_3.intersection_update({'python','www'})
print(test_set_3)

print('--------------------------------')

test_set_3=set({'python','izm','com'})
test_set_3.difference_update({'python','www'})
print(test_set_3)

test_set_3=set({'python','izm','com','www'})
test_set_3.difference_update({'python','www'})
print(test_set_3)

print('--------------------------------')

test_set_3=set({'python','izm','com'})
test_set_3.symmetric_difference_update({'python','www'})

print(test_set_3)

test_set_3=set({'izm','com','www'})
test_set_3.symmetric_difference_update({'python','www'})

print(test_set_3)

print('--------------------------------')

#演算子で同様の結果を得ることが可能
test_set_3={'python','izm','com'}
test_set_3 &={'python','www'}

print(test_set_3)

print('--------------------------------')
test_set_3={'python','izm','com'}
test_set_3 -={'python','www'}

print(test_set_3)

print('--------------------------------')
test_set_3={'python','izm','com'}
test_set_3 ^={'python','www'}

print(test_set_3)


#セットを比較して更新
print('================================')
