from flask import Flask, render_template, request, jsonify
from datetime import datetime

# Import modules
from modules.aritmatika import *
from modules.logika import *
from modules.transformasi import *
from modules.konversi import *

app = Flask(__name__)

# Global history
history = []

def record_history(kategori, operasi, rumus, langkah, hasil):
    item = {
        'waktu': datetime.now().strftime("%H:%M:%S"),
        'kategori': kategori,
        'operasi': operasi,
        'rumus': str(rumus),
        'langkah': str(langkah),
        'hasil': str(hasil)
    }
    history.insert(0, item)
    if len(history) > 20:
        history.pop()

@app.route('/')
def home():
    return render_template('index.html')


# =========================================
# ARITMATIKA
# =========================================
@app.route('/aritmatika', methods=['POST'])
def aritmatika():
    data = request.get_json()
    try:
        angka1 = float(data.get('angka1', 0) if data.get('angka1') != "" else 0)
    except (ValueError, TypeError):
        angka1 = 0.0

    try:
        angka2 = float(data.get('angka2', 0) if data.get('angka2') != "" else 0)
    except (ValueError, TypeError):
        angka2 = 0.0

    operator = data.get('operator')
    hasil = ""
    rumus = ""
    langkah = ""

    if operator == "+":
        hasil = tambah(angka1, angka2)
        rumus = "a + b"
        langkah = f"{angka1} + {angka2} = {hasil}"
    elif operator == "-":
        hasil = kurang(angka1, angka2)
        rumus = "a - b"
        langkah = f"{angka1} - {angka2} = {hasil}"
    elif operator == "*":
        hasil = kali(angka1, angka2)
        rumus = "a × b"
        langkah = f"{angka1} × {angka2} = {hasil}"
    elif operator == "/":
        hasil = bagi(angka1, angka2)
        rumus = "a ÷ b"
        langkah = f"{angka1} ÷ {angka2} = {hasil}"
    elif operator == "%":
        hasil = modulus(angka1, angka2)
        rumus = "a % b"
        langkah = f"{angka1} % {angka2} = {hasil}"
    elif operator == "**":
        hasil = pangkat(angka1, angka2)
        rumus = "a pangkat b"
        langkah = f"{angka1}^{angka2} = {hasil}"
    elif operator == "//":
        hasil = floor_division(angka1, angka2)
        rumus = "a // b"
        langkah = f"{angka1} // {angka2} = {hasil}"
    elif operator == "akar":
        hasil = akar(angka1)
        rumus = "√a"
        langkah = f"√{angka1} = {hasil}"

    record_history("Aritmatika", operator, rumus, langkah, hasil)

    return jsonify({
        'hasil': hasil,
        'rumus': rumus,
        'langkah': langkah,
        'history': history
    })


# =========================================
# OPERATOR LOGIKA
# =========================================
@app.route('/logika', methods=['POST'])
def logika():
    data = request.get_json()
    a_raw = str(data.get('a', '')).strip().lower()
    b_raw = str(data.get('b', '')).strip().lower()
    
    a = a_raw in ['true', '1', 't', 'y', 'yes']
    b = b_raw in ['true', '1', 't', 'y', 'yes']
    
    operator = data.get('operator')
    hasil = ""
    rumus = ""
    langkah = ""

    if operator == "AND":
        hasil = operasi_and(a, b)
        rumus = "A AND B"
        langkah = f"{a} AND {b} = {hasil}"
    elif operator == "OR":
        hasil = operasi_or(a, b)
        rumus = "A OR B"
        langkah = f"{a} OR {b} = {hasil}"
    elif operator == "NOT":
        hasil = operasi_not(a)
        rumus = "NOT A"
        langkah = f"NOT {a} = {hasil}"
    elif operator == "XOR":
        hasil = operasi_xor(a, b)
        rumus = "A XOR B"
        langkah = f"{a} XOR {b} = {hasil}"
    elif operator == "NAND":
        hasil = operasi_nand(a, b)
        rumus = "A NAND B"
        langkah = f"{a} NAND {b} = {hasil}"
    elif operator == "NOR":
        hasil = operasi_nor(a, b)
        rumus = "A NOR B"
        langkah = f"{a} NOR {b} = {hasil}"

    record_history("Logika", operator, rumus, langkah, hasil)

    return jsonify({
        'hasil': hasil,
        'rumus': rumus,
        'langkah': langkah,
        'history': history
    })


# =========================================
# TRANSFORMASI BILANGAN
# =========================================
@app.route('/transformasi', methods=['POST'])
def transformasi():
    data = request.get_json()
    try:
        angka = int(data.get('angka', 0) if data.get('angka') != "" else 0)
    except (ValueError, TypeError):
        angka = 0

    jenis = data.get('jenis')
    hasil = ""
    rumus = ""
    langkah = ""

    if jenis == "biner":
        hasil = decimal_ke_biner(angka)
        rumus = "Desimal -> Biner"
        langkah = f"bin({angka}) = {hasil}"
    elif jenis == "oktal":
        hasil = decimal_ke_oktal(angka)
        rumus = "Desimal -> Oktal"
        langkah = f"oct({angka}) = {hasil}"
    elif jenis == "hexa":
        hasil = decimal_ke_hexa(angka)
        rumus = "Desimal -> Heksadesimal"
        langkah = f"hex({angka}) = {hasil}"

    record_history("Transformasi Basis", jenis, rumus, langkah, hasil)

    return jsonify({
        'hasil': hasil,
        'rumus': rumus,
        'langkah': langkah,
        'history': history
    })


# =========================================
# KONVERSI SUHU
# =========================================
@app.route('/suhu', methods=['POST'])
def suhu():
    data = request.get_json()
    try:
        celcius = float(data.get('celcius', 0) if data.get('celcius') != "" else 0)
    except (ValueError, TypeError):
        celcius = 0.0

    jenis = data.get('jenis')
    hasil = ""
    rumus = ""
    langkah = ""

    if jenis == "fahrenheit":
        hasil = celcius_ke_fahrenheit(celcius)
        rumus = "(C × 9/5) + 32"
        langkah = f"({celcius} × 9/5) + 32 = {hasil}"
    elif jenis == "kelvin":
        hasil = celcius_ke_kelvin(celcius)
        rumus = "C + 273.15"
        langkah = f"{celcius} + 273.15 = {hasil}"
    elif jenis == "reamur":
        hasil = celcius_ke_reamur(celcius)
        rumus = "C × 4/5"
        langkah = f"{celcius} × 4/5 = {hasil}"

    record_history("Suhu", jenis, rumus, langkah, hasil)

    return jsonify({
        'hasil': hasil,
        'rumus': rumus,
        'langkah': langkah,
        'history': history
    })


# =========================================
# KONVERSI MATA UANG
# =========================================
@app.route('/mata_uang', methods=['POST'])
def mata_uang():
    data = request.get_json()
    try:
        idr = float(data.get('idr', 0) if data.get('idr') != "" else 0)
    except (ValueError, TypeError):
        idr = 0.0

    jenis = data.get('jenis')
    hasil = ""
    rumus = ""
    langkah = ""

    if jenis == "usd":
        hasil = idr_ke_usd(idr)
        rumus = "IDR / 16000"
        langkah = f"{idr} / 16000 = {hasil}"
    elif jenis == "eur":
        hasil = idr_ke_eur(idr)
        rumus = "IDR / 17500"
        langkah = f"{idr} / 17500 = {hasil}"
    elif jenis == "sgd":
        hasil = idr_ke_sgd(idr)
        rumus = "IDR / 11800"
        langkah = f"{idr} / 11800 = {hasil}"

    record_history("Mata Uang", jenis, rumus, langkah, hasil)

    return jsonify({
        'hasil': hasil,
        'rumus': rumus,
        'langkah': langkah,
        'history': history
    })


# =========================================
# FIBONACCI
# =========================================
@app.route('/fibonacci', methods=['POST'])
def fibonacci():
    data = request.get_json()
    try:
        n = int(data.get('n', 0) if data.get('n') != "" else 0)
    except (ValueError, TypeError):
        n = 0

    hasil = fibonacci_list(n)
    rumus = "F(n) = F(n-1) + F(n-2)"
    langkah = f"Deret Fibonacci hingga {n} angka"
    
    record_history("Bonus", "fibonacci", rumus, langkah, str(hasil))

    return jsonify({
        'hasil': hasil,
        'rumus': rumus,
        'langkah': langkah,
        'history': history
    })


# =========================================
# FAKTORIAL
# =========================================
@app.route('/faktorial', methods=['POST'])
def faktorial():
    data = request.get_json()
    try:
        n = int(data.get('n', 0) if data.get('n') != "" else 0)
    except (ValueError, TypeError):
        n = 0

    hasil = hitung_faktorial(n)
    rumus = "n! = n × (n-1) × ... × 1"
    langkah = f"{n}! = {hasil}"

    record_history("Bonus", "faktorial", rumus, langkah, hasil)

    return jsonify({
        'hasil': hasil,
        'rumus': rumus,
        'langkah': langkah,
        'history': history
    })


# =========================================
# HAPUS RIWAYAT
# =========================================
@app.route('/clear_history', methods=['POST'])
def clear_history():
    global history
    history.clear()
    return jsonify({'status': 'success', 'history': history})


# =========================================
# MENJALANKAN FLASK
# =========================================
if __name__ == '__main__':
    app.run(debug=True)