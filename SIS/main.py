import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

import data_processor

if __name__ == '__main__':
    raw_data_bunch = data_processor.load_dataset()
    raw_data_bunch.show_properties()

    data = pd.DataFrame(raw_data_bunch.data)
    data.columns = raw_data_bunch.feature_names
    print data.head()

    # Add the target values
    data['REQ_WATER'] = raw_data_bunch.target

    # Remove target value from X
    X = data.drop('REQ_WATER', axis=1)

    l_reg = LinearRegression(n_jobs=-1)

    # Train the regression model
    l_reg.fit(X, data.REQ_WATER)

    print '________________________________________________________________________'
    print pd.DataFrame(zip(X.columns, l_reg.coef_), columns=['features', 'estimatedCoefficients'])

    plt.scatter(data.TEMPERATURE, data.REQ_WATER)
    plt.xlabel('Temperature')
    plt.ylabel('Required water')
    plt.title('Relationship between temperature and required water')
    plt.show()

    mseFull = np.mean((data.REQ_WATER - l_reg.predict(X)) ** 2)
    print '________________________________________________________________________'
    print 'Mean squared distance: ', mseFull



