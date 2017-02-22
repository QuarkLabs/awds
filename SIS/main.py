import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import utils

if __name__ == '__main__':
    data_pd = utils.deserialize('data_pd')
    l_reg = utils.deserialize('l_reg')
    X = utils.deserialize('X')

    print '________________________________________________________________________'
    print pd.DataFrame(zip(X.columns, l_reg.coef_), columns=['features', 'estimatedCoefficients'])

    # plt.scatter(data_pd.TEMPERATURE, data_pd.REQ_WATER)
    # plt.xlabel('Temperature')
    # plt.ylabel('Required water')
    # plt.title('Relationship between temperature and required water')
    # plt.show()

    plt.scatter(data_pd.REQ_WATER, l_reg.predict(X))
    plt.xlabel('Required water')
    plt.ylabel('Predicted water')
    plt.title('Relationship between required water and predicted water')
    plt.show()

    mseFull = np.mean((data_pd.REQ_WATER - l_reg.predict(X)) ** 2)
    print '________________________________________________________________________'
    print 'Mean squared distance: ', mseFull