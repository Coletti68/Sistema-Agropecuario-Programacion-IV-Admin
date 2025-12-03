const ws_scheme = window.location.protocol === "https:" ? "wss" : "ws";
const socket = new WebSocket(ws_scheme + '://' + window.location.host + "/ws/notificaciones/");

socket.onopen = () => console.log("✅ WebSocket conectado");
socket.onclose = () => console.log("❌ WebSocket cerrado");
socket.onerror = (e) => console.error("❌ Error WebSocket", e);

socket.onmessage = (event) => {
    const data = JSON.parse(event.data);

    if (data.evento === "nuevo_usuario") {
        const tbody = document.getElementById('usuarios-tbody');
        if (!tbody) return;

        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${escapeHtml(data.nombre)}</td>
            <td>${escapeHtml(data.email)}</td>
            <td>${escapeHtml(data.rol || '')}</td>
            <td>Activo</td>
            <td>
                <a href="#" class="btn btn-warning">Editar</a>
                <a href="#" class="btn btn-danger">Desactivar</a>
            </td>
        `;
        tbody.prepend(tr);

        showToast("📢 Nuevo usuario registrado: " + data.nombre);
    }
};

function escapeHtml(unsafe) {
    if (!unsafe && unsafe !== 0) return '';
    return String(unsafe)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
}

function showToast(message) {
    const toast = document.createElement('div');
    toast.className = "toast-message";
    toast.innerText = message;
    document.body.appendChild(toast);

    setTimeout(() => toast.remove(), 3000);
}
