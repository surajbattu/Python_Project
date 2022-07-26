n1, n2 = 0, 1
fibList = []
while n2 < 4000000:
       nth = n1 + n2
       if nth%2 == 0:
           fibList.append(nth)
       n1 = n2
       n2 = nth

print(sum(fibList))
