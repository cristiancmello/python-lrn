import array

list_is_container_mutable_sequence = []

an_ordered_list = ['orange', 'apple', 'grape']

heterogeneous_list = [
    'string',
    2.09,
    (1, 2),
    array.array('d', [1, 2]),
    [3, 4],
    {'name': 'John'}
]

list_created_by_literals = ['banana', 'apple']

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

list_created_using_empty_constructor = list()

list_created_using_constructor_w_tuple = list((1, 2, 3))

list_created_using_constructor_w_dict = list({'name', 'birthDate'})

list_created_using_constructor_w_dict_items = list({'city': 'New York', 'name': 'John'}.items())

list_created_using_constructor_w_string = list('abc')


def append_element_on_list(element):
    list_is_container_mutable_sequence.append(element)


def generate_code_list_using_forloop(symbols):
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))

    return codes


def generate_code_list_using_listcomps(symbols):
    return [ord(symbol) for symbol in symbols]


def generate_code_list_using_listcomps_without_walrusop():
    s = 'ABC'
    codes = [ord(s) for s in s]
    return codes


def generate_code_list_using_listcomps_walrusop(symbols):
    codes = [last := ord(s) for s in symbols]
    return last, codes


def beyond_ascii_listcomps(symbols):
    return [ord(c) for c in symbols if ord(c) > 127]


def beyond_ascii_mapfilter(symbols):
    return list(filter(lambda c: c > 127, map(ord, symbols)))


def list_shallow_copy(letters):
    return letters[:] # or letters[::]


def list_slicing_from_2_index_to_end(letters):
    return letters[2:]


def list_slicing_uppercase_letters(letters):
    return letters[::2]


def list_slicing_lowercase_letters(letters):
    return letters[1::2]


def list_slicing_first_three_letters(letters):
    return letters[:3]


def list_slicing_last_letter(letters):
    return letters[-1:]


def list_slicing_last_three_lowercase_letters(letters):
    return letters[-5::2]


def list_slicing_medium_uppercase_letters(letters):
    return letters[2:5:2]


def list_slicing_reverse_all_letters(letters):
    return letters[::-1]


def list_slicing_uppercase_using_slice_operator(letters):
    return letters[slice(None, None, 2)]


def cartesian_product_tshirts(colors, sizes):
    return [(color, size) for color in colors for size in sizes]


def cartesian_product_tshirts_nestedloop(colors, sizes):
    tshirts = []
    for color in colors:
        for size in sizes:
            tshirts.append((color, size))

    return tshirts


def cartesian_product(l1, l2):
    return [a * b for a in l1 for b in l2]


def generate_codes_using_genexp(symbols):
    return list(ord(c) for c in symbols)