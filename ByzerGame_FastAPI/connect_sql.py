from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://work:pass0218@localhost/dbgame"


class Card(declarative_base()):
    __tablename__ = "app_byzer_game_card"
    id = Column(String, primary_key=True)
    # 他のカラムもあればここに書く

# 引数-カードid?
# 返り値-辞書型
def select(**kwargs):
    if kwargs.get('id') == None:
        return {'result' : 'idがありません!'}
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal() # SessionLocalクラスをインスタンス化。

    # id = 'x001' のCardレコード取得
    card = session.query(Card).filter(Card.id == 'x000').first()

    if card:
        print(f"Found card: id={card.id}")
        return { 'id' : '頭おかしいんじゃないのーーーーーー！？！？！？！？！？！？' }
    else:
        print("Card not found")

    session.close()