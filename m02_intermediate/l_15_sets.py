available_ips =set()
used_ips =set()
def print_ips():
    # print("Available ips ",available_ips)
    # print("Used ips ", used_ips)
    used_ips_list = list(used_ips)
    available_ips_list = list(available_ips)
    if len(available_ips_list)>len(used_ips_list):
        for _ in range(0, len(available_ips_list)-len(used_ips_list)):
            used_ips_list.append("")
    elif len(used_ips_list)>len(available_ips_list):
        for _ in range(0,len(used_ips_list)-len(available_ips_list)):
            available_ips_list.append("")
    print()
    print("      Available   Used")
    print("      ---------   ----")
    for available, used in zip(available_ips_list,used_ips_list):
        print (f'{available:>16} {used:<16}')

for index in range(180,200,3):
    available_ips.add("10.0.1."+str(index))

print_ips()
while True:
    ip_address = input("\nEnter an IP  address:")
    if not ip_address:
        print("Exiting ...")
        exit()
    if ip_address in available_ips:
        available_ips.remove(ip_address)
        used_ips.add(ip_address)
        print_ips()
        if len(available_ips.intersection(used_ips))>0:
            print(f'ERROR:Some IPs are used more than once')
    else:
        print(f'ip adress is not found in avaible ips')
