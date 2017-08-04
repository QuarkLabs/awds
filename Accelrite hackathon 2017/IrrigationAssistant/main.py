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


if __name__ == '__main__':
    # Copy the generated data and model from LRModelTrainer
    file_handler.update_files()

    # print calculate_req_water(1, 1, 25, 1, 5)
    # print calculate_req_water(2, 1, 25, 1, 5)
    print calculate_req_water(1, 1, 25, 4, 4)
    print calculate_req_water(1, 1, 25, 4, 5)
    print calculate_req_water(1, 1, 25, 4, 6)
    print calculate_req_water(1, 1, 25, 4, 7)
    print calculate_req_water(1, 1, 25, 4, 8)
    print calculate_req_water(1, 1, 25, 4, 9)
    print calculate_req_water(1, 1, 25, 4, 10)