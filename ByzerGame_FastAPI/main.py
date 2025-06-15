'''
起動コマンド
uvicorn main:app --reload --port 8080
'''

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from connect_sql import select
from fastapi import Request


app = FastAPI()


dic_test = {'a':'aaa' , 'b':'bbb' , 'c':'ccc'}

# @app.get("/")
# async def get():
#     return dic_test

@app.post("/")
async def post(request: Request):
    print('postを受けた!')
    data = await request.json()
    print(type(data), data)
    dic_result = select(**data)
    return dic_result

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")
