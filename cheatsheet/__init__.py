from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


HOSTNAME = 'localhost'
DATABASE = 'cheatsheet'
USER = 'root'
PASSWORD = ''
CONNECTION_STRING = f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOSTNAME}:3306/{DATABASE}'

Session = sessionmaker()
engine = create_engine(CONNECTION_STRING)
Session.configure(bind=engine)