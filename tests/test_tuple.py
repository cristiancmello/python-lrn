import unittest

from kata_1.tuple import *


class TestTuple(unittest.TestCase):
    def test_can_create_tuple_unpacking(self):
        lat, long = lax_coordinates
        self.assertEqual(lat, 33.9425)
        self.assertEqual(long, -118.408056)

        city, year, pop, chg, area = tokyo_data_tuple_as_record

        self.assertEqual(city, 'Tokyo')
        self.assertEqual(year, 2003)
        self.assertEqual(pop, 32_450)
        self.assertEqual(chg, 0.66)
        self.assertEqual(area, 8014)

    def test_iterating_over_list_of_tuples(self):
        traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
        strseq_country_passports = """BRA/CE342567
ESP/XDA205856
USA/31195855
"""
        sorted_countries = ['BRA', 'ESP', 'USA']

        self.assertEqual(generate_sorted_country_passports_using_formmating_op(traveler_ids), strseq_country_passports)
        self.assertListEqual(generate_sorted_countries_using_listcomp_dummyvar(traveler_ids), sorted_countries)
        self.assertListEqual(generate_sorted_countries_using_forloop_dummyvar(traveler_ids), sorted_countries)

    def test_tuple_containing_mutable_object(self):
        a = (10, 'alpha', [1, 2])
        b = (10, 'alpha', [1, 2])
        self.assertTrue(verify_tuples_are_equals(a, b))
        self.assertFalse(verify_tuples_are_equals_after_insert_mutable_obj(a, b))
        self.assertTupleEqual(b, (10, 'alpha', [1, 2, 99]))

        # tuples with mutable items can be source of bugs!

    def test_verifying_tuple_is_has_fixed_value(self):
        tuple_fixed = (10, 'alpha', (1, 2))
        tuple_mutable = (10, 'alpha', [1, 2])
        self.assertTrue(fixed(tuple_fixed))
        self.assertFalse(fixed(tuple_mutable))

    def test_showing_tuple_is_more_efficient_than_list(self):
        a = (1, 2)
        b = create_tuple_using_constructor(a)

        c = [1, 2]
        d = create_list_using_constructor(c)

        self.assertEqual(id(a), id(b))
        self.assertNotEqual(id(c), id(d))

    def test_showing_tuple_has_fixed_length(self):
        a = (1, 2)
        new_element = 3
        self.assertTupleEqual(appending_element_in_tuple(a, new_element), (1, 2, 3))

    def test_tuple_operations(self):
        a = (1, 2)
        b = (3, 4)
        self.assertTupleEqual(concats(a, b), (1, 2, 3, 4))

        element = 99
        self.assertFalse(has_element(a, element))

        c = (1, 2, 1, 3)
        self.assertEqual(count_elements(c, 1), 2)

        position = 2
        self.assertEqual(get_value_from_tuple(c, position), 1)

        position_of_first_occurrence_of_element = 3
        element = 3
        self.assertEqual(get_first_occurr(c, element), position_of_first_occurrence_of_element)

        length_of_tuple = 4
        self.assertEqual(get_tuple_length(c), length_of_tuple)

        repeated_concat = (1, 2, 1, 3, 1, 2, 1, 3)
        self.assertTupleEqual(repeat_concat(c), repeated_concat)

        b = (99, 88)
        self.assertTupleEqual(reversed_repeated_concat(b), (99, 88, 99, 88))

    def test_unpacking_tuples(self):
        coords = (33.9425, -118.408056)
        self.assertEqual(get_coord_unpacking_tuple(coords, 'lat'), 33.9425)
        self.assertEqual(get_coord_unpacking_tuple(coords, 'long'), -118.408056)

        swapped_coords = (-118.408056, 33.9425)
        self.assertEqual(powerful_swap_using_unpack(coords), swapped_coords)

        # divmod(20, 8) <=> 20 / 8 = 2 remaind 4 => (2, 4)
        self.assertTupleEqual(unpacking_tuple_as_arg_for_divmod((20, 8)), (2, 4))

        filename = './test_tuple.py'
        current_dir = '.'
        self.assertEqual(current_dir, get_basename_using_unpacking_ospathsplit(filename))

    def test_getting_excess_argument_head_tail(self):
        t = tuple(range(5))
        self.assertTupleEqual(grab_excess_items(t), (0, 1, [2, 3, 4]))

        t = tuple(range(3))
        self.assertTupleEqual(grab_excess_items(t), (0, 1, [2]))

        t = tuple(range(2))
        self.assertTupleEqual(grab_excess_items(t), (0, 1, []))

        t = tuple(range(5))
        self.assertTupleEqual(grab_excess_items_medium_pos(t), (0, [1, 2], 3, 4))
        self.assertTupleEqual(grab_excess_items_header_pos(t), ([0, 1], 2, 3, 4))

    def test_get_codes_from_symbols_more_eff_using_genexp(self):
        symbols = '$¢£¥€¤'
        self.assertTupleEqual(generate_codes_using_genexp(symbols), (36, 162, 163, 165, 8364, 164))
