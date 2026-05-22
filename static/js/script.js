// Fungsi Helper untuk merender history
function renderHistory(historyList) {
    const container = document.getElementById("historyContainer");
    if (!historyList || historyList.length === 0) {
        container.innerHTML = "<p>Belum ada riwayat.</p>";
        return;
    }

    let html = "<ul>";
    historyList.forEach(item => {
        html += `<li>
            <span style="color: #6272a4;">[${item.waktu}]</span> 
            <span style="color: #ff79c6;">${item.kategori} (${item.operasi}):</span> 
            <span style="color: #50fa7b;">${item.langkah}</span>
        </li>`;
    });
    html += "</ul>";
    container.innerHTML = html;
}

// =====================
// ARITMATIKA
// =====================
function hitung(op) {
    fetch('/aritmatika', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            angka1: document.getElementById("angka1").value,
            angka2: document.getElementById("angka2").value,
            operator: op
        })
    })
    .then(r => r.json())
    .then(data => {
        document.getElementById("rumusAritmatika").innerHTML = data.rumus;
        document.getElementById("langkahAritmatika").innerHTML = data.langkah;
        document.getElementById("hasil").innerHTML = data.hasil;
        renderHistory(data.history);
    });
}

function akar() {
    fetch('/aritmatika', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            angka1: document.getElementById("angka1").value,
            angka2: "0", 
            operator: "akar"
        })
    })
    .then(r => r.json())
    .then(data => {
        document.getElementById("rumusAritmatika").innerHTML = data.rumus;
        document.getElementById("langkahAritmatika").innerHTML = data.langkah;
        document.getElementById("hasil").innerHTML = data.hasil;
        renderHistory(data.history);
    });
}

// =====================
// LOGIKA
// =====================
function logika(op) {
    fetch('/logika', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            a: document.getElementById("logika1").value,
            b: document.getElementById("logika2").value,
            operator: op
        })
    })
    .then(r => r.json())
    .then(data => {
        document.getElementById("rumusLogika").innerHTML = data.rumus;
        document.getElementById("langkahLogika").innerHTML = data.langkah;
        document.getElementById("hasilLogika").innerHTML = data.hasil;
        renderHistory(data.history);
    });
}

// =====================
// TRANSFORMASI BILANGAN
// =====================
function transformasi(jenis) {
    fetch('/transformasi', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            angka: document.getElementById("angkaTransformasi").value,
            jenis: jenis
        })
    })
    .then(r => r.json())
    .then(data => {
        document.getElementById("rumusTransformasi").innerHTML = data.rumus;
        document.getElementById("langkahTransformasi").innerHTML = data.langkah;
        document.getElementById("hasilTransformasi").innerHTML = data.hasil;
        renderHistory(data.history);
    });
}

// =====================
// KONVERSI SUHU
// =====================
function suhu(jenis) {
    fetch('/suhu', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            celcius: document.getElementById("angkaTransformasi").value,
            jenis: jenis
        })
    })
    .then(r => r.json())
    .then(data => {
        document.getElementById("rumusTransformasi").innerHTML = data.rumus;
        document.getElementById("langkahTransformasi").innerHTML = data.langkah;
        document.getElementById("hasilTransformasi").innerHTML = data.hasil;
        renderHistory(data.history);
    });
}

// =====================
// KONVERSI MATA UANG
// =====================
function mata_uang(jenis) {
    fetch('/mata_uang', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            idr: document.getElementById("angkaTransformasi").value,
            jenis: jenis
        })
    })
    .then(r => r.json())
    .then(data => {
        document.getElementById("rumusTransformasi").innerHTML = data.rumus;
        document.getElementById("langkahTransformasi").innerHTML = data.langkah;
        document.getElementById("hasilTransformasi").innerHTML = data.hasil;
        renderHistory(data.history);
    });
}

// =====================
// MATEMATIKA LANJUT
// =====================
function fibonacci() {
    fetch('/fibonacci', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            n: document.getElementById("angkaBonus").value
        })
    })
    .then(r => r.json())
    .then(data => {
        document.getElementById("rumusBonus").innerHTML = data.rumus;
        document.getElementById("langkahBonus").innerHTML = data.langkah;
        document.getElementById("hasilBonus").innerHTML = data.hasil; // array di konversi jadi string
        renderHistory(data.history);
    });
}