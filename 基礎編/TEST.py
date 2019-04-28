#文字列
print('python-izm')
print("python-izm")

#複数行出力させる場合
test_str="""
test_1
test_2
"""
print(test_str)

#文字の連結
test_str ='python'
test_str =test_str +'-'
test_str =test_str + 'izm3'
print(test_str)

#文字列の追加

test_str ='012'
test_str += '345'
test_str += '678'
print(test_str)

#文字列に対して「＊」を使用する場合、文字の繰り返しとなる

test_str='012'*3
print(test_str)

#文字列の変換方法
test_integer=100
print(str(test_integer)+'円')

#文字列の置換
test_str='python-izm4'
print(test_str.replace('izm','ism'))

#文字列の分割
test_str='python-izm5'
print(test_str.split('-'))

#文字数のそろえ方（0埋めとか:文字指定編）
test_str='999'
print(test_str.rjust(10,'1'))
print(test_str.rjust(10,'!'))

#文字数のそろえ方（0埋めとか:指定なし編）
test_str='888'
print(test_str.zfill(10))
print(test_str.zfill(2))

#文字列の検索 先頭検索
test_str='python-izm5'

print(test_str.startswith("python"))
print(test_str.startswith("izm"))

#文字列の検索 部分検索

print('z' in test_str)
print('a' in test_str)

#文字列変換
test_str='Python-Izm.COM'

print(test_str.upper())
print(test_str.lower())

#先頭・末尾の削除
print('------------------------------------------------')
test_str='          python-izm.com'
print(test_str)

test_str=test_str.lstrip()
print(test_str)

test_str=test_str.lstrip('python')
print(test_str)

print('------------------------------------------------')
test_str='python-izm.com          '
print(test_str+'/')

test_str=test_str.rstrip()
print(test_str+'/')

test_str=test_str.rstrip("com")
print(test_str+'/')
