#例外処理
#try,except,finaliy

def exception_test(value_1,value_2):
    print('====計算開始====')
    result=0

    try:
        result=value_1+value_2
    except:
        print('計算できませんでした')
    finally:
        print('計算終了')
    
    return result

print(exception_test(100,200))
print(exception_test(100,'200'))

#raise
def exception_test2(value_1,value_2):
    print('====計算開始====')
    result=0

    try:
        result=value_1+value_2
    except:
        print('計算できませんでした')
        raise
    finally:
        print('計算終了')
    
    return result

try:
    print(exception_test2(100,200))
    print(exception_test2(200,200))
    print(exception_test2(300,'200'))
except:
    print('エラーを受け取りました')

#エラー内容の取得
#サイトの記述だとちゃんとでないので、少し改変
#import sys
import traceback

def exception_test3(value_1,value_2):
    print('====計算開始====')
    result=0

    try:
        result=value_1+value_2
    except:
        print('計算できませんでした')
        raise
    finally:
        print('計算終了')
    
    return result

try:
    print(exception_test3(100,'200'))
except :
    print('--------------------')
    print(traceback.format_exc())
    print('--------------------')

