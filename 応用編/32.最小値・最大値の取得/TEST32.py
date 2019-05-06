#32.最小値・最大値の取得
#min
print(min([10,20,30,5,3]))
print(min('Z','A','J','w'))

#max
print(max([10,20,30,5,3]))
print(max('Z','A','J','w'))

#key引数

def key_func(n):
    return int(n)

l=[2,3,4,'111']

print(min(l,key=key_func))
print(max(l,key=key_func))

print('========================================-')
def key_func2(n):
    return str(n)

l=[2,3,4,'111']

print(min(l,key=key_func2))
print(max(l,key=key_func2))

print('========================================-')

l=[2,3,4,'111']

print(min(l,key=int))
print(max(l,key=int))
print(min(l,key=str))
print(max(l,key=str))

print('========================================-')

def key_func3(n):
    return n[2]

#code/name/score
l=[(1,'pyhton',100),(2,'ruby',80),(3,'Perl',40)]

print(min(l,key=key_func3))
print(max(l,key=key_func3))

#クラスで行う場合
def key_func4(n):
    return n.score

class TestClass:
    def __init__(self,code,name,score):
        self.code=code
        self.name=name
        self.score=score

    def __str__(self):
        return '({},{},{})'.format(self.code,self.name,self.score)

l=[
    TestClass(1,'pyhton',100),
    TestClass(2,'ruby',80),
    TestClass(3,'Perl',40)
]

print(min(l,key=key_func4))
print(max(l,key=key_func4))
