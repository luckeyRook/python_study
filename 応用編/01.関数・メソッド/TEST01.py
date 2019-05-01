#01.関数・メソッド
#関数の基礎
def test_func():
    print('call test_func')

test_func()

#引数の基礎

def test_func2(num_1,num_2,oprn):
    if oprn==1:
        print("足し算開始")
        print(num_1 + num_2)

    elif oprn==2:
        print("引き算開始")
        print(num_1 - num_2)

    elif oprn==3:
        print("掛け算開始")
        print(num_1 * num_2)

    elif oprn==4:
        print("割り算開始")
        print(num_1 / num_2)

    else:
        print("不明なオペレーションです。")


test_func2(100,10,3)

#引数の初期値

def test_func3(num_1,num_2,oprn=1):
    if oprn==1:
        print("足し算開始")
        print(num_1 + num_2)

    elif oprn==2:
        print("引き算開始")
        print(num_1 - num_2)

    elif oprn==3:
        print("掛け算開始")
        print(num_1 * num_2)

    elif oprn==4:
        print("割り算開始")
        print(num_1 / num_2)

    else:
        print("不明なオペレーションです。")


test_func3(100,10)

#引数の初期値設定したものに値をいれた場合

def test_func4(num_1,num_2,oprn=1):
    if oprn==1:
        print("足し算開始")
        print(num_1 + num_2)

    elif oprn==2:
        print("引き算開始")
        print(num_1 - num_2)

    elif oprn==3:
        print("掛け算開始")
        print(num_1 * num_2)

    elif oprn==4:
        print("割り算開始")
        print(num_1 / num_2)

    else:
        print("不明なオペレーションです。")


test_func4(100,10,4)

#関数とメソッド
#関数
def test_func5() :
    print("call test_func5")

class TestClass:
    #メソッド
    def TestMethod():
        print("call TestMethod")

print("-----------------------------")
print(test_func5)
print(TestClass.TestMethod)

print("-----------------------------")
print(type(test_func5))
print(type(TestClass.TestMethod))
    
print("-----------------------------")
t=TestClass()
print(test_func5)
print(t.TestMethod)


