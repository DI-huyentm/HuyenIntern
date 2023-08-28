from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todos.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind = engine)
Base = declarative_base()

# 12 vien bi 1 vien gia
# 8 vien: (1) con lai 4 vien
# neu bang nhau => vien gia trong 4 vien, lay 2 vien trong do can(2):
#     bang nhau=> can 1 vien that 1 vien gia/that(3)
#     lech nhau => can 1 vien that 1 vien gia/that(3)
# neu lech nhau => lay 2 vien trong 4 o moi ben, dem di can(2):
#     bang nhau => 
# => can 1 ben trong 2 voi 1 ben trong 10 (2)
# neu khac nhau => can 
