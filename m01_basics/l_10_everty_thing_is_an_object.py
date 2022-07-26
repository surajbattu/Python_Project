# print("---")
# i = 1
# print (f" i value before {i} changing and id of i {id(i)}")
# print("---")
# i = 1+i
# print (f" i value after {i} changing and id of i {id(i)}")
# print("---")
# j=i
# print (f" i value before {i} changing and id of i {id(i)}")
# print (f" j value before {j} changing and id of i {id(j)}")
# print("---")
# i+=1
# print (f" i value after {i} changing and id of i {id(i)}")
# print (f" j value after {j} changing and id of i {id(j)}")
# print("---")
l1 =[1]
print (f" List l1 value before {l1} changing and id of l1 {id(l1)}")
print("---")
l1.append(2)
print (f" List l1 value after {l1} changing and id of l1 {id(l1)}")
print("---")
l2=l1
print (f" List l1 value before {l1} changing and id of l1 {id(l1)}")
print (f" List l2 value before {l2} changing and id of l2 {id(l2)}")
print("---")
l1.append(3)
print (f" List l1 value after {l1} changing and id of l1 {id(l1)}")
print (f" List l2 value after {l2} changing and id of l2 {id(l2)}")
print("---")

def fun(a,b):
    a+=1
    b.append(5)
    print (f" a and b inside function {a} and {b}")
    print("---")
a1=1
b1=[1,2,3]
print(f" a and b before calling function {a1} and {b1}")
print("---")
fun(a1,b1)
print(f" a and b after calling function {a1} and {b1}")
