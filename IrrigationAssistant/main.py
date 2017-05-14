import pandas as pd

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
    return [int(min_prediction), int(rec_prediction)]


def get_water(type, moisture):
    condition = update_crop_condition(type, moisture)
    water_volume = calculate_req_water(condition[0], condition[1], condition[2], condition[3], condition[4])
    update_water_volume(water_volume)
    return water_volume[1]     # Return only recommended water amount


def update_crop_condition(type, moisture):
    # Insert moisture to database
    return [type, 2, 25, 4, moisture]   # type, age, temperature, shower, moisture


def update_water_volume(water_volume):
    pass


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




