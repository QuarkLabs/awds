import data_processor
import pandas as pd
from sklearn.linear_model import LinearRegression


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

    Q = pd.DataFrame({'TYPE': [1.0, 1.0, 1.0], 'AGE': [1.0, 1.0, 1.0], 'TEMPERATURE': [25.0, 25.0, 25.0],
                      'SHOWER': [1.0, 2.0, 3.0], 'MOISTURE': [0.00805, 0.01595, 0.02422]})
    Q = Q[['TYPE', 'AGE', 'TEMPERATURE', 'SHOWER', 'MOISTURE']]
    print Q
    print l_reg.predict(Q)

    print ''
    print ''

    print X[:3]
    print l_reg.predict(X[:3])