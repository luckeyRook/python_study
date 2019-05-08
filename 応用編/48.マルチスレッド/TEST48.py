#48.マルチスレッド
#複数のスレッドによる処理
import threading
import time
import datetime

class TestThread(threading.Thread):
    def run(self):
        print(' === start sub thread === ')
        for i in range(5):
            time.sleep(5)
            print('  sub thread : '+ str(datetime.datetime.today()))
        print(' === end sub thread === ')
        
th = TestThread()
th.start()

time.sleep(1)

print('=== start main thread === ')
for i in range(5):
    time.sleep(10)
    print('main thread : '+ str(datetime.datetime.today()))
print('=== end main thread === ')

print('=========================================')

#デーモンスプレッド
import threading
import time
import datetime

class TestThread2(threading.Thread):
    def run(self):
        print(' === start sub thread === ')
        for i in range(5):
            time.sleep(5)
            print('  sub thread : '+ str(datetime.datetime.today()))
        print(' === end sub thread === ')
        
th2 = TestThread2()
th2.daemon=True
#th2.daemon=false
th2.start()

time.sleep(1)

print('=== start main thread === ')
for i in range(5):
    time.sleep(10)
    print('main thread : '+ str(datetime.datetime.today()))
print('=== end main thread === ')

