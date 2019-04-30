#スライス
#スライスの基本
test_list=['https','www','python','izm','com']
print(test_list[:])
print(test_list[::])

#要素の取得
test_list_2=['https','www','python','izm','com']
#終了位置指定
print(test_list_2[:4])

#開始位置指定
print(test_list_2[2:])

#ステップ幅指定
print(test_list_2[::2])

#開始・終了位置指定
print(test_list_2[3:5])

#負の数値を入れた場合
test_list_3=['https','www','python','izm','com']
print(test_list_3[-1:]) #末尾から全ての要素
print(test_list_3[:-1]) #末尾まで全ての要素
print(test_list_3[::-1]) #末尾から逆順の要素

#要素を超過した場合
test_list_4=['https','www','python','izm','com']
print(test_list_4[:999]) #末尾から全ての要素


#要素の代入
test_list_5=['https','www','python','izm','com']
test_list_5[1:3]=('WWW','PYTHON')
print(test_list_5) #末尾から全ての要素
