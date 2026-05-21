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