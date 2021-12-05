from src.repositories.CoffeePreparationRepository import CoffeePreparationRepository


class CoffeePreparationService:
    def __init__(self) -> None:
        self.coffeePreparationRepository = CoffeePreparationRepository()
        pass

    def get_all_coffee_preparations(self):
        coffee_preparations = self.coffeePreparationRepository.get_all()

        data = []
        for coffee_preparation in coffee_preparations:
            data.append([x for x in coffee_preparation])

        return data

    def get_last_coffee_preparation(self):
        coffee_preparation = self.coffeePreparationRepository.get_most_recent()

        data = [x for x in coffee_preparation]

        return data
