# 🧮 Kalkulator Canggih Web (Flask-Based Multi-Calculator)

Sebuah aplikasi kalkulator berbasis web interaktif yang dikembangkan menggunakan **Flask (Python)** untuk *backend* serta **HTML, CSS, dan JavaScript murni (Vanilla)** untuk *frontend*. Proyek ini dirancang sebagai aplikasi kalkulator multi-fungsi yang tidak hanya melakukan operasi matematika dasar, tetapi juga operasi logika, konversi basis bilangan, konversi suhu, konversi mata uang, hingga fungsi matematika lanjut seperti Fibonacci dan Faktorial.

Aplikasi ini dilengkapi dengan fitur **Riwayat Perhitungan (History)** yang tersimpan selama sesi berjalan serta fitur **Tema Gelap/Terang (Toggle Dark Mode)** untuk kenyamanan visual pengguna.

---

## 🚀 Fitur Utama

Aplikasi ini memiliki 5 kategori fitur utama yang terorganisir dalam tata letak kartu (*cards*) yang responsif:

### 1. ➕ Aritmatika
Mendukung berbagai operasi aritmatika dasar dan menengah:
*   **Penjumlahan (`+`)**
*   **Pengurangan (`-`)**
*   **Perkalian (`×`)**
*   **Pembagian (`÷`)**
*   **Modulus (`%`)** (Sisa hasil bagi)
*   **Pangkat (`^`)**
*   **Floor Division (`//`)** (Pembagian bulat ke bawah)
*   **Akar Kuadrat (`√`)**

### 2. 🔀 Operator Logika
Melakukan operasi logika *Boolean* menggunakan input bertipe string/Boolean (seperti `true`/`false`, `1`/`0`, `t`/`f`, `y`/`n`):
*   **AND**
*   **OR**
*   **NOT** (hanya beroperasi pada Input 1)
*   **XOR**
*   **NAND**
*   **NOR**

### 3. 🔄 Transformasi & Konversi
Kategori ini menggunakan satu kolom input nilai yang dapat dikonversikan ke berbagai format:
*   **Basis Angka:** Mengubah bilangan Desimal ke basis **Biner**, **Oktal**, atau **Heksadesimal**.
*   **Suhu:** Mengonversi derajat **Celcius** ke **Fahrenheit**, **Kelvin**, atau **Reamur**.
*   **Mata Uang:** Mengonversi **Rupiah (IDR)** ke mata uang asing: **USD** (kurs asumsian 16.000), **EUR** (kurs 17.500), atau **SGD** (kurs 11.800).

### 4. 🧮 Matematika Lanjut (Bonus)
Fungsi khusus berbasis teori matematika terapan:
*   **Deret Fibonacci:** Menghasilkan deret Fibonacci hingga suku ke-N.
*   **Faktorial (`n!`):** Menghitung hasil perkalian faktorial dari bilangan bulat positif N.

### 5. ⏳ Riwayat & Kustomisasi UI
*   **Riwayat Perhitungan:** Mencatat semua hasil operasi sebelumnya lengkap dengan rumus dan langkah perhitungannya. Riwayat dibatasi hingga 20 entri terakhir dan dapat dibersihkan dengan tombol "Hapus Riwayat".
*   **Toggle Tema (Dark Mode):** Memungkinkan perpindahan instan antara tema gelap yang modern dan tema terang yang bersih.

---

## 📂 Struktur Proyek

Berikut adalah struktur direktori dari proyek Kalkulator Canggih Web ini:

```text
PROJECT_KALKULATOR/
├── modules/                   # Modul Python untuk fungsi logika kalkulator
│   ├── aritmatika.py          # Logika fungsi aritmatika, faktorial, dan fibonacci
│   ├── konversi.py            # Logika konversi suhu dan mata uang
│   ├── logika.py              # Logika operasi Boolean (AND, OR, XOR, dll)
│   └── transformasi.py        # Logika konversi basis bilangan (Biner, Oktal, Hexa)
├── static/                    # File aset statis
│   ├── css/
│   │   └── style.css          # Desain antarmuka, tata letak grid, dan tema gelap/terang
│   └── js/
│       └── script.js          # Logic frontend untuk melakukan request AJAX ke server Flask
├── templates/
│   └── index.html             # Layout utama kalkulator (HTML5)
├── .gitignore                 # File konfigurasi git ignore untuk Python
├── app.py                     # Entry point utama aplikasi Flask (Backend)
├── README.md                  # Dokumentasi proyek (File ini)
└── requirements.txt           # File daftar dependensi proyek (Flask)
```

---

## 🛠️ Teknologi yang Digunakan

*   **Backend:** [Python 3.x](https://www.python.org/) dengan *micro-framework* [Flask](https://flask.palletsprojects.com/)
*   **Frontend:** HTML5, CSS3 (Modern Flexbox/Grid & CSS Variables), JavaScript (Fetch API untuk request asynchronous)
*   **API:** RESTful JSON API untuk komunikasi data antara frontend dan backend tanpa reload halaman.

---

## ⚙️ Cara Instalasi dan Menjalankan Proyek

Ikuti langkah-langkah di bawah ini untuk menjalankan aplikasi di komputer lokal Anda:

### 1. Prasyarat
Pastikan Anda sudah menginstal **Python 3.x** di komputer Anda. Anda bisa memverifikasinya melalui command prompt/terminal:
```bash
python --version
```

### 2. Kloning Proyek
Unduh kode sumber atau kloning repositori ini:
```bash
git clone https://github.com/username/PROJECT_KALKULATOR.git
cd PROJECT_KALKULATOR
```
*(Catatan: Sesuaikan link dengan tautan repositori Anda jika di-host di GitHub).*

### 3. Instalasi Dependensi
Instal framework Flask yang dibutuhkan oleh aplikasi ini. Jalankan perintah berikut di terminal:
```bash
pip install -r requirements.txt
```
*Atau secara langsung:*
```bash
pip install Flask
```

### 4. Jalankan Aplikasi
Jalankan file entry point `app.py` menggunakan Python:
```bash
python app.py
```

Setelah server aktif, Anda akan melihat output di terminal yang menunjukkan bahwa server lokal berjalan di:
```text
 * Running on http://127.0.0.1:5000
```

### 5. Akses Aplikasi di Browser
Buka browser web favorit Anda (Chrome, Edge, Firefox, dll) lalu akses alamat berikut:
```text
http://127.0.0.1:5000
```

---

## 💡 Cara Kerja Aplikasi

1.  **Pengiriman Data (AJAX):** Setiap kali tombol operasi ditekan (misalnya tombol `+`), JavaScript di frontend akan menangkap input dari form terkait.
2.  **Fetch API:** JavaScript mengirimkan data tersebut ke server Flask secara asinkron menggunakan format JSON melalui method `POST` (contoh route: `/aritmatika`, `/logika`, dll).
3.  **Proses di Backend:** Server Flask menerima request tersebut, memanggil modul kalkulator yang sesuai di direktori `/modules`, menghitung hasilnya, serta mencatat transaksi tersebut ke dalam riwayat global (*history list*).
4.  **Respons JSON:** Flask mengembalikan respons berupa format JSON berisi hasil akhir, rumus, langkah-langkah detail, beserta daftar riwayat terbaru.
5.  **Render UI:** JavaScript menerima respons dari server dan memperbarui tampilan (DOM) secara real-time tanpa perlu me-refresh halaman web secara keseluruhan.

---

## 📝 Kontributor
*   **Nama Mahasiswa / Pengembang:** [ihyamiftahurrohman]
*   **Mata Kuliah:** Pengantar Pemrograman
*   **Semester:** Semester 2 
