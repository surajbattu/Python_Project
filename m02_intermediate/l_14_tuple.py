from create_utils.util import create_devices, create_devices_tuple
from pprint import pprint
from collections import namedtuple
if __name__ == '__main__':
    devices = create_devices(1,1)
    print("--------------------------")
    pprint(tuple(devices))
    devices = create_devices_tuple(1,1)
    print("--------------------------")
    pprint(devices)

print("----Device as tuple--")
print("--------------------------")
device = ("r3-f7-10tesla", "cisco", "catalyst 2960", "ios","1.2.3.4" )
print ("  name :",device[0])
print ("  vendor :",device[1])
print ("  model :",device[2])
print ("  os :",device[3])
print ("  version :",device[4])

print("--------------------------")
print("----Named Tuples")
Device = namedtuple('Device',['name','vendor','model','os','version'])
device = Device("r3-f7-10tesla", "cisco", "catalyst 2960", "ios","1.2.3.4" )
print ("  name :",device.name)
print ("  vendor :",device.vendor)
print ("  model :",device.model)
print ("  os :",device.os)
print ("  version :",device.version)

print("----PPRINT Named Tuples")
pprint(device)
print("----Convert devices to  Named Tuples")

devices = create_devices(num_subnets=4,num_devices=5)
create_named_tuple = list()
for device in devices:
    Device = namedtuple('Device',device.keys())
    create_named_tuple.append(Device(**device))
pprint(create_named_tuple)

print("----NICELY Named Tuples")
print ("  NAME    Vendor : OS    IP Address")
print ("  ----    ------ : --    -- -------")

for device in create_named_tuple:
    print (f'{device.name:>15} {device.vendor:>10} {device.os:<6} {device.ip:>15}')


