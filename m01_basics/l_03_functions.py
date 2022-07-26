from tabulate import tabulate
from random import choice
from operator import itemgetter
import string

def create_device(num_devices, num_subnets):
    device_list = []
    if num_devices >= 254 or num_subnets >= 254:
        print("Too many device or subnets requested")
        return device_list

    for sub_net in range(num_subnets+1):
        for device in range(num_devices+1):
            devices = {}
            devices["name"] = choice(["apple", "microsoft", "intel"]) + choice(["_A", "_Z"]) + choice(
                string.ascii_letters)
            devices["vendor"] = choice(["tata", "infosys"])
            if devices["vendor"] == "tata":
                devices["os"] = "YOUTELLME"""
                devices["version"] = "1.12"
            elif devices["vendor"] == "infosys":
                devices["os"] = "IDONTKNOW"
                devices["version"] = choice(["anything", "everything"])
            devices["ip"] = "10.0.22." + str(sub_net)+"."+ str(device)
            device_list.append(devices)
    return device_list

if __name__ == '__main__':
    created_devices = create_device(2,2)
    print (tabulate(created_devices,headers ="keys"))

