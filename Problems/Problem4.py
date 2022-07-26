palimList = []
def palimum():
    for i in range(100,999):
        for j in range(100,999):
            num = i * j
            StrNum = str (num)
            if StrNum == StrNum[::-1]:
                StrNum = int(StrNum)
                palimList.append(StrNum)
    return (palimList)

List = palimum()
print(List)
largest_number = List[0]
for number in List:
    if number > largest_number:
        largest_number = number
print(largest_number)