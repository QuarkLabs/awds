import pandas as pd

import utils


def calculate_req_water(type, age, temperature, shower, moisture):
    l_reg = utils.deserialize('l_reg')
    X = pd.DataFrame({'TYPE': type, 'AGE': age, 'TEMPERATURE': temperature, 'SHOWER': shower, 'MOISTURE': moisture}, index=[0])
    return l_reg.predict(X)


if __name__ == '__main__':
    print calculate_req_water(1, 1, 25, 1, 0.00805)
    print calculate_req_water(1, 1, 25, 2, 0.01595)
    print calculate_req_water(1, 1, 25, 3, 0.02422)
