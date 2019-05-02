#13.ジェネレータ
#ジェネレータとは反復可能なオブジェクトのこと

#ジェネレータの基礎
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)

#疑似コード
#for i in <ジェネレータ>:
#    print(i)

#ジェネレータ関数のyield

def func_sample():
    yield("おはよう")
    yield("こんにちは")
    yield("こんばんわ")

for i in func_sample():
    print(i)

print('--------------------------------')
def func_sample2():
    yield("おはよう")
    yield("こんにちは")
    yield("こんばんわ")

f = func_sample2()
print(next(f))
print(next(f))
print(f.__next__())

#ジェネレータ式
#内包表記
gen_sample = (i for i in 'おはよう　こんにちは　こんばんは'.split())
print(gen_sample)
for i in gen_sample:
    print(i)
