import os
from cPickle import dump
from cPickle import load


def serialize(obj, name):
    pickle_file_path = os.path.abspath('pickle_data/' + name + '.p')
    pickle_file = open(pickle_file_path, 'wb')

    # Save the object to pickle file
    dump(obj, pickle_file)


def deserialize(name):
    pickle_file_path = os.path.abspath('pickle_data/' + name + '.p')
    pickle_file = open(pickle_file_path, 'rb')

    # Load the pickle file
    obj = load(pickle_file)
    pickle_file.close()

    return obj
