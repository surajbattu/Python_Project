


print(f'\nNormalization tests\n')
#-----STRING NORMANLIZATION
device_1 = {
    "name": "abCd-ef-4X",
    "vendor": "apple",
    "model": "Mac_Air",
    "os":"Catalina",
    "version":"8.2.32",
    "ip":"10.0.0.23"
}
device_2 = {
    "name": "ABCD-EF-4x",
    "vendor": "APPLE",
    "model": "MaC_AIr",
    "os":"CataLIna",
    "version":"8.2.32",
    "ip":"10.0.0.23"
}

if (
    device_1["name"].lower() ==  device_2["name"].lower()
    and device_1["vendor"].lower() ==  device_2["vendor"].lower()
    and device_1["model"].lower() ==  device_2["model"].lower()
    and device_1["os"].lower() ==  device_2["os"].lower()
    and device_1["version"].lower() ==  device_2["version"].lower()
    and device_1["ip"].lower() ==  device_2["ip"].lower()
):
    print(f'String normalization lower works')
else:
    print(f'String normalization lower does not works')
if (
    device_1["name"].casefold() ==  device_2["name"].lower()
    and device_1["vendor"].casefold() ==  device_2["vendor"].lower()
    and device_1["model"].casefold() ==  device_2["model"].lower()
    and device_1["os"].casefold() ==  device_2["os"].lower()
    and device_1["version"].casefold() ==  device_2["version"].lower()
    and device_1["ip"].casefold() ==  device_2["ip"].lower()
):
    print(f'String normalization casefold works')
else:
    print(f'String normalization casefold does not works')

#-----MAC address normalization

mac_colon = "A0:bc:c4:55"
mac_comma = "A0,bc,C4,55"
mac_dots = "A0.bc.C4.55"
mac_caps = "A0,BC,C4,55"
# Return MAC normalization
def normalization(mac_add):
    return mac_add.lower().replace(":","").replace(",","").replace(".","")
if normalization(mac_comma) == normalization(mac_caps) == normalization(mac_dots)==normalization(mac_colon):
    print(f'Mac address normalization works')
else:
    print(f'Mac address normalization does not works')

#----IP adress Normalization
ip_adress1 = "10.000.01.01"
ip_adress2 = "010.0.01.1"
ip_adress3 = "10.000.1.001"
from ipaddress import IPv4Address
if IPv4Address(ip_adress2) == IPv4Address(ip_adress1) ==IPv4Address(ip_adress3):
    print(f'IP address normalization works')
else:
    print(f'IP address normalization does not works')
