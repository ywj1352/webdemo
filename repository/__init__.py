from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:12345678@127.0.0.1:3306/bookstore", echo=True)
DBSession = sessionmaker(bind=engine)
