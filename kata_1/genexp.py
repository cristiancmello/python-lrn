
def generate_tshirts_strseq(colors, sizes):
    tshirts = ""

    for tshirt in (f'{c} {s}\n' for c in colors for s in sizes):
        tshirts += tshirt

    return tshirts
