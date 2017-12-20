#Fibonacci
count = 0
for i in range(1,101):
    if i==1:
        n1=1
        print(n1)
    elif i==2:
        n2=1
        print(n2)
    else:
        n1,n2 = n2,n1+n2
        print(n2)
    count += 1
print('总共输出:%d个Fibonacci数' %count)
