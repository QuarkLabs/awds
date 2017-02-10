# a - Current moisture level of the soil
# b - Environmental temperature
# c - Atmospheric humidity
# d - Amount of water poured (flow rate x duration)

# p - Type of the plant
# q - Age of the plant

# y - Final moisture

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn

from sklearn.datasets import load_boston

boston = load_boston()

# print boston.keys()
# print boston.data.shape
# print boston.feature_names
# print boston.DESCR

bos = pd.DataFrame(boston.data)
bos.columns = boston.feature_names
print bos.head()

bos['PRICE'] = boston.target

from sklearn.linear_model import LinearRegression
X = bos.drop('PRICE', axis=1)

lm = LinearRegression()

lm.fit(X, bos.PRICE)

LinearRegression(copy_X=True, fit_intercept=True, normalize=False)

print 'Estimated intercept coefficient:', lm.intercept_
print 'Number of coefficients:', len(lm.coef_)

print pd.DataFrame(zip(X.columns, lm.coef_), columns=['features', 'estimatedCoefficients'])

plt.scatter(bos.RM, bos.PRICE)
plt.xlabel('Average number of rooms per dwelling (RM)')
plt.ylabel('Housing price')
plt.title('Relationship between RM and Price')
plt.show()