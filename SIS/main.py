import numpy as np
import pandas as pd
import sklearn
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

from data_processor import load_dataset
from utils import show_bunch_properties


if __name__ == '__main__':
    raw_data_bunch = load_dataset()

    show_bunch_properties(raw_data_bunch)



    # Converting raw data to pandas data frame
    data = pd.DataFrame(raw_data_bunch.data)
    data.columns = raw_data_bunch.feature_names
    print data.head()

    print '________________________________________________________________________'

    # Add the target values
    data['WATER'] = raw_data_bunch.target

    # Remove target value from X
    X = data.drop('WATER', axis=1)

    l_reg = LinearRegression(n_jobs=-1)

    l_reg.fit(X, data.WATER)

    print 'Estimated intercept coefficient:', l_reg.intercept_
    print 'Number of coefficients:', len(l_reg.coef_)

    print '________________________________________________________________________'

    print pd.DataFrame(zip(X.columns, l_reg.coef_), columns=['features', 'estimatedCoefficients'])

    plt.scatter(data.CMOIST, data.WATER)
    plt.xlabel('Current moisture')
    plt.ylabel('Required water')
    plt.title('Relationship between current moisture and required water')
    plt.show()

    print '________________________________________________________________________'

    mseFull = np.mean((data.WATER - l_reg.predict(X)) ** 2)
    print mseFull




