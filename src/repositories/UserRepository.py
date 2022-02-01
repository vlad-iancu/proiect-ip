from werkzeug.security import generate_password_hash
from src.db import get_db


class UserRepository:
    def add(self, username, password):
        try:
            get_db().execute(
                "INSERT INTO User (username, password) VALUES (?, ?)",
                (username, generate_password_hash(password)),
            )
            get_db().commit()
            return 0

        except get_db().IntegrityError:
            return -1

    def getByUsername(self, username):
        user = get_db().execute(
            'SELECT * FROM User WHERE username = ?', (username,)
        ).fetchone()

        return user

    def getById(self, user_id):
        user = get_db().execute(
            'SELECT * FROM User WHERE id = ?', (user_id,)
        ).fetchone()

        return user
