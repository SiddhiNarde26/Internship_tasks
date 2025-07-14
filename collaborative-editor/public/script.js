const editor = document.getElementById('editor');
const statusMessage = document.getElementById('statusMessage');

const ws = new WebSocket('ws://localhost:3000');

ws.onopen = () => {
    console.log('Connected to WebSocket server');
    statusMessage.textContent = 'Connected';
    statusMessage.style.color = '#28a745';
};

ws.onmessage = event => {
    try {
        const message = JSON.parse(event.data);
        if (message.type === 'initial-content' || message.type === 'content-update') {
            if (editor.value !== message.content) {
                const originalSelectionStart = editor.selectionStart;
                const originalSelectionEnd = editor.selectionEnd;

                editor.value = message.content;

                editor.setSelectionRange(originalSelectionStart, originalSelectionEnd);
            }
        }
    } catch (e) {
        console.error("Error parsing message from server:", e);
    }
};

ws.onclose = () => {
    console.log('Disconnected from WebSocket server');
    statusMessage.textContent = 'Disconnected';
    statusMessage.style.color = '#dc3545';
};

ws.onerror = error => {
    console.error('WebSocket error:', error);
    statusMessage.textContent = 'Error!';
    statusMessage.style.color = '#ffc107';
};

editor.addEventListener('input', () => {
    const content = editor.value;
    ws.send(JSON.stringify({ type: 'content-update', content: content }));
});