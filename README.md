# SQLAlchemy cheat sheet

## Running examples

To run the examples, change the `CONNECTION_STRING` in `cheatsheet/__init__.py`. Also change the connection string in `cheatsheet/alembic/alembic.ini` for running Alembic migrations. `mysql-connector` is included as dependency for running the examples against MySQL or MariaDb.

This project uses [Poetry]() to manage dependencies, so install it and then run:

```
poetry shell
```

## Working with Alembic

```
cd cheatsheet
alembic init alembic
alembic revision --autogenerate -m "migration"
```

## Creating Session object

`Session` is basic object that is tied to our SQL connection and will allow us to run various ORM commands as a Unit of Work.

Session is created once in `cheatsheet/__init__.py` like this:

```python
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
Session = sessionmaker()
engine = create_engine(CONNECTION_STRING)
Session.configure(bind=engine)
```