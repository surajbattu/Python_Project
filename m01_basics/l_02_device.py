import string
from operator import itemgetter
from pprint import pprint
from random import choice
from tabulate import tabulate


devices = []

for item in range(10):
    device = {}
    device["name"] = choice(["apple","microsoft","intel"]) + choice(["_A","_Z"]) + choice(string.ascii_letters)
    device["vendor"] = choice(["tata","infosys"])
    if device["vendor"] == "tata":
        device["os"] = "YOUTELLME"""
        device["version"] ="1.12"
    elif device["vendor"] == "infosys":
        device["os"] = "IDONTKNOW"
        device["version"] = choice(["anything","everything"])
    device["ip"] = "10.0.22."+ str(item)
    print(device)
    devices.append(device)
    for key, value in device.items():
        print(f"{key:.10s}:{value}")
pprint (devices)

print (tabulate(sorted(devices,key=itemgetter("name","os","version")),headers="keys"))
