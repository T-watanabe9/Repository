
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# engineとSessionLocalとbaseのインスタンス化。
# FastAPI起動時の最初の1度だけ実行。以降、このインスタンスをずっと保持。
DATABASE_URL = "postgresql+psycopg2://work:pass0218@localhost/dbgame"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# sqlテーブルをモデルとして定義。
class User(Base):
    __tablename__ = "app_byzer_game_card"
    id = Column(String, primary_key=True)
    name = Column(String)
    category = Column(String)
    cost = Column(Integer)
    reduction_symbol = Column(String)
    color = Column(String)
    race = Column(String)
    effect_text = Column(String)
    symbol = Column(String)
    flavor_text = Column(String)

    def __repr__(self):
        return self.name
    


# FastAPIでの依存関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# SQLセレクト文を成形,実施する関数。
def sql_select(session: Session, **conditions) -> list[User]:
    
    # クエリの宣言。
    query = session.query(User)

    # 引数として受けた検索条件がidを含んでいれば、idと合致するレコードを探索しreturn。
    if (id:= conditions.get('id')):
        query = query.filter(User.id == id)
        # 検索結果の取得。
        result = query.all() # 検索結果の件数に関わらずリスト型を返して欲しいので.all()とした。
        return result        # もし0件の場合は[]が返る。


    # 検索条件がidを含んでない場合、その他の検索条件で順番に絞り込み。

    if (ward := conditions.get('searchText')):
        query = query.filter(or_(
                             User.name.like(f"%{ward}%"),
                             User.race.like(f"%{ward}%"),
                             User.effect_text.like(f"%{ward}%"),
                             ))


    # query.all()やquery.first()で初めてRDBMSに問い合わせが入る。
    return query.order_by(User.cost).all()
