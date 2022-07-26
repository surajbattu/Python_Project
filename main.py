from tabulate import tabulate_formats
print("My name is Suraj Battu")
x = 1
if x==1:
    print ("x is", x)
    myX=float(x)
    print (x,myX)
    Xstring = "Hi"
    Xstring1 = 'Hi'
    print(Xstring1.upper())
    print(Xstring +" and "  + Xstring1 + " and " +str(x))
MyList = []
MyList.append("hi")
MyList.append('hello')
print(MyList)
print ("First item in the list is "+MyList[0])
for i in MyList:
    print(i)


x_list = [1]*10
y_list = [2]*10
big_list = x_list+y_list
print (big_list)
import numpy as np
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
# Create a numpy array np_weight_kg from weight_kg
np_weight = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg
np_pounds = np_weight * 2.2
# Print out np_weight_lbs
print(np_pounds)

directory = {"Country":["India","America"],
        "Capital":["Delhi","DC"]}
import pandas as pd
Dir_DataFrame = pd.DataFrame(directory)
print(Dir_DataFrame)

