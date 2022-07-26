import re

Find_Member = []
for member in dir(re):
    if 'find' in member:
        Find_Member.append(member)


print(sorted(Find_Member))




