import data_processor
import pandas as pd
from sklearn.linear_model import LinearRegression

import utils


def calculate_req_water(type, age, temperature, shower, moisture):
    raw_data_bunch = data_processor.load_dataset()
    raw_data_bunch.show_properties()

    data_pd = pd.DataFrame(raw_data_bunch.data)
    data_pd.columns = raw_data_bunch.feature_names
    # print data_pd.head()

    # Add the target values
    data_pd['REQ_WATER'] = raw_data_bunch.target

    # Remove target value from X
    X = data_pd.drop('REQ_WATER', axis=1)

    l_reg = LinearRegression(n_jobs=-1)

    # Train the regression model
    l_reg.fit(X, data_pd.REQ_WATER)

    X = pd.DataFrame({'TYPE': type, 'AGE': age, 'TEMPERATURE': temperature, 'SHOWER': shower, 'MOISTURE': moisture},
                     index=[0])
    return l_reg.predict(X)


# if __name__ == '__main__':
#     print calculate_req_water(1, 1, 25, 1, 0.00805)
#     print calculate_req_water(1, 1, 25, 2, 0.01595)
#     print calculate_req_water(1, 1, 25, 3, 0.02422)

if __name__ == '__main__':
    raw_data_bunch = data_processor.load_dataset()
    # raw_data_bunch.show_properties()

    data_pd = pd.DataFrame(raw_data_bunch.data)
    data_pd.columns = raw_data_bunch.feature_names
    # print data_pd.head()

    # Add the target values
    data_pd['REQ_WATER'] = raw_data_bunch.target

    # Remove target value from X
    X = data_pd.drop('REQ_WATER', axis=1)

    l_reg = LinearRegression()

    # Train the regression model
    l_reg.fit(X, data_pd.REQ_WATER)

    Q = pd.DataFrame({'TYPE': [1, 1, 1], 'AGE': [1, 1, 1], 'TEMPERATURE': [25, 25, 25],
                      'SHOWER': [1, 2, 3], 'MOISTURE': [0.00805, 0.01595, 0.02422]})

    print l_reg.predict(Q)