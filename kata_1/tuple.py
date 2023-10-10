import os.path

lax_coordinates = (33.9425, -118.408056)

tokyo_data_tuple_as_record = ('Tokyo', 2003, 32_450, 0.66, 8014)


def generate_sorted_country_passports_using_formmating_op(passports: list[tuple]):
    strseq = str()
    for passport in sorted(passports):
        strseq += '%s/%s\n' % passport
    return strseq


def generate_sorted_countries_using_listcomp_dummyvar(passports: list[tuple]):
    return [country for country, _ in sorted(passports)]


def generate_sorted_countries_using_forloop_dummyvar(passports: list[tuple]):
    countries = []
    for country, _ in sorted(passports):
        countries.append(country)
    return countries


def verify_tuples_are_equals(t1: tuple, t2: tuple):
    return t1 == t2


def verify_tuples_are_equals_after_insert_mutable_obj(t1: tuple, t2: tuple):
    t2[2].append(99)
    return t1 == t2


def fixed(o):
    try:
        hash(o)
        return True
    except TypeError:
        return False


def create_tuple_using_constructor(t: tuple):
    return tuple(t)


def create_list_using_constructor(l: list):
    return list(l)


def appending_element_in_tuple(t: tuple, e):
    l = list(t)
    l.append(e)
    return tuple(l)


def concats(t1: tuple, t2: tuple):
    return t1 + t2


def has_element(t: tuple, e):
    return e in t


def count_elements(t: tuple, e):
    return t.count(e)


def get_value_from_tuple(t: tuple, pos: int):
    return t[pos]


def get_first_occurr(t: tuple, e):
    return t.index(e)


def get_tuple_length(t: tuple):
    return len(t)


def repeat_concat(t: tuple):
    return t * 2


def reversed_repeated_concat(t: tuple):
    return 2 * t


def get_coord_unpacking_tuple(coords: tuple[float, float], attr: str):
    lat, _ = coords
    _, long = coords

    d = {'lat': lat, 'long': long}

    return d[attr]


def powerful_swap_using_unpack(coords: tuple[float, float]):
    lat, long = coords
    long, lat = lat, long
    return lat, long


def unpacking_tuple_as_arg_for_divmod(args: tuple[float, float]):
    return divmod(*args)


def get_basename_using_unpacking_ospathsplit(filename: str) -> str:
    # alternative: basename, _ = os.path.split(filename)
    return [basename for basename in os.path.split(filename)][0]


def get_tuple_comma_termination():
    return 1,


def grab_excess_items(t: tuple):
    a, b, *tail = t
    return a, b, tail


def grab_excess_items_medium_pos(t: tuple):
    a, *medium, c, d = t
    return a, medium, c, d


def grab_excess_items_header_pos(t: tuple):
    *header, b, c, d = t
    return header, b, c, d


def generate_codes_using_genexp(symbols: str):
    return tuple(ord(s) for s in symbols)

