def reverse_complement(sequence):
    """Takes a string (sequence) of DNA and returns the Reverse Complement."""
    reverse_strand = list(reversed(sequence.upper()))        
    return complement(reverse_strand)
    
def complement(sequence):
    """Takes a string (sequence) of DNA and returns the Complementary Strand."""
    comp = ""
    for letter in sequence:
        if letter == "A":
            comp += "T"
        elif letter == "T":
            comp += "A"
        elif letter == "C":
            comp += "G"
        elif letter == "G":
            comp += "C"
        elif letter == "N":
            comp += "N"
        else:
            comp += " _ "
    return comp
