import sqlite3

import click
from flask.cli import with_appcontext
from src.config.Configuration import Configuration

db = None


def get_db():
    global db
    if db is None:
        db = sqlite3.connect(
            Configuration.getInstance().db.file,
            detect_types=sqlite3.PARSE_DECLTYPES,
            check_same_thread=False
        )
        db.row_factory = sqlite3.Row

    return db


def close_db(e=None):
    global db
    if db is not None:
        db.close()
        db = None


def init_db():
    db = get_db()

    with open('schema.sql', encoding='utf8') as schema_file:
        db.executescript(schema_file.read())

    with open('data.sql', encoding='utf8') as data_file:
        db.executescript(data_file.read())


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
