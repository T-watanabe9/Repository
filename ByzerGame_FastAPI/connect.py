
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# engineとSessionLocalとbaseのインスタンス化。
# FastAPI起動時の最初の1度だけ実行。以降、このインスタンスをずっと保持。
DATABASE_URL = "postgresql+psycopg2://work:pass0218@localhost/dbgame"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


# sqlテーブルをモデルとして定義。
class User(base):
    __tablename__ = "app_byzer_game_card"
    id = Column(String, primary_key=True)
    name = Column(String)
    cost = Column(Integer)
    effect_text = Column(String)

    def __repr__(self):
        return self.name
    


# FastAPIでの依存関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# クエリ関数（例：動的検索）
def sql_select(session: Session, **kwargs):
    
    # SQLクエリ文の整形。
    query = session.query(User)

    if (id:= kwargs.get('id'))is not None:
        query = query.filter(User.id == id)
        return query.first()

    if (text:= kwargs.get('searchText')) is not None:
        query = query.filter(User.name.like(f"%{text}%"))

    # if (name:= kwargs.get('name')) is not None:
    #     query = query.filter(User.name.like(f"%{name}%"))

    # query.all()やquery.first()で初めてRDBMSに問い合わせが入る。
    return query.order_by(User.cost).all()
