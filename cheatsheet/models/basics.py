import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from cheatsheet import Session


# to declare SQLAlchemy models declaratively, inherit from Base
Base = declarative_base()


class World(Base):
    """Defines various different data types"""
    # how the table is named in the database
    __tablename__ = 'world'

    # primary key is nullable=False and indexed by default
    id = sa.Column(sa.BigInteger, primary_key=True)