import os.path

lax_coordinates = (33.9425, -118.408056)

tokyo_data_tuple_as_record = ('Tokyo', 2003, 32_450, 0.66, 8014)


def generate_sorted_country_passports_using_formmating_op(traveler_ids):
    str_country_passports = ""

    for passport in sorted(traveler_ids):
        str_country_passports += '%s/%s\n' % passport

    return str_country_passports


def generate_sorted_countries_using_listcomp_dummyvar(traveler_ids):
    # _ : called dummy variable
    return list(country for country, _ in sorted(traveler_ids))


def generate_sorted_countries_using_forloop_dummyvar(traveler_ids):
    sorted_countries = []

    for country, _ in sorted(traveler_ids):
        sorted_countries.append(country)

    return sorted_countries


def verify_tuples_are_equals(a, b):
    return a == b


def verify_tuples_are_equals_after_insert_mutable_obj(a, b):
    b[-1].append(99)
    return a == b


def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True


def create_tuple_using_constructor(t):
    return tuple(t)


def create_list_using_constructor(l):
    return list(l)


def appending_element_in_tuple(t, element):
    l_ = list(t)
    l_.append(element)
    return tuple(l_)


def concats(t1, t2):
    return t1 + t2


def has_element(t, e):
    return e in t


def count_elements(t: tuple, e):
    return t.count(e)


def get_value_from_tuple(t, p):
    return t[p]


def get_first_occurr(t: tuple, e):
    return t.index(e)


def get_tuple_length(t: tuple):
    return len(t)


def repeat_concat(t):
    return t * 2


def reversed_repeated_concat(t):
    return 2 * t


def get_coord_unpacking_tuple(t, coord):
    if coord == 'lat':
        lat, _ = t
        return lat
    elif coord == 'long':
        _, long = t
        return long


def powerful_swap_using_unpack(t):
    lat, long = t
    long, lat = lat, long

    return lat, long


def unpacking_tuple_as_arg_for_divmod(t: tuple) -> tuple:
    return divmod(*t)


def get_basename_using_unpacking_ospathsplit(file):
    basename, _ = os.path.split(file)
    return basename


def grab_excess_items(t: tuple):
    a, b, *rest = t
    return a, b, rest


def grab_excess_items_medium_pos(t: tuple):
    a, *body, c, d = t
    return a, body, c, d


def grab_excess_items_header_pos(t: tuple):
    *header, b, c, d = t
    return header, b, c, d


def generate_codes_using_genexp(symbols):
    return tuple(ord(c) for c in symbols)
