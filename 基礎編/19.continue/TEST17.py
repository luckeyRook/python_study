#continue
#continueの基礎

for num in range(100):

    #10で割り切れないものは、continueされる
    if num%10:
        continue
    print(num)

