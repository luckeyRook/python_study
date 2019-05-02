#12.lambda式
#lambda式とは名前の無い関数のこと

#lambda式の基礎
#↓通常の関数
def puls_value(value_1,value_2):
    return value_1+value_2

print(puls_value(10,100))

#lambda式
l_func=lambda num_1,num_2:num_1 + num_2
print(l_func(10,100))
