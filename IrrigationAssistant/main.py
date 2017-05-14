import pandas as pd
import MySQLdb
from datetime import datetime

import file_handler
from utils import deserialize


def calculate_req_water(type, age, temperature, shower, moisture):
    min_l_reg = deserialize('min_l_reg')
    rec_l_reg = deserialize('rec_l_reg')

    X = pd.DataFrame({'TYPE': type, 'AGE': age, 'TEMPERATURE': temperature, 'SHOWER': shower, 'MOISTURE': moisture},
                     index=[0])
    X = X[['TYPE', 'AGE', 'TEMPERATURE', 'SHOWER', 'MOISTURE']]

    min_prediction = min_l_reg.predict(X)[0]
    rec_prediction = rec_l_reg.predict(X)[0]

    # return [min_prediction, rec_prediction]
    return [min_prediction, rec_prediction]


def get_water(type, moisture):
    age = get_age()
    temperature = get_temperature()
    shower = get_shower()

    water_volume = calculate_req_water(type, age, temperature, shower, moisture)

    update_crop_condition(type, temperature, shower, moisture, water_volume)
    return water_volume[1]     # Return only recommended water amount


def get_age():
    return 1


def get_temperature():
    return 25


def get_shower():
    return 3


def update_crop_condition(type, temperature, shower, moisture, water_volume):
    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         passwd="",  # your password
                         db="sis")  # name of the data base

    cur = db.cursor()
    sql = "INSERT INTO crop_condition(farmer_has_crop_crop_id, temperature, shower, moisture, min_water, rec_water, calculated_date) " \
            "VALUES(" \
            + str(type) + ", " \
            + str(temperature) + ", " \
            + str(shower) + ", " \
            + str(moisture) + ", " \
            + str(water_volume[0]) + ", " \
            + str(water_volume[1]) + ", '" \
            + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "')"
    try:
        cur.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


if __name__ == '__main__':
    # Copy the generated data and model from LRModelTrainer
    file_handler.update_files()

    # print calculate_req_water(1, 1, 25, 4, 4)
    # print calculate_req_water(1, 1, 25, 4, 5)
    # print calculate_req_water(1, 1, 25, 4, 6)
    # print calculate_req_water(1, 1, 25, 4, 7)
    # print calculate_req_water(1, 1, 25, 4, 8)
    # print calculate_req_water(1, 1, 25, 4, 9)
    # print calculate_req_water(1, 1, 25, 4, 10)

    print get_water(1, 5)
    print get_water(1, 10)




