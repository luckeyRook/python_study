#四則演算
test_integer = 100

print(test_integer + 10) #足し算
print(test_integer - 10) #引き算
print(test_integer * 10) #掛け算
print(test_integer / 10) #割り算

#数値型への変換
test_str='100'

print(int(test_str)+100)

#不動小数点への変換
test_str='100.5'

print(float(test_str)+100)

#不動小数点（省略ver）
test_float=.5
print(test_float)

#複素数への変換
test_complex=100 + 5j
print(test_complex)
print(test_complex.real)
print(test_complex.imag)



