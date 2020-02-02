import typer
from cheatsheet.models import basics


app = typer.Typer()


@app.command()
def init():
    ...


@app.command()
def gen_migrations():
    # https://alembic.sqlalchemy.org/en/latest/api/commands.html
    ...


if __name__ == "__main__":
    app()