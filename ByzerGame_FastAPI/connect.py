
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# engineとSessionLocalとbaseのインスタンス化。
# FastAPI起動時の最初の1度だけ実行。以降、このインスタンスをずっと保持。
DATABASE_URL = "postgresql+psycopg2://work:pass0218@localhost/dbgame"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# FastAPIでの依存関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




#-----------------------------------
# SQLテーブルをモデルとして定義
#-----------------------------------

# Raceテーブル。
class RaceDB(Base):
    __tablename__ = "app_byzer_game_race"

    id    = Column(Integer, primary_key=True)
    name  = Column(String, nullable=False)
    order = Column(Integer)

    def __repr__(self):
        return f"<Race {self.id}:{self.name}>"

# Cardテーブル。
class CardDB(Base):
    __tablename__ = "app_byzer_game_card"
    id = Column(String, primary_key=True)
    name = Column(String)
    category = Column(String)
    cost = Column(Integer)
    reduction_symbol = Column(String)
    color = Column(String)
    race1_id = Column(Integer, ForeignKey("app_byzer_game_race.id"))
    race2_id = Column(Integer, ForeignKey("app_byzer_game_race.id"))
    race3_id = Column(Integer, ForeignKey("app_byzer_game_race.id"))
    effect_text = Column(String)
    symbol = Column(String)
    flavor_text = Column(String)

    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "cost": self.cost,
            "reduction_symbol": self.reduction_symbol,
            "color": self.color,
            "race1": self.race1.name if self.race1 else None,
            "race2": self.race2.name if self.race2 else None,
            "race3": self.race3.name if self.race3 else None,
            "effect_text": self.effect_text,
            "symbol": self.symbol,
            "flavor_text": self.flavor_text,
        }

    def __repr__(self):
        return self.name
    




#-----------------------------------
# SELECTのためのメソッド。
#-----------------------------------



# デッキレシピで展開するsqlクエリを書くメソッド。
def select_by_deckrecipe(session: Session, **recipe):
    
    result = {}

    # mainリストが存在すれば実行。
    list_main = recipe.get('main')
    if list_main:
        result["main"] = []
        for cardID in list_main : 
            # print(cardID)
            query = session.query(CardDB).filter(CardDB.id == cardID)
            result["main"].append(query.first().to_dict())

    # exリストが存在すれば実行。
    list_ex = recipe.get('ex')
    if list_ex:
        result["ex"] = []
        for cardID in list_ex : 
            # print(cardID)
            query = session.query(CardDB).filter(CardDB.id == cardID)
            result["ex"].append(query.first().to_dict())

    return result




# # SQLセレクト文を成形,実施する関数。
# # テーブル定義のうち、raceを書き直したので、そこは修正。
# def sql_select(session: Session, **conditions) -> list[CardDB]:
    
    # # クエリの宣言。
    # query = session.query(CardDB)

    # # 引数として受けた検索条件がidを含んでいれば、idと合致するレコードを探索しreturn。
    # if (id:= conditions.get('id')):
    #     query = query.filter(CardDB.id == id)
    #     # 検索結果の取得。
    #     result = query.all() # 検索結果の件数に関わらずリスト型を返して欲しいので.all()とした。
    #     return result        # もし0件の場合は[]が返る。


    # # 検索条件がidを含んでない場合、その他の検索条件で順番に絞り込み。

    # if (ward := conditions.get('searchText')):
    #     query = query.filter(or_(
    #                          CardDB.name.like(f"%{ward}%"),
    #                          CardDB.race.like(f"%{ward}%"),
    #                          CardDB.effect_text.like(f"%{ward}%"),
    #                          ))


    # # query.all()やquery.first()で初めてRDBMSに問い合わせが入る。
    # return query.order_by(CardDB.cost).all()
    
    # return []

