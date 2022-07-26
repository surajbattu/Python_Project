
NumLst = []
for num in range(1000):
    if num % 3 == 0 or num % 5 == 0:
        NumLst.append(num)

print(sum(NumLst))
