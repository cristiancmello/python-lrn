import os.path

lax_coordinates = (33.9425, -118.408056)

tokyo_data_tuple_as_record = ('Tokyo', 2003, 32_450, 0.66, 8014)


def generate_sorted_country_passports_using_formmating_op(passports):
    passport_str = ''
    for passport in sorted(passports):
        passport_str += '%s/%s\n' % passport
    return passport_str


def generate_sorted_countries_using_listcomp_dummyvar(passports):
    return [country for country, _ in sorted(passports)]


def generate_sorted_countries_using_forloop_dummyvar(passports):
    countries = []

    for country, _ in sorted(passports):
        countries.append(country)

    return countries


def verify_tuples_are_equals(t1, t2):
    return t1 == t2


def verify_tuples_are_equals_after_insert_mutable_obj(a, b):
    b[2].append(99)
    return a == b


def fixed(t: tuple):
    try:
        hash(t)
    except TypeError:
        return False
    return True


def create_tuple_using_constructor(t):
    return tuple(t)


def create_list_using_constructor(l):
    return list(l)


def appending_element_in_tuple(t, e):
    _l = list(t)
    _l.append(e)
    return tuple(_l)


def concats(t1: tuple, t2: tuple) -> tuple:
    return t1 + t2


def has_element(t: tuple, e: any) -> bool:
    return e in t


def count_elements(t: tuple, e: any) -> int:
    return t.count(e)


def get_value_from_tuple(t: tuple, p: int) -> any:
    return t[p]


def get_first_occurr(t: tuple, e: any) -> int:
    return t.index(e)


def get_tuple_length(t: tuple) -> int:
    return len(t)


def repeat_concat(t: tuple) -> tuple:
    return t * 2


def reversed_repeated_concat(t: tuple) -> tuple:
    return 2 * t


def get_coord_unpacking_tuple(coord: tuple[float, float], attr: str) -> float:
    if attr == 'lat':
        lat, _ = coord
        return lat
    elif attr == 'long':
        _, long = coord
        return long


def powerful_swap_using_unpack(coord: tuple[float, float]) -> tuple[float, float]:
    lat, long = coord
    long, lat = lat, long
    return lat, long


def unpacking_tuple_as_arg_for_divmod(args: tuple[float, float]) -> tuple[float, float]:
    return divmod(*args)


def get_basename_using_unpacking_ospathsplit(filename: str) -> str:
    basename, _ = os.path.split(filename)
    return basename


def grab_excess_items(t: tuple):
    a, b, *tail = t
    return a, b, tail


def grab_excess_items_medium_pos(t: tuple):
    a, *medium, c, d = t
    return a, medium, c, d


def grab_excess_items_header_pos(t: tuple):
    *header, b, c, d = t
    return header, b, c, d


def generate_codes_using_genexp(symbols: str) -> tuple[int]:
    return tuple(ord(s) for s in symbols)