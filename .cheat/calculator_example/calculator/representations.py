def bin2int(bin_number: tuple):
    """Returns base 10 representation of binary number BIN_NUMBER"""
    int_number = 0
    for ele in bin_number:
        # left bit shift and or operator
        # for intermediate addition
        int_number = (int_number << 1) | ele
    return int_number
