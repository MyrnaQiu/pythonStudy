#prime numbers
count = 0
for i in range(1,101):
    for j in range(2,i):
        if i%j == 0:break
        if i == j+1:
            print(i)
            count += 1
print('100以内的质数有：%d个' %count)
