#23.要素を区切り文字で連結
#str.join

#これを「www.python-izm.com」にしたい
elem=['www','python-izm','com']

#失敗例
host_name=''
for val in elem:
    host_name += val +'.'
print(host_name)

#改善例
elem=['www','python-izm','com']
host_name2=''
for val in elem:
    if val != 'com':
        host_name2 += val +'.'
    else:
        host_name2 += val
print(host_name2)

#str.joinを使用した場合
print('.'.join(elem))

#他
elem2=['www','python-izm','com']
print('\n'.join(elem2))
print(','.join(elem2))
print(' '.join('1234567890'))

print('+'.join(('1','2','3')))