from create_utils.util import create_devices
from pprint import pprint
from random import randint, uniform
from datetime import datetime

devices = create_devices(num_devices=25, num_subnets=2)
print ("  NAME    Vendor : OS    IP Address    Last Heard")
print ("  ----    ------ : --    -- -------    ---- ----------")
for device in devices:
    print(
        f'{device["name"]:>15} {device["vendor"]:>10} {device["os"]:<6} {device["ip"]:>15} {device["version"]}'
    )
print ("  NAME    Vendor : OS    IP Address    Version")
print ("  ----    ------ : --    -- -------    ---- ----------")
for device in devices:
    if device["vendor"].lower=="tata":
        print(
            f'{device["name"]:>15} {device["vendor"]:>10} {device["os"]:<6} {device["ip"]:>15} {device["version"]}'
        )
print(f"\n Starting companrision of device name")
for index, device_a in enumerate(devices):
    for device_b in devices[index+1:]:
        if device_a["name"]==device_b["name"]:
            print(f' Match found for {device_a["ip"]} and {device_b["ip"]}')

print(f"\n End of companrision of device name")

print(f"\n Creating standard versions")
standard_versions ={}
for device in devices:
    vesrion_os = device["vendor"]+":"+device["os"]
    if vesrion_os not in standard_versions:
        standard_versions[vesrion_os] = device["version"]
print (standard_versions)
print(f"\n Creating non complaint device")
non_complaint_devices = dict()
for version_os,_ in standard_versions.items():
    non_complaint_devices[version_os] = []

for device in devices:
    vesrion_os = device["vendor"]+":"+device["os"]
    if device["version"] != standard_versions[vesrion_os]:
        non_complaint_devices[version_os].append(device["ip"] + " version "+device["version"])

pprint(non_complaint_devices)

print(f"\n Assignment COPY and DEEPCOPY")
devices2= devices
devices[0]["name"] = "JUNK"
if devices == devices2:
    print(f"\n Assignment and modifications are same")
    print(f"\n Assignment is not same as COPY")
else:
    print(f"\n hmm some thing went wrong")
print("-------------")
from copy import copy, deepcopy
devices2= copy(devices)
devices2[0]["name"] = "ANOTHER JUNK"
if devices == devices2 :
    print(f"\n Shallow copy and modifications are same")
    print(f"\n Copy only copies the first level not entire object ")
else:
    print(f"\n hmm some thing went wrong")
print("-------------")
devices2= deepcopy(devices)
devices[0]["name"] = "JUNK"
if device == devices2 :
    print(f"\n hmm some thing went wrong")
else:
    print(f"\n Deep copy and modifications are not same")
    print(f"\n Deep Copy copies complete object ")

std_avail = 96
std_res = 1.0
for device in devices:
    device["avail"] = randint(94,100)
    device["res"] = uniform(0.5,1.5)
    if device["avail"] < std_avail:
        print(f"{datetime.now()} :  -availability  < {std_avail}")
    if device["res"] < std_res:
        print(f"{datetime.now()} :  -response time  < {std_res}")

print(f'\n Caomparing classes')

class DeviceWithEQ:
    def __init__(self,name,ip):
        self.name = name
        self.ip = ip
        
    def __eq__(self, other):
        if  not isinstance(other,DeviceWithEQ):
            return False
        return self.name == other.name and self.ip==other.ip

d1= DeviceWithEQ("device 1","10.0.01")
d1_equal = DeviceWithEQ("device 1","10.0.01")
d1_different = DeviceWithEQ("device 2","10.0.02")
if d1== d1_equal:
    print(f"\n{d1} :  equals to {d1_equal}")
else:
    print(f"Some thing went wrong")
print("-------------")
if d1== d1_different:
    print(f"Some thing went wrong")
else:
    print(f"\n{d1} : not  equals < {d1_different}")
print("-------------")

class DeviceWithNoEQ:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
d1= DeviceWithNoEQ("device 1","10.0.01")
d1_equal = DeviceWithNoEQ("device 1","10.0.01")
d1_same = d1
if d1== d1_equal:
    print(f"Some thing went wrong")
else:
    print(f"\n{d1} : not equals to {d1_equal}")
print("-------------")
if d1== d1_same:
    print(f"\n{d1} :  equals < {d1_same}")
else:
    print(f"Some thing went wrong")

print("-------------")



