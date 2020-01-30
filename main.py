import typer
from cheatsheet.models import basics


app = typer.Typer()


@app.command()
def init():
    ...    


if __name__ == "__main__":
    app()