from tabulate import tabulate
##from create_utils.util import create_devices
import create_utils.util as CU
if __name__ == '__main__':
    created_devices = CU.create_devices(2,2)
    print (tabulate(created_devices,headers ="keys"))