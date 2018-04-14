def TM(seq):
    """A basic TM calculator, calculates the anealing temperature
    of a given primer(seq) string"""
    accumulator = 0
    for base in seq.lower():
        if base == "t" or base == "a":
            accumulator += 2
        else:
            accumulator += 4
    return accumulator
