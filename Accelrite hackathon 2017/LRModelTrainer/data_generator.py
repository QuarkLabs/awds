import csv
import os
import random

crop_types = [1, 2]
ages = [1, 2, 3]
temperatures = [25, 26, 27, 28, 29, 30]
showers = [1, 2, 3, 4]

off_percentage = 0.01

min_moisture = 0.0
max_moisture = 10.0
min_req_water = 0.0
max_req_water = 100.0


def calculate_moisture(shower, temperature):
    return (shower * 0.2) / temperature


def calculate_req_water(shower, temperature):
    return 1.0 / (shower * 0.8)


def calculate_min_moisture():
    min_value = None
    for temperature in temperatures:
        for shower in showers:
            value = calculate_moisture(shower, temperature)
            if min_value is None or value < min_value:
                min_value = value

    min_value -= min_value * off_percentage
    return min_value


def calculate_max_moisture():
    max_value = None
    for temperature in temperatures:
        for shower in showers:
            value = calculate_moisture(shower, temperature)
            if max_value is None or value > max_value:
                max_value = value

    max_value += max_value * off_percentage
    return max_value


def calculate_min_req_water():
    min_value = None
    for temperature in temperatures:
        for shower in showers:
            value = calculate_req_water(shower, temperature)
            if min_value is None or value < min_value:
                min_value = value

    min_value -= min_value * off_percentage
    return min_value


def calculate_max_req_water():
    max_value = None
    for temperature in temperatures:
        for shower in showers:
            value = calculate_req_water(shower, temperature)
            if max_value is None or value > max_value:
                max_value = value

    max_value += max_value * off_percentage
    return max_value


def map_range(x, pre_min, pre_max, post_min, post_max):
    ratio = float(post_max - post_min) / float(pre_max - pre_min)
    mapped = ((x - pre_min) * ratio) + post_min
    print pre_min, pre_max, ' | ', post_min, post_max, ' | ', x, ' -> ', mapped
    return mapped


def generate_data():
    min_raw_file_path = os.path.abspath('generated_data/min_raw_data.csv')
    rec_raw_file_path = os.path.abspath('generated_data/rec_raw_data.csv')

    # Create new csv files
    min_raw_file = open(min_raw_file_path, 'w')
    rec_raw_file = open(rec_raw_file_path, 'w')

    min_rows = []
    rec_rows = []

    min_writes = csv.writer(min_raw_file, delimiter=',', quoting=csv.QUOTE_NONE, lineterminator='\n')
    rec_writes = csv.writer(rec_raw_file, delimiter=',', quoting=csv.QUOTE_NONE, lineterminator='\n')

    # Add default lines
    row_count = len(crop_types) * len(ages) * len(temperatures) * len(showers)
    column_count = 5
    min_rows.append([row_count, column_count])
    min_rows.append(['TYPE', 'AGE', 'TEMPERATURE', 'SHOWER', 'MOISTURE', 'REQ_WATER'])
    rec_rows.append([row_count, column_count])
    rec_rows.append(['TYPE', 'AGE', 'TEMPERATURE', 'SHOWER', 'MOISTURE', 'REQ_WATER'])

    pre_min_moisture = calculate_min_moisture()
    pre_max_moisture = calculate_max_moisture()
    pre_min_req_water = calculate_min_req_water()
    pre_max_req_water = calculate_max_req_water()

    print 'Pre min. moisture: ', pre_min_moisture
    print 'Pre max. moisture: ', pre_max_moisture
    print 'Pre min. req. water: ', pre_min_req_water
    print 'Pre max. req. water: ', pre_max_req_water

    # Generate sample data
    for crop_type in crop_types:
        for age in ages:
            for temperature in temperatures:
                for shower in showers:
                    base_moisture = calculate_moisture(shower, temperature)
                    moisture_off = base_moisture * off_percentage
                    moisture = random.uniform(base_moisture - moisture_off, base_moisture + moisture_off)
                    moisture = map_range(moisture, pre_min_moisture, pre_max_moisture, min_moisture, max_moisture)

                    base_req_water = calculate_req_water(shower, temperature)
                    req_water_off = base_req_water * off_percentage
                    req_water = random.uniform(base_req_water - req_water_off, base_req_water + req_water_off)
                    req_water = map_range(req_water, pre_min_req_water, pre_max_req_water, min_req_water, max_req_water)

                    min_row = [crop_type, age, temperature, shower, round(moisture, 5), round(req_water * 0.7, 5)]
                    min_rows.append(min_row)
                    rec_row = [crop_type, age, temperature, shower, round(moisture, 5), round(req_water, 5)]
                    print rec_row, '_________________________________________________________________'
                    rec_rows.append(rec_row)

    # Write the data to csv file
    for min_row in min_rows:
        min_writes.writerow(min_row)
    for rec_row in rec_rows:
        rec_writes.writerow(rec_row)
