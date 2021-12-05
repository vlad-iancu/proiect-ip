from src.db import get_db


class CoffeePreparationRepository:

    def __init__(self) -> None:
        pass

    def get_all():
        coffee_preparations = get_db().execute(
            'SELECT * FROM coffeepreparation ORDER BY finished_at DESC').fetchall()

        return coffee_preparations

    def get_most_recent():
        coffee_preparation = get_db().execute(
            'SELECT * FROM coffeepreparation ORDER BY finished_at DESC LIMIT 1').fetchone()

        return coffee_preparation
