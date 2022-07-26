import yaml

from l_00_inventory import device
with open("l_00_inventory.yaml","w") as yopen:
    yopen.write(yaml.dump(device, indent=4))
with open("l_00_inventory.yaml","r") as yread:
     yaml_inventory = yread.read()
with open("l_00_alternamtive_inventory.yaml", "r") as yread:
    yaml_slternative_inventory = yread.read()
# Printing  Invetory from YAML file
print("Printing  Inventory from YAML file\n",yaml_inventory)

# Convert YAML to Python and back to STRING for printing
print(f'\n YAML pretty version\n')
print(yaml.dump(yaml.safe_load(yaml_inventory),indent=4))

# Compare original inventory with inventory we wrote

print("---------------------------------")
inventory_we_wrote = yaml.safe_load(yaml_inventory)

if device == inventory_we_wrote:
    print("BOTH ARE EQUAL")
else:
    print("ERROR: BOTH ARE NO EQUAL")
print("---------------------------------")
inventory_we_wrote_1 = yaml.safe_load(yaml_slternative_inventory)
if device == inventory_we_wrote_1:
    print("BOTH ARE EQUAL")
else:
    print("ERROR: BOTH ARE NO EQUAL")



