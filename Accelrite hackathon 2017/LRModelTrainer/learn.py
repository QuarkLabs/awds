import data_processor
import pandas as pd
from sklearn.linear_model import LinearRegression

import utils


def train_model():
    min_raw_data_bunch = data_processor.load_min_dataset()
    min_raw_data_bunch.show_properties()
    rec_raw_data_bunch = data_processor.load_rec_dataset()
    rec_raw_data_bunch.show_properties()

    min_data_pd = pd.DataFrame(min_raw_data_bunch.data)
    min_data_pd.columns = min_raw_data_bunch.feature_names
    print min_data_pd.head()
    rec_data_pd = pd.DataFrame(rec_raw_data_bunch.data)
    rec_data_pd.columns = rec_raw_data_bunch.feature_names
    print rec_data_pd.head()

    # Add the target values
    min_data_pd['REQ_WATER'] = min_raw_data_bunch.target
    rec_data_pd['REQ_WATER'] = rec_raw_data_bunch.target

    # Remove target value from X
    min_X = min_data_pd.drop('REQ_WATER', axis=1)
    rec_X = rec_data_pd.drop('REQ_WATER', axis=1)

    min_l_reg = LinearRegression(n_jobs=-1)
    rec_l_reg = LinearRegression(n_jobs=-1)

    # Train the regression model
    min_l_reg.fit(min_X, min_data_pd.REQ_WATER)
    rec_l_reg.fit(rec_X, rec_data_pd.REQ_WATER)

    # Serialize the trained objects
    utils.serialize(min_data_pd, 'min_data_pd')
    utils.serialize(min_l_reg, 'min_l_reg')
    utils.serialize(min_X, 'min_X')
    utils.serialize(rec_data_pd, 'rec_data_pd')
    utils.serialize(rec_l_reg, 'rec_l_reg')
    utils.serialize(rec_X, 'rec_X')