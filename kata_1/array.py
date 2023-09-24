from array import array


def generate_codes_using_genexp(symbols: str):
    return array('I', (ord(s) for s in symbols))  # second arg: () are required
