# SQLAlchemy cheat sheet

## Running examples

To run the examples, change the `CONNECTION_STRING` in `cheatsheet/__init__.py`. Also change the connection string in `cheatsheet/alembic/alembic.ini` for running Alembic migrations. `mysql-connector` is included as dependency for running the examples against MySQL or MariaDb.

This project uses [Poetry](https://python-poetry.org/) to manage dependencies, so install it and then run:

```bash
poetry shell
```

Then apply Alembic migrations:
```bash

```

## Working with Alembic

Note: to run the commands in this project, switch to `cheatsheet` directory:

```bash
cd cheatsheet
```

When beginning a new project, Alembic needs to be initialized. It will create `alembic_version` database table with `alembic_num` column to store information about applied migrations:

```bash
alembic init alembic
```

After that, a migration based on changes in the SQLAlchemy model can be generated ("migration" would become the name for the migration):

```bash
alembic revision --autogenerate -m "migration"
```

The new migration file will be stored in `alembic/versions` as a Python file and can be further modified before it is applied. It is a good idea to review the changes, since Alembic might not pick up all changes perfectly.

Generated migrations needs to be applied to the database. Alembic will only apply migrations that haven't been applied before:

```bash
# head refers to the latest migration, 
# but we can provide a different "target" migration here
alembic upgrade head
```

## Creating Session object

`Session` is basic object that is tied to our SQL connection and will allow us to run various ORM commands as a *Unit of Work*.

Session is created once in `cheatsheet/__init__.py` like this:

```python
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
Session = sessionmaker()
engine = create_engine(CONNECTION_STRING)
Session.configure(bind=engine)
```

## Defining SQLAlchemy models

## Basic attributes

## Relationships

## Querying data

## Querying data with joins

## Querying data with aggregations

## Inserting new data

## Inserting data in bulk

## Updating data

## Updating data in bulk