from random import choice
import string

def create_devices(num_devices, num_subnets):
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
def create_devices_tuple(num_devices, num_subnets):


    return tuple(create_devices(num_devices=num_devices, num_subnets=num_subnets))