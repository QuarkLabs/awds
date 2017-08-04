class Crop:
    def __init__(self, name, size):
        self.name = name                # Name of the Crop
        self.size = size			    # Size of the crop field in sq.ft.
        self.state = "ACTIVE"		    # ACTIVE FINISHED CANCELLED
        self.volume_to_supply = 0.00	# Water volume to serve in a Day
        self.supplied_volume = 0.00	    # Supplied water volume
        
    def set_min_req(self, req):
        self.min_req = req

    def set_minimum_water_requirement(self, volume): # ltr / per day, per sq.ft
    	self.volume_to_supply = volume * self.size
