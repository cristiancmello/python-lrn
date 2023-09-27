import unittest

from numpy.testing import *

from kata_1.numpy import *


class TestNumpy(unittest.TestCase):
    def test_basic_operations(self):
        ndarray_expected = np.array(range(12))

        assert_equal(ndarray_expected, ndarray_from_arange)
        assert_equal("<class 'numpy.ndarray'>", str_from_type_of_ndarray_from_arange)
        assert_equal(12, total_of_elems_extracted_from_shape_from_12element_arange)
        assert_equal(1, dimensions_of_12element_arange_from_lenshape)

    def test_reshape_adding_dimensions_w_ndarray(self):
        a_ndarray = np.arange(12)
        expected_dimensions = 2
        expected_dim_0 = 3  # rows
        expected_dim_1 = 4  # columns
        ndarray_expected = np.array([
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [8, 9, 10, 11]
        ])

        ndarray_transposed_expected = np.array([
            [0, 4, 8],
            [1, 5, 9],
            [2, 6, 10],
            [3, 7, 11]
        ])

        add_dim(a_ndarray)
        assert_equal(expected_dimensions, len(a_ndarray.shape))

        dim_0, dim_1 = a_ndarray.shape
        assert_equal(expected_dim_0, dim_0)
        assert_equal(expected_dim_1, dim_1)
        assert_equal(ndarray_expected, a_ndarray)

        assert_equal(np.array([8, 9, 10, 11]), get_row_2_from_ndarray(a_ndarray))
        assert_equal(9, get_elem_from_row2_index1(a_ndarray))
        assert_equal(np.array([2, 6, 10]), get_column2_from_ndarray(a_ndarray))
        assert_equal(ndarray_transposed_expected, transpose_ndarray(a_ndarray))
