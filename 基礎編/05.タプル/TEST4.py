#タプル：配列の一つ
#作成後に要素の追加と削除ができない。
#つまり、固定された配列となる。

import datetime

def get_today():
    today = datetime.datetime.today()
    #ここで要素を（）でくくることで3つの要素を持ったタプルを作成できる
    value = (today.year,today.month,today.day)

    return value

test_tuple = get_today()
print(test_tuple)
print(test_tuple[0])
print(test_tuple[1])
print(test_tuple[2])
