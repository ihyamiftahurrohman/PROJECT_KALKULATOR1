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