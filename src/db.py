import sqlite3

import click
from flask import g
from flask.cli import with_appcontext
from src.config.Configuration import Configuration


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            Configuration.getInstance().db.file,
            detect_types=sqlite3.PARSE_DECLTYPES,
            check_same_thread=False
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


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
