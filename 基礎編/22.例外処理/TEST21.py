#エラー内容の取得
#おまけ
import sys
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
#except Exception as e:
#    t,v,tb=sys.exc_info()
    print('--------------------')
    print(traceback.format_exc())
#    print(traceback.format_exception(t,v,tb))
#    print(traceback.format_tb(e.__traceback__))
    print('--------------------')
