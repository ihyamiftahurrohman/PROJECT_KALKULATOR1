import math

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Tidak bisa dibagi 0"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Tidak bisa di-modulo 0"
    return a % b

def pangkat(a, b):
    return a ** b

def floor_division(a, b):
    if b == 0:
        return "Tidak bisa dibagi 0"
    return a // b

def akar(a):
    if a < 0:
        return "Tidak bisa akar negatif"
    return math.sqrt(a)

def hitung_faktorial(n):
    try:
        n = int(n)
        if n < 0:
            return "Faktorial tidak didefinisikan untuk angka negatif"
        return math.factorial(n)
    except (ValueError, TypeError):
        return "Input harus berupa angka bulat"

def fibonacci_list(n):
    try:
        n = int(n)
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib
    except (ValueError, TypeError):
        return "Input harus berupa angka bulat"