from l_03_functions import create_device
from pprint import pprint
from time import sleep
from operator import itemgetter
from random import choice
from datetime import datetime
from tabulate import tabulate

devices = create_device(5,2)
pprint (devices)
for device in devices:
    sleep(0.1)
    device["last_heard"] = str(datetime.now())
    print(device)
print (tabulate(sorted(devices,key=itemgetter("name","os","version")),headers="keys"))

print ("  NAME    Vendor : OS    IP Address    Last Heard")
print ("  ----    ------ : --    -- -------    ---- ----------")
for deivce in devices:
    print(
        f'{device["name"]:>7} {device["vendor"]:>10} {device["os"]:<6} {device["ip"]:>15} {device["last_heard"][:-4]}'
    )
for device in sorted(devices, key=itemgetter("last_heard"),reverse=True):
    print(
        f'{device["name"]:>7} {device["vendor"]:>10} {device["os"]:<6} {device["ip"]:>15} {device["last_heard"][:-4]}'
    )
for device in devices:
    print (device["name"],end="")
    sleep(.3)
    print(" ....waiting done")