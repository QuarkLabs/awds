import pandas as pd

import file_handler
from utils import deserialize


def calculate_req_water(type, age, temperature, shower, moisture):
    min_l_reg = deserialize('min_l_reg')
    rec_l_reg = deserialize('rec_l_reg')

    X = pd.DataFrame({'TYPE': type, 'AGE': age, 'TEMPERATURE': temperature, 'SHOWER': shower, 'MOISTURE': moisture}, index=[0])
    X = X[['TYPE', 'AGE', 'TEMPERATURE', 'SHOWER', 'MOISTURE']]

    return [min_l_reg.predict(X)[0], rec_l_reg.predict(X)[0]]


if __name__ == '__main__':
    # Copy the generated data and model from LRModelTrainer
    file_handler.update_files()

    print calculate_req_water(1, 1, 25, 1, 0.56241)
    print calculate_req_water(1, 1, 25, 2, 3.63963)
    print calculate_req_water(1, 1, 25, 3, 6.76412)