import threading
from crop import *
from sensor_data import *

INTERVAL = 1  # Interval to check the water flow (sec)
crop_list = []


def set_crop_details():
    crop1 = Crop("Crop 1", 2.0)
    crop1.set_minimum_water_requirement(2)
    crop_list.append(crop1)

    crop2 = Crop("Crop 2", 10.0)
    crop2.set_minimum_water_requirement(3)
    crop_list.append(crop2)

    crop3 = Crop("Crop 3", 8.0)
    crop3.set_minimum_water_requirement(5)
    crop_list.append(crop3)

def print_info():
    print("-"*35 + "\nFLOW CONTROLLER")
    print("INTERVAL\t: {0} sec".format(INTERVAL))
    print("NUMBER OF CROPS\t: {0}".format(len(crop_list)))
    print("-"*35)
    print(" CROP\t\tWATER VOLUME\tTODAY\tSTATE")


def check():
	# Update water flow rates of each crop
	data = get_flow_data()
	print_info()

	for i in range(len(crop_list)):
		crop = crop_list[i]
        
		print(" {0}:\t{1}\t\t{2}\t{3}".format(crop.name, crop.supplied_volume if crop.state == "ACTIVE" else crop.volume_to_supply, crop.volume_to_supply, crop.state))
        
		if crop.state == "ACTIVE":
			crop.supplied_volume += data[i] * INTERVAL / 60 #!flow rate is per minute

			if crop.supplied_volume > crop.volume_to_supply:
				crop.state = "FINISHED"
				#<< Close the valve of the crop >>#

        
            


            
	print("-"*35 + "\n\n") #

	threading.Timer(INTERVAL, check).start()


def start():
    set_crop_details()
    check()


start()
