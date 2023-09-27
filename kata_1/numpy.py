import numpy as np
from numpy import ndarray

ndarray_from_arange = np.arange(12)
str_from_type_of_ndarray_from_arange = str(type(ndarray_from_arange))

total_of_elems, = ndarray_from_arange.shape
total_of_elems_extracted_from_shape_from_12element_arange = total_of_elems
dimensions_of_12element_arange_from_lenshape = len(ndarray_from_arange.shape)


def add_dim(a_ndarray: ndarray):
    a_ndarray.shape = (3, 4)


def get_row_2_from_ndarray(a: ndarray):
    return a[2]


def get_elem_from_row2_index1(a: ndarray):
    return a[2, 1]


def get_column2_from_ndarray(a: ndarray):
    return a[:, 2]


def transpose_ndarray(a: ndarray):
    return a.transpose()

