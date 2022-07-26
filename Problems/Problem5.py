i = 1
while True:
    for j in range(1,21):
        if (i % j) != 0:
            break
        if (i % j) == 0 and j==20:
            print(i)
            exit()
    i += 1

