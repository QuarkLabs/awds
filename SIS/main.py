import pandas as pd

import utils


def calculate_req_water(type, age, temperature, shower, moisture):
    data_pd = utils.deserialize('data_pd')
    l_reg = utils.deserialize('l_reg')

    X = pd.DataFrame({'TYPE': type, 'AGE': age, 'TEMPERATURE': temperature, 'SHOWER': shower, 'MOISTURE': moisture}, index=[0])
    return l_reg.predict(X)


if __name__ == '__main__':
    print calculate_req_water(1, 1, 25, 1, 0.01612)
    # 1,1,25,1,0.01612,0.00064

    print calculate_req_water(1, 1, 25, 2, 0.03172)
    # 1,1,25,2,0.03172,0.00126

    print calculate_req_water(1, 1, 25, 3, 0.04795)
    # 1,1,25,3,0.04795,0.00194
