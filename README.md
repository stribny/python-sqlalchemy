# SQLAlchemy cheat sheet

## Running examples

To run the examples, change the `CONNECTION_STRING` in `cheatsheet/__init__.py`. Also change the connection string in `cheatsheet/alembic/alembic.ini` for running Alembic migrations. `mysql-connector` is included as dependency for running the examples against MySQL or MariaDb.

This project uses [Poetry](https://python-poetry.org/) to manage dependencies, so install it and then run:

```bash
poetry shell
```

Then apply Alembic migrations:
```bash
cd cheatsheet && alembic upgrade head
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

## Alternatives to using Alembic

### nomad

In case Alembic doesn't work well for us, we can use a simple migration tool [nomad](https://pypi.org/project/nomad/) that works with plain Python scripts and SQL files.

One possible workflow could be to use Alembic to only generate initial migration SQL based on the diff between our models and a database, but store and run migrations using nomad.

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

There are two basic ways to define our models in SQLAlchemy:
- subclassing from `Base` class
- using classical mapping through `MetaData` object

## Basic attributes

## Relationships

Relationships are defined using `relationship` function.

When we define relationships, we need to choose a loading strategy that SQLAlchemy will use to load relevant objects into memory. There are two basic loading strategies:
- lazy loading (default)
- eager loading

## Column property

Column properties can be used for automatically computed columns.

For instance, if we have a `Poll` with multiple `Voter`s, we can automatically expose the number
of voters in the `Poll` object:

```python
import sqlalchemy as sa
from sqlalchemy import select, func
from sqlalchemy.orm import column_property
from sqlalchemy.sql.functions import coalesce

class Voter(Base):
    id = Column(sa.BigInteger, autoincrement=True, primary_key=True, index=True)
    poll_id = Column(sa.BigInteger, ForeignKey("polls.id"), nullable=False)

class Poll(Base):
    id = Column(sa.BigInteger, autoincrement=True, primary_key=True, index=True)
    voters = sa.relationship("Voter", backref="poll")
    # coalesce will handle the situation where there aren't any
    #   voters yet associated with the poll
    n_voters = column_property(
        select([coalesce(func.count(Voter.id), 0)])
    )
```

## Querying data

## Querying data with joins

## Querying data with aggregations

## Inserting new data

## Inserting data in bulk

## Updating data

## Updating data in bulk