def celcius_ke_fahrenheit(c):
    try:
        return (float(c) * 9/5) + 32
    except ValueError:
        return "Input tidak valid"

def celcius_ke_kelvin(c):
    try:
        return float(c) + 273.15
    except ValueError:
        return "Input tidak valid"

def celcius_ke_reamur(c):
    try:
        return float(c) * 4/5
    except ValueError:
        return "Input tidak valid"

def idr_ke_usd(rp):
    try:
        # Asumsi 1 USD = 16,000 IDR
        return float(rp) / 16000
    except ValueError:
        return "Input tidak valid"

def idr_ke_eur(rp):
    try:
        # Asumsi 1 EUR = 17,500 IDR
        return float(rp) / 17500
    except ValueError:
        return "Input tidak valid"

def idr_ke_sgd(rp):
    try:
        # Asumsi 1 SGD = 11,800 IDR
        return float(rp) / 11800
    except ValueError:
        return "Input tidak valid"
