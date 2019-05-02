#17.コンテキストマネージャ
#「__enter__」、「__exit__」が実装されたオブジェクト

#特殊メソッドを実装する

class ContextManagerTest:
    def __enter__(self):
        print('__enter__')

    def __exit__(self,exc_type,exc_value,traceback):
        print('__exit__')
        print(exc_type)
        print(exc_value)
        print(traceback)
        return True

with ContextManagerTest():
    print('with')
    val=int('abc')

class ContextManagerTest2:
    def __enter__(self):
        print('__enter__')
        return 'as obj'

    def __exit__(self,exc_type,exc_value,traceback):
        print('__exit__')

with ContextManagerTest2() as as_obj:
    print(as_obj)

#デコレーターを使用する
#簡単にコンテキストマネージャーを作成する方法

from contextlib import contextmanager

@contextmanager
def context_maneger_text():
    print('enter')
    yield
    print('exit')

with context_maneger_text() :
    print('with')
    print('test')

from contextlib import contextmanager

@contextmanager
def context_maneger_text2():
    print('enter')
    yield 'as_obj'
    print('exit')

with context_maneger_text2() as as_obj:
    print(as_obj)
