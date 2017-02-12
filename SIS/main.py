# a - Current moisture level of the soil
# b - Environmental temperature
# c - Atmospheric humidity
# d - Amount of water poured (flow rate x duration)

# p - Type of the plant
# q - Age of the plant

# y - Final moisture

import numpy as np
import pandas as pd
import sklearn

from data_processor import load_dataset

raw_data_bunch = load_dataset()

bos = pd.DataFrame(raw_data_bunch.data)
bos.columns = raw_data_bunch.feature_names
print bos.head()