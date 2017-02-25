from os.path import dirname
from os.path import join
from os.path import abspath
from distutils.dir_util import copy_tree
from distutils.dir_util import remove_tree


def update_files():
    parent_path = dirname(dirname(__file__))

    from_generated_data = join(parent_path, 'LRModelTrainer', 'generated_data')
    to_generated_data = abspath('generated_data')
    remove_tree(to_generated_data)
    copy_tree(from_generated_data, to_generated_data)

    from_pickle_data = join(parent_path, 'LRModelTrainer', 'pickle_data')
    to_pickle_data = abspath('pickle_data')
    remove_tree(to_pickle_data)
    copy_tree(from_pickle_data, to_pickle_data)
