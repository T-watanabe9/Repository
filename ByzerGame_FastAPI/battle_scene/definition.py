

class battle:
    pass



# battle_sceneで返すjason。
response_data = {
        "header":"CreateCard",

        "body":"～関数に渡す値～"
    }


# ゲーム開始時の処理
def open_the_gate():
    instance = battle()
    
    draw()
    draw()
    draw()
    draw()
    draw()

    response = {

        "header":"CreateCard",
        "body":"CreateCard" 
    }

    return response

# カードを引く、みたいな。
def draw():
    print('カードを1枚引いた!')
    return
