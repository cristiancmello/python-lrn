import array

list_is_container_mutable_sequence = []

an_ordered_list = ['orange', 'apple', 'grape']

heterogeneous_list = [
    str(),
    2.1,
    (1, 2),
    array.array('I', [1]),
    list([1, 2]),
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

list_created_using_constructor_w_dict_items = list({'name': 'John', 'city': 'New York'}.items())

list_created_using_constructor_w_string = list('abc')


def append_element_on_list(e):
    list_is_container_mutable_sequence.append(e)


def list_shallow_copy(letters: list):
    return letters[:]


def list_slicing_from_2_index_to_end(letters: list):
    return letters[2:]


def list_slicing_uppercase_letters(letters: list):
    return letters[::2]


def list_slicing_lowercase_letters(letters: list):
    return letters[1::2]


def list_slicing_first_three_letters(letters: list):
    return letters[:3]


def list_slicing_get_last_letter_in_list(letters: list):
    return letters[-1:]


def list_slicing_get_last_letter(letters: list):
    return letters[-1]


def list_slicing_last_three_lowercase_letters(letters: list):
    return letters[3::2]


def list_slicing_medium_uppercase_letters(letters: list):
    return letters[2:5:2]


def list_slicing_reverse_all_letters(letters: list):
    return letters[::-1]


def list_slicing_uppercase_using_slice_constructor(letters: list):
    return letters[slice(None, None, 2)]


def generate_code_list_using_forloop(symbols: str) -> list[int]:
    codelist = []
    for s in symbols:
        codelist.append(ord(s))
    return codelist


def generate_code_list_using_listcomps(symbols: str) -> list[int]:
    return [ord(s) for s in symbols]


def generate_code_list_using_listcomps_without_walrusop(symbols: str) -> list[int]:
    return [ord(c) for c in symbols]


def generate_code_list_using_listcomps_walrusop(symbols: str) -> tuple[int, list[int]]:
    codelist = [last := ord(s) for s in symbols]
    return last, codelist


def beyond_ascii_listcomps(symbols: str):
    return [ord(s) for s in symbols if ord(s) > 127]


def beyond_ascii_mapfilter(symbols: str):
    return list(filter(lambda s: s > 127, map(ord, symbols)))


def cartesian_product_tshirts(colors: list[str], sizes: list[str]) -> list[tuple[str, str]]:
    return [(color, size) for color in colors for size in sizes]


def cartesian_product_tshirts_nestedloop(colors: list[str], sizes: list[str]) -> list[tuple[str, str]]:
    tshirts = []
    for color in colors:
        for size in sizes:
            tshirts.append((color, size))
    return tshirts


def cartesian_product(l1: list[int], l2: list[int]) -> list[int]:
    return [a * b for a in l1 for b in l2]


def generate_codes_using_genexp(symbols: str) -> list[int]:
    return list(ord(s) for s in symbols)