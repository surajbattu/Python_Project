from pprint import pprint

device = {
    "name": "abCd-ef-4X",
    "vendor": "apple",
    "model": "Mac_Air",
    "os":"Catalina",
    "version":"8.2.32",
    "ip":"10.0.0.23"
}

# SIMPLE PRINT
print("\n----Simple Print----")
print ("device", device)
print ("device name", device["name"])

# PRETTY PRINT
print("\n----Pretty Print---")
pprint( device)

# NICELY FORMATTED PRINT
print("\n----NICE Print----")
for key, value in device.items():
    print(f"{key:>8s}:{value}")
