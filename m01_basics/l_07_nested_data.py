import copy
from pprint import pprint
from random import choice
from create_utils.util import create_devices
device = {
    "name":"r3-lx-02",
    "vendor": "cisco",
    "model" : "catalyst 290",
    "os"    : "ios",
    "interfaces":[]
}

print(f'\n\n-----devices with no interfaces---')
for key, value in device.items():
    print(f'{key:>16s} : {value}')

interfaces = list()
for index in range(0,8):
    interface = {
        "name":"g/0/0/"+str(index),
        "speed" : choice(["10","100","1000"])
    }
    interfaces.append(interface)
device["interfaces"] = interfaces
print(f'\n\n-----devices with interfaces---')
for key, value in device.items():
    if key != "interfaces":
        print(f'{key:>16s} : {value}')
    else:
        print(f'{key:>16s} :')
        for iternface in interfaces:
            print(f'\t\t\t\t\t{interface}')
print()
print(f'\n\n-----devices with interfaces with pprint---')
pprint(device)
print(f'\n\n-----network with devices d interfaces---')


