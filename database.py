from sqlalchemy import create_engine
# from sqlalchemy import  MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import setting


engine = create_engine(setting.database_url, connect_args={
                       "check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



def create_table():
    # 1. Удаляет ВСЕ таблицы
    # Base.metadata.drop_all(engine)

    # 2. Создает ВСЕ таблицы заново
    Base.metadata.create_all(engine)


# create_table()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        

