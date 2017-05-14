import pandas as pd
import MySQLdb
from datetime import datetime
import pyowm
from dateutil.relativedelta import relativedelta

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
    age = get_age(type)
    temperature = get_temperature()
    shower = get_shower()

    water_volume = calculate_req_water(type, age, temperature, shower, moisture)

    update_crop_condition(type, temperature, shower, moisture, water_volume)
    return water_volume[1]     # Return only recommended water amount


def get_age(type):
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="sis")
    cur = db.cursor()

    cur.execute("SELECT start_date FROM farmer_has_crop WHERE crop_id = " + str(type))

    start_date = cur.fetchall()[0][0]
    end_date = datetime.now()
    difference_in_years = relativedelta(end_date, start_date).years
    db.close()

    return difference_in_years


def get_temperature():
    owm = pyowm.OWM('762538bb02614c55a70704b5976c9065')
    observation = owm.weather_at_place('London,uk')
    w = observation.get_weather()
    temperature = w.get_temperature('celsius')['temp']
    return temperature


def get_shower():
    owm = pyowm.OWM('762538bb02614c55a70704b5976c9065')
    observation = owm.weather_at_place('London,uk')
    w = observation.get_weather()
    rain = w.get_rain()
    if rain == {}:
        rain = 0
    return rain


def update_crop_condition(type, temperature, shower, moisture, water_volume):
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="sis")
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




