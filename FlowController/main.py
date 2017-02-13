import threading
from crop import *
from sensor_data import *

INTERVAL = 1  # Interval to check the water flow (sec)
crop_list = []

def check():
	# Update water flow rates of each crop
	data = get_flow_data()

	for i in range(len(crop_list)):
		crop = crop_list[i]

		if crop.state == "ACTIVE":
			crop.supplied_volume += data[i] * INTERVAL / 60 #!flow rate is per minute
			print(" {0}:\t{1}\t({2})".format(crop.name, crop.supplied_volume, crop.volume_to_supply)) #

			if crop.supplied_volume > crop.volume_to_supply:
				crop.state = "FINISHED"
				#<< Close the valve of the crop >>#
		elif crop.state == "FINISHED":
			print(" {0}:\tValve Closed".format(crop.name)) #

	print("="*35) #

	threading.Timer(INTERVAL, check).start()

# Crop 1
crop1 = Crop("Crop 1", 2.0)
crop1.set_minimum_water_requirement(2)
crop_list.append(crop1)

# Crop 2
crop2 = Crop("Crop 2", 10.0)
crop2.set_minimum_water_requirement(3)
crop_list.append(crop2)

# Crop 3
crop3 = Crop("Crop 3", 8.0)
crop3.set_minimum_water_requirement(5)
crop_list.append(crop3)

# Start Checking
check()
