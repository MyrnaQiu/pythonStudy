#Fibonacci
count = 0
n1=1
n2=0
for i in range(1,101):     
    n1,n2 = n2,n1+n2
    print(n2)
    count += 1
print('总共输出:%d个Fibonacci数' %count)
