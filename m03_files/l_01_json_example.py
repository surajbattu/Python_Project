import json
from l_00_inventory import device
with open("l_00_inventory.json","w") as jopen:
    jopen.write(json.dumps(device, indent=4))
with open("l_00_inventory.json","r") as jread:
     json_inventory = jread.read()

# Printing  Invetory from Json file
print("Printing  Inventory from Json file\n",json_inventory)

# Convert JSON to Python and back to STRING for printing
print(f'\n Json pretty version\n')
print(json.dumps(json.loads(json_inventory),indent=4))

# Compare original inventory with inventory we wrote

print("---------------------------------")
inventory_we_wrote = json.loads(json_inventory)
if device == inventory_we_wrote:
    print("BOTH ARE EQUAL")
else:
    print("ERROR: BOTH ARE NO EQUAL")



