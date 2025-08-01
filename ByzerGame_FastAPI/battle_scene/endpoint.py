from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import json
from . import definition


router = APIRouter()




# メソッドリスト。
method_dict = {
        "ゲートオープン界放！" : definition.open_the_gate
    }

# BattleSceneのリクエスト。
@router.websocket("/")
async def battle_test(websocket: WebSocket):
    print('aa')
    await websocket.accept()
    try:
        while True:
            # クライアントからテキストを受ける。
            data = await websocket.receive_text()
            dic_data:dict = json.loads(data)
            # ヘッダーを取得して、メソッド辞書から実行。
            header = dic_data.get('header')
            response_data = method_dict[header]()
            print(response_data)
            
            # response_dataがNoneじゃなければ。
            if response_data:
                await websocket.send_text(json.dumps(response_data))

    except WebSocketDisconnect:
        print("Client disconnected")

