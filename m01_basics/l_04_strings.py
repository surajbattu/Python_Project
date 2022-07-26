from pprint import pprint

big_string = " This US-IND-99, is Huge string , ok "
#SPLIT
#print("Using split")
split_str = big_string.split(",")
print("     ",split_str)
#Strip then Split
split_str = big_string.strip().split(",")
print("     ",split_str)
#Remove blanks
split_str = big_string.replace(" ","").split(",")
print("     ",split_str)
#Remove blanks and replace comma with colon
split_str = big_string.replace(" ","").replace(",",":")
print("     ",split_str)
#Strip every item
split_str = list()
for item in big_string.split(","):
    split_str.append(item.strip())
print("     ",split_str)
#IGNORE CASE
upper_case = "UPPERCASE"
if upper_case=="uppercase":
    print(f" match:{upper_case}")
else:
    print(f"Didnt Match:{upper_case}")
if upper_case.lower()=="uppercase":
    print(f" match:{upper_case}")
else:
    print(f"Didnt Match:{upper_case}")
if upper_case.lower()=="upperCAse".lower():
    print(f" match:{upper_case}")
else:
    print(f"Didnt Match:{upper_case}")
#Find
expected_str = "US"
index = big_string.find(expected_str)
if index>=0:
    print(expected_str + " found at position "+ str(index))
    print(f"{expected_str} found at position {index}")
else:
    print("Didnt find")
#Enumerate
split_str = big_string.split(",")
for item, string_part in enumerate(split_str):
    print(f"Part number {item+1}:{string_part}")

str_lines = """
GigaBitEtherNet1
       Switching Path   Pkts In   Chars In    Pkts Out   Chars Out
            Processor     25376   152666          8242      494554
          Route cache     25376   152666          8242      494554
    Distributed cache     25376   152666          8242      494554
                Total     25376   152666          8242      494554
GigaBitEtherNet2
       Switching Path   Pkts In   Chars In    Pkts Out   Chars Out
            Processor     25376   152666          8242      494554
          Route cache     25376   152666          8242      494554
    Distributed cache     25376   152666          8242      494554
                Total     25376   152666          8242      494554
"""
string_counter =dict()
string_counter1 =dict()
split_str_lines = str_lines.splitlines()
for item, splitted_str in enumerate(split_str_lines):
    #print(splitted_str)
    #if splitted_str=="GigaBitEtherNet":
    if splitted_str.find('GigaBitEtherNet',0)==0:
        current_line = split_str_lines[index+6]
        string_counter[splitted_str] = current_line.split()[1:]
       # string_counter1[splitted_str[1:6].strip()] = splitted_str[6:]
pprint(string_counter)
pprint(string_counter1)

