#rangeとxrange

for num in range(10):
    print(num)



print('------------------------------------------')
#引数を二つ設定した場合

for num in range(2,10):
    print(num)


print('------------------------------------------')

#引数に負の値を設定した場合

for num in range(-2,10):
    print(num)

print('------------------------------------------')

#xrangeを使用する場合
#xrangeはpython2のみ使用可能
#当環境はpython3のため、記述のみ
#メモリ効率が良い→python3ではrangeが改善されたため、撤廃

for num in xrange(10):
    print(num)
