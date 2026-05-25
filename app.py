from flask import Flask, render_template, request, jsonify
from datetime import datetime

# Import modules
from modules.aritmatika import *
from modules.logika import *
from modules.transformasi import *
from modules.konversi import *

app = Flask(__name__)

# Auto-cache-busting for static files (CSS/JS)
import os
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            try:
                values['q'] = int(os.stat(file_path).st_mtime)
            except OSError:
                pass
    from flask import url_for
    return url_for(endpoint, **values)

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
        rumus = "Penjumlahan: a + b"
        langkah = f"Menambahkan {angka1} dengan {angka2}: {angka1} + {angka2} = {hasil}"
    elif operator == "-":
        hasil = kurang(angka1, angka2)
        rumus = "Pengurangan: a - b"
        langkah = f"Mengurangi {angka1} dengan {angka2}: {angka1} - {angka2} = {hasil}"
    elif operator == "*":
        hasil = kali(angka1, angka2)
        rumus = "Perkalian: a × b"
        langkah = f"Mengalikan {angka1} dengan {angka2}: {angka1} × {angka2} = {hasil}"
    elif operator == "/":
        hasil = bagi(angka1, angka2)
        rumus = "Pembagian: a ÷ b"
        langkah = f"Membagi {angka1} dengan {angka2}: {angka1} ÷ {angka2} = {hasil}"
    elif operator == "%":
        hasil = modulus(angka1, angka2)
        rumus = "Modulus: a % b (Sisa hasil bagi)"
        langkah = f"Mencari sisa pembagian dari {angka1} dibagi {angka2}: {angka1} % {angka2} = {hasil}"
    elif operator == "**":
        hasil = pangkat(angka1, angka2)
        rumus = "Perpangkatan: a^b (a pangkat b)"
        langkah = f"Mengalikan {angka1} sebanyak {angka2} kali: {angka1}^{angka2} = {hasil}"
    elif operator == "//":
        hasil = floor_division(angka1, angka2)
        rumus = "Floor Division: a // b (Pembagian bulat ke bawah)"
        langkah = f"Hasil bagi bulat dari {angka1} ÷ {angka2} (dibulatkan ke bawah): {angka1} // {angka2} = {hasil}"
    elif operator == "akar":
        hasil = akar(angka1)
        rumus = "Akar Kuadrat: √a"
        langkah = f"Mencari nilai yang jika dikalikan dirinya sendiri menghasilkan {angka1}: √{angka1} = {hasil}"

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
        rumus = "Logika AND: A ∧ B (Bernilai True/1 jika kedua input True)"
        langkah = f"Memeriksa apakah ({a}) DAN ({b}) keduanya True -> {hasil}"
    elif operator == "OR":
        hasil = operasi_or(a, b)
        rumus = "Logika OR: A ∨ B (Bernilai True/1 jika salah satu atau kedua input True)"
        langkah = f"Memeriksa apakah salah satu dari ({a}) ATAU ({b}) bernilai True -> {hasil}"
    elif operator == "NOT":
        hasil = operasi_not(a)
        rumus = "Logika NOT: ¬A (Membalik nilai input A)"
        langkah = f"Membalik nilai kebenaran dari ({a}) -> NOT {a} = {hasil}"
    elif operator == "XOR":
        hasil = operasi_xor(a, b)
        rumus = "Logika XOR: A ⊕ B (Bernilai True/1 jika kedua input berbeda)"
        langkah = f"Memeriksa apakah ({a}) berbeda dengan ({b}) -> {hasil}"
    elif operator == "NAND":
        hasil = operasi_nand(a, b)
        rumus = "Logika NAND: ¬(A ∧ B) (Kebalikan dari AND)"
        langkah = f"Mengambil kebenaran dari: NOT ({a} AND {b}) -> {hasil}"
    elif operator == "NOR":
        hasil = operasi_nor(a, b)
        rumus = "Logika NOR: ¬(A ∨ B) (Kebalikan dari OR)"
        langkah = f"Mengambil kebenaran dari: NOT ({a} OR {b}) -> {hasil}"

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
        rumus = "Desimal ke Biner (Basis 10 -> Basis 2)"
        langkah = f"Membagi angka desimal {angka} dengan 2 secara berulang hingga sisa 0 atau 1: bin({angka}) = {hasil}"
    elif jenis == "oktal":
        hasil = decimal_ke_oktal(angka)
        rumus = "Desimal ke Oktal (Basis 10 -> Basis 8)"
        langkah = f"Membagi angka desimal {angka} dengan 8 secara berulang hingga sisa 0-7: oct({angka}) = {hasil}"
    elif jenis == "hexa":
        hasil = decimal_ke_hexa(angka)
        rumus = "Desimal ke Heksadesimal (Basis 10 -> Basis 16)"
        langkah = f"Membagi angka desimal {angka} dengan 16 secara berulang (sisa 10-15 diganti A-F): hex({angka}) = {hasil}"

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
        rumus = "Konversi ke Fahrenheit: (°C × 9/5) + 32"
        langkah = f"({celcius} × 1.8) + 32 = {celcius * 1.8} + 32 = {hasil}°F"
    elif jenis == "kelvin":
        hasil = celcius_ke_kelvin(celcius)
        rumus = "Konversi ke Kelvin: °C + 273.15"
        langkah = f"{celcius} + 273.15 = {hasil} K"
    elif jenis == "reamur":
        hasil = celcius_ke_reamur(celcius)
        rumus = "Konversi ke Reamur: °C × 4/5"
        langkah = f"{celcius} × 0.8 = {hasil}°Re"

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
        rumus = "IDR ke USD (Kurs: Rp16.000 / USD)"
        langkah = f"Rp{idr:,.0f} ÷ Rp16.000 = ${hasil:.2f} USD"
    elif jenis == "eur":
        hasil = idr_ke_eur(idr)
        rumus = "IDR ke EUR (Kurs: Rp17.500 / EUR)"
        langkah = f"Rp{idr:,.0f} ÷ Rp17.500 = €{hasil:.2f} EUR"
    elif jenis == "sgd":
        hasil = idr_ke_sgd(idr)
        rumus = "IDR ke SGD (Kurs: Rp11.800 / SGD)"
        langkah = f"Rp{idr:,.0f} ÷ Rp11.800 = S${hasil:.2f} SGD"

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
    rumus = "Deret Fibonacci: F(n) = F(n-1) + F(n-2) dengan F(0)=0, F(1)=1"
    langkah = f"Menghasilkan deret hingga suku ke-{n}: {', '.join(map(str, hasil[:10]))}{'...' if len(hasil) > 10 else ''}"
    
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
    rumus = "Faktorial: n! = n × (n-1) × ... × 1 (khusus 0! = 1)"
    
    if n > 0:
        mult_steps = " × ".join(str(i) for i in range(n, 0, -1))
        langkah = f"{n}! = {mult_steps} = {hasil}"
    else:
        langkah = f"0! = {hasil}"

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
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)