i = 3
count  = 1
while True:
    for idx in range (2,i):
        if i%idx == 0:
            break
        if idx == (i-1):
            count += 1
            if count == 10001:
                print(i)
                exit()
    i += 1

      