import array


def generate_codes_using_genexp(symbols):
    return array.array('I', (ord(c) for c in symbols))

