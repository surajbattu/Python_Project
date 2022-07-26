sum=0
sum1=0
for i in range(101):
    sum = sum + (i*i)
    sum1 = sum1+i
    if i==100:
        print(sum1*sum1 - sum)
