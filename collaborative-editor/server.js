const express = require('express');
const http = require('http');
const WebSocket = require('ws');

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

const PORT = process.env.PORT || 3000;

app.use(express.static('public'));

const clients = new Set();
let documentContent = '';

wss.on('connection', ws => {
    clients.add(ws);
    console.log('Client connected');

    ws.send(JSON.stringify({ type: 'initial-content', content: documentContent }));

    ws.on('message', message => {
        console.log('received: %s', message);

        try {
            const parsedMessage = JSON.parse(message);

            if (parsedMessage.type === 'content-update') {
                documentContent = parsedMessage.content;
                clients.forEach(client => {
                    if (client !== ws && client.readyState === WebSocket.OPEN) {
                        client.send(JSON.stringify({ type: 'content-update', content: documentContent }));
                    }
                });
            }
        } catch (e) {
            console.error("Failed to parse message or invalid message format:", e);
        }
    });

    ws.on('close', () => {
        clients.delete(ws);
        console.log('Client disconnected');
    });

    ws.on('error', error => {
        console.error('WebSocket error:', error);
    });
});

server.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}`);
});