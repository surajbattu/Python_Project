device_str =" r3-f7-10tesla, cisco, catalyst 2960, ios ,extra stupid stuff "
device =[]
for item in device_str.split(","):
    device.append(item.strip())
print(f'\ndevice using for loop\n\t\t {device}')

#LIST COMPREHENSION
device = [item.strip() for item in device_str.split(",") ]
print(f'\ndevice using for LIST COMPREHENSION\n\t\t {device}')
#LIST COMPREHENSION in simpler way
new_device_str = device_str.split(",")
device = [item.strip() for item in new_device_str ]
print(f'\ndevice using for LIST COMPREHENSION in simpler way\n\t\t {device}')
#LIST COMPREHENSION with CONDITION
device = [item.strip() for item in device_str.split(",") if "stupid" not in item ]
print(f'\ndevice using for LIST COMPREHENSION with CONDITION\n\t\t {device}')

device_info = [
    ("name","r3-lx-02"),
    ("vendor", "cisco"),
    ("model" , "catalyst 290"),
     ("os"   ,  "ios"),
]
#DICT comprehenstion from list of tuples
device = {item[0]:item[1] for item in device_info}
print(f'\ndevice using DICT comprehenstion from list of tuples\n\t\t {device}')
print("Nicely printed ")
for key, value in device.items():
    print(f'{key:>16s} : {value}')

device_inf0_str = "name: r3-f7-10tesla, vendor:cisco,model: catalyst 2960, os:ios ,version:v12.12"
#LIST THEN DICT COMPREHNSION FROM STRING
device_key_pairs = [kv_pair.split(":") for kv_pair in device_inf0_str.split(",")]
device = {item[0]:item[1] for item in device_key_pairs}
print(f'\nusing list and dict comphrehension\n\t\t {device} ')
print("Nicely printed again")
for key, value in device.items():
    print(f'{key:>16s} : {value}')
#DICT COMPREHENSION FROM STRING
device = {item.split(":")[0]:item.split(":")[1] for item in device_inf0_str.split(",")}
print(f'\nusing  dict comphrehension\n\t\t {device} ')
print("Nicely printed again and again")
for key, value in device.items():
    print(f'{key:>16s} : {value}')