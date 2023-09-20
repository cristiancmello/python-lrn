import collections
import unittest
from array import array
from collections.abc import Sequence

from kata_1.list import *


class TestList(unittest.TestCase):
    def test_can_create_container_mutable_sequence_using_list(self):
        self.assertIsInstance(list_is_container_mutable_sequence, list)
        self.assertIsInstance(list_is_container_mutable_sequence, collections.abc.Sequence)
        self.assertIsInstance(list_is_container_mutable_sequence, collections.abc.MutableSequence)

        self.assertListEqual(list_is_container_mutable_sequence, [])
        append_element_on_list(1)
        self.assertListEqual(list_is_container_mutable_sequence, [1])

    def test_ordered_lists(self):
        self.assertListEqual(an_ordered_list, ['orange', 'apple', 'grape'])

    def test_get_list_index(self):
        self.assertEqual(an_ordered_list[0], 'orange')
        self.assertEqual(an_ordered_list[1], 'apple')

    def test_list_can_be_heterogeneous(self):
        self.assertIsInstance(heterogeneous_list[0], str)
        self.assertIsInstance(heterogeneous_list[1], float)
        self.assertIsInstance(heterogeneous_list[2], tuple)
        self.assertIsInstance(heterogeneous_list[3], array.array)
        self.assertIsInstance(heterogeneous_list[4], list)
        self.assertIsInstance(heterogeneous_list[5], dict)

    def test_list_can_be_created_using_literals(self):
        self.assertListEqual(list_created_by_literals, ['banana', 'apple'])

    def test_list_as_matrix(self):
        self.assertListEqual(matrix, [[1, 2, 3], [4, 5, 6]])

    def test_creating_list_from_iterables_using_constructor(self):
        self.assertListEqual(list_created_using_empty_constructor, [])
        self.assertListEqual(list_created_using_constructor_w_tuple, [1, 2, 3])
        self.assertIn('name', list_created_using_constructor_w_dict)
        self.assertIn('birthDate', list_created_using_constructor_w_dict)
        self.assertIn(('name', 'John'), list_created_using_constructor_w_dict_items)
        self.assertIn(('city', 'New York'), list_created_using_constructor_w_dict_items)
        self.assertListEqual(list_created_using_constructor_w_string, ['a', 'b', 'c'])

    def test_retrieving_multiple_items_from_list_using_slicing(self):
        letters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd']
        self.assertListEqual(list_shallow_copy(letters), ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd'])
        self.assertListEqual(list_slicing_from_2_index_to_end(letters), ['B', 'b', 'C', 'c', 'D', 'd'])
        self.assertListEqual(list_slicing_uppercase_letters(letters), ['A', 'B', 'C', 'D'])
        self.assertListEqual(list_slicing_lowercase_letters(letters), ['a', 'b', 'c', 'd'])
        self.assertListEqual(list_slicing_first_three_letters(letters), ['A', 'a', 'B'])
        self.assertListEqual(list_slicing_last_letter(letters), ['d'])
        self.assertListEqual(list_slicing_last_three_lowercase_letters(letters), ['b', 'c', 'd'])
        self.assertListEqual(list_slicing_medium_uppercase_letters(letters), ['B', 'C'])
        self.assertListEqual(list_slicing_reverse_all_letters(letters), ['d', 'D', 'c', 'C', 'b', 'B', 'a', 'A'])
        self.assertListEqual(list_slicing_uppercase_using_slice_constructor(letters), ['A', 'B', 'C', 'D'])

    def test_creating_codelist_using_listcomps(self):
        symbols = '$¢£¥€¤'
        self.assertListEqual(generate_code_list_using_forloop(symbols), [36, 162, 163, 165, 8364, 164])
        self.assertListEqual(generate_code_list_using_listcomps(symbols), [36, 162, 163, 165, 8364, 164])

    def test_creating_codelist_using_listcomps_with_localscopevar_walrusop(self):
        self.assertEqual(generate_code_list_using_listcomps_without_walrusop('ABC'), [65, 66, 67])
        last = 67
        self.assertEqual(generate_code_list_using_listcomps_walrusop('ABC'), (last, [65, 66, 67]))

    def test_listcomps_vs_lambda_mapfilter_beyond_ascii(self):
        self.assertEqual(beyond_ascii_listcomps('$¢£¥€¤'), [162, 163, 165, 8364, 164])
        self.assertEqual(beyond_ascii_mapfilter('$¢£¥€¤'), [162, 163, 165, 8364, 164])

    def test_cartesian_product(self):
        colors = ['black', 'white']
        sizes = ['S', 'M', 'L']
        tshirts = [
            ('black', 'S'),
            ('black', 'M'),
            ('black', 'L'),
            ('white', 'S'),
            ('white', 'M'),
            ('white', 'L')
        ]
        self.assertListEqual(cartesian_product_tshirts(colors, sizes), tshirts)
        self.assertListEqual(cartesian_product_tshirts_nestedloop(colors, sizes), tshirts)

        l1 = [10, 20, 30]
        l2 = [2, 4, 6]
        l1_product_l2 = [20, 40, 60, 40, 80, 120, 60, 120, 180]

        self.assertListEqual(cartesian_product(l1, l2), l1_product_l2)

    def test_get_codes_from_symbols_more_eff_using_genexp(self):
        symbols = '$¢£¥€¤'
        self.assertListEqual(generate_codes_using_genexp(symbols), [36, 162, 163, 165, 8364, 164])

