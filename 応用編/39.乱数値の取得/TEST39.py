#39.乱数値の取得
#randam

import random

#0.0～1.0までのfloat値を取得します。
print(random.random())
#設定された引数間のfloat値を取得します。
print(random.uniform(1,100))
#設定された引数間のint値を取得します。
print(random.randint(1,100))
#設定された引数間の値を取得します。
print(random.choice('1234567890abcdefghij'))

sample_list=['python','izm','com','random','sample']
#配列の並びをシャッフルします。
random.shuffle(sample_list)
print(sample_list)