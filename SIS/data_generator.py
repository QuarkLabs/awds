import csv
import os
import random

raw_file_path = os.path.abspath("sample_data/raw_data.csv")

# Create a new csv file
raw_file = open(raw_file_path, 'w')

writes = csv.writer(raw_file, delimiter=',', quoting=csv.QUOTE_NONE, lineterminator='\n')

crop_types = [1, 2]
ages = [1, 2, 3]
temperatures = [25, 26, 27, 28, 29, 30]
showers = [1, 2, 3, 4]
# moisture

rows = []

# Add default lines
row_count = len(crop_types) * len(ages) * len(temperatures) * len(showers)
column_count = 5
rows.append([row_count, column_count])
rows.append(["TYPE", "AGE", "TEMPERATURE", "SHOWER", "MOISTURE", "REQ_WATER"])

# Generate sample data
for crop_type in crop_types:
    for age in ages:
        for temperature in temperatures:
            for shower in showers:
                base_moisture = (shower * 0.2) / temperature
                moisture_off = base_moisture * 0.01
                moisture = random.uniform(base_moisture - moisture_off, base_moisture + moisture_off)

                base_req_water = 1.0 / (moisture * 0.5)
                req_water_off = base_req_water * 0.01

                req_water = random.uniform(base_req_water - req_water_off, base_req_water + req_water_off)
                rows.append([crop_type, age, temperature, shower, round(moisture, 5), round(req_water, 5)])

# Write the data to csv file
for row in rows:
    writes.writerow(row)
