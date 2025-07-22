'''
起動コマンド
uvicorn main:app --reload --port 8080

テストコマンド
curl.exe -X POST http://localhost:8080/build/ -H "Content-Type: application/json" -d "@test.json"
'''


from fastapi import FastAPI, Request, Depends
from connect import get_db, sql_select, select_by_deckrecipe
from battle_scene.endpoint import router 

app = FastAPI()

app.include_router(router)


# getリクエストは本番じゃほぼ使わないがテスト用として。
@app.get("/")
async def get():
    return {'a':'aaa' , 'b':'bbb' , 'c':'ccc'}


#-----------------------------------
# BuildSceneのリクエスト。
#-----------------------------------

# デッキレシピ展開のエンドポイント。
@app.post("/deckrecipe/")
async def search_by_deckrecipe(request: Request, session = Depends(get_db)):

    recipe = await request.json()
    print(f'recieve : {recipe}') # 受けたデータを表示。

    data = select_by_deckrecipe(session, **recipe)
    print(data)
    # result = 
    return data


# 検索条件(search_condition)を辞書型で受けて、connect.pyのselect関数に渡す。
@app.post("/build/")
async def post_build(request: Request, session = Depends(get_db)):
    search_condition = await request.json()
    print(f'Recieve Message : {search_condition}')
    list_users = sql_select(session , **search_condition)
    message = [user.__dict__ for user in list_users]
    print(f'Send Message : {message}')
    return message


