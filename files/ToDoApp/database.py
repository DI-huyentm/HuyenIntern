from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Database configuration
# db = pymysql.connect(
#     host="127.0.0.1",
#     user="root",
#     password="",
#     database="huyenngo",
#     cursorclass=pymysql.cursors.DictCursor,
# )

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:@127.0.0.1:3306/huyenngo'

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind = engine)
Base = declarative_base()


