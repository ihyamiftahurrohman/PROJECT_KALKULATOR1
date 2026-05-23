def operasi_and(a, b):
    return a and b

def operasi_or(a, b):
    return a or b

def operasi_not(a):
    return not a

def operasi_xor(a, b):
    return (a and not b) or (not a and b)

def operasi_nand(a, b):
    return not (a and b)

def operasi_nor(a, b):
    return not (a or b)