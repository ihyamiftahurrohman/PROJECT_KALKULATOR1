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

# =========================================
# OPERATOR LOGIKA
# =========================================
@app.route('/logika', methods=['POST'])
def logika():
    data = request.get_json()

# =========================================
# TRANSFORMASI BILANGAN
# =========================================
@app.route('/transformasi', methods=['POST'])
def transformasi():
    data = request.get_json()