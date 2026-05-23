def decimal_ke_biner(angka):
    try:
        return bin(int(angka))[2:]
    except ValueError:
        return "Input tidak valid"

def decimal_ke_oktal(angka):
    try:
        return oct(int(angka))[2:]
    except ValueError:
        return "Input tidak valid"

def decimal_ke_hexa(angka):
    try:
        return hex(int(angka))[2:].upper()
    except ValueError:
        return "Input tidak valid"