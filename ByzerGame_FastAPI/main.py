'''
起動コマンド
uvicorn main:app --reload --port 8080

テストコマンド
curl.exe -X POST http://localhost:8080/build/ -H "Content-Type: application/json" -d "@test.json"
'''


from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request, Depends
from connect import get_db, select

app = FastAPI()


# getリクエストは本番じゃほぼ使わないがテスト用として。
@app.get("/")
async def get():
    return {'a':'aaa' , 'b':'bbb' , 'c':'ccc'}


# BuildSceneのリクエスト。
# Build場面はすべてpostで良いと思う。
# 検索条件(search_condition)を辞書型で受けて、connect.pyのselect関数に渡す。
@app.post("/build/")
async def post_build(request: Request , session = Depends(get_db)):
    search_condition = await request.json()
    print(search_condition)
    result = select(session , **search_condition)
    print(result)
    return  [user.__dict__ for user in result]


# RunSceneのリクエスト。
# Run場面はすべてwssが良いチャットっぽいので。
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")
