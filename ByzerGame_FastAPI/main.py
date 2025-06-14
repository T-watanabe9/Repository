from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse


app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>WebSocket Echo</title>
    </head>
    <body>
        <h1>WebSocket Echo Test</h1>
        <textarea id="log" rows="10" cols="30"></textarea><br>
        <input id="messageInput" type="text" autocomplete="off"/>
        <button onclick="sendMessage()">Send</button>

        <script>
            const ws = new WebSocket("ws://localhost:8000/ws");
            const log = document.getElementById("log");

            ws.onmessage = function(event) {
                log.value += "Server: " + event.data + "\\n";
            };

            function sendMessage() {
                const input = document.getElementById("messageInput");
                ws.send(input.value);
                log.value += "You: " + input.value + "\\n";
                input.value = '';
            }
        </script>
    </body>
</html>
"""

dic = {'a':'aaa' , 'b':'bbb' , 'c':'ccc'}

@app.get("/")
async def get():
    return dic

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")
