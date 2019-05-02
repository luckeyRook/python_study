#16.with文
#with文の基礎

with open('file.txt') as f:
    #
    #何らかの処理を行う
    #
    print(f.closed)

print(f.closed)

f=open('file.txt')

#with文は下の処理と同じ動きをする
try:
    #
    #何らかの処理を行う
    #
    pass
except:
    pass
finally:
    f.close()