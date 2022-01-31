from src.db import get_db


class EnvironmentRepository:

    def setTemperature(self, temp):
        db = get_db()
        db.execute(
            'INSERT INTO Temperature (value)'
            ' VALUES (?)',
            (temp,)
        )

        db.commit()

        temperature_check = get_db().execute(
            'SELECT id, timestamp, value' +
            ' FROM temperature' +
            ' ORDER BY timestamp DESC'
        ).fetchone()

        return temperature_check
