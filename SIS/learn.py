import data_processor
import pandas as pd
from sklearn.linear_model import LinearRegression

import utils

raw_data_bunch = data_processor.load_dataset()
raw_data_bunch.show_properties()

data_pd = pd.DataFrame(raw_data_bunch.data)
data_pd.columns = raw_data_bunch.feature_names
print data_pd.head()

# Add the target values
data_pd['REQ_WATER'] = raw_data_bunch.target

# Remove target value from X
X = data_pd.drop('REQ_WATER', axis=1)

l_reg = LinearRegression(n_jobs=-1)

# Train the regression model
l_reg.fit(X, data_pd.REQ_WATER)

# Serialize the trained objects
utils.serialize(data_pd, 'data_pd')
utils.serialize(l_reg, 'l_reg')
utils.serialize(X, 'X')