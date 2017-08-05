import csv
from os.path import dirname
from os.path import join

import numpy as np


class Bunch(dict):
    def __init__(self, **kwargs):
        dict.__init__(self, kwargs)

    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setstate__(self, state):
        pass

    def show_properties(self):
        print ''
        print 'Bunch properties________________________________________________'
        print self.keys()
        print self.data.shape
        print self.feature_names
        # print bunch.DESCR
        print ''


def load_min_dataset():
    module_path = dirname(__file__)

    fdescr_name = join(module_path, 'generated_data', 'min_raw_data.csv')
    with open(fdescr_name) as f:
        descr_text = f.read()

    data_file_name = join(module_path, 'generated_data', 'min_raw_data.csv')
    with open(data_file_name) as f:
        data_file = csv.reader(f)
        temp = next(data_file)
        n_samples = int(temp[0])
        n_features = int(temp[1])
        data = np.empty((n_samples, n_features))
        target = np.empty((n_samples,))
        temp = next(data_file)
        feature_names = np.array(temp)

        for i, d in enumerate(data_file):
            data[i] = np.asarray(d[:-1], dtype=np.float)
            target[i] = np.asarray(d[-1], dtype=np.float)

    return Bunch(data=data,
                 target=target,
                 feature_names=feature_names[:-1],
                 DESCR=descr_text)


def load_rec_dataset():
    module_path = dirname(__file__)

    fdescr_name = join(module_path, 'generated_data', 'rec_raw_data.csv')
    with open(fdescr_name) as f:
        descr_text = f.read()

    data_file_name = join(module_path, 'generated_data', 'rec_raw_data.csv')
    with open(data_file_name) as f:
        data_file = csv.reader(f)
        temp = next(data_file)
        n_samples = int(temp[0])
        n_features = int(temp[1])
        data = np.empty((n_samples, n_features))
        target = np.empty((n_samples,))
        temp = next(data_file)
        feature_names = np.array(temp)

        for i, d in enumerate(data_file):
            data[i] = np.asarray(d[:-1], dtype=np.float)
            target[i] = np.asarray(d[-1], dtype=np.float)

    return Bunch(data=data,
                 target=target,
                 feature_names=feature_names[:-1],
                 DESCR=descr_text)
