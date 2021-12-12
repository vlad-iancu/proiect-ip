from src.repositories.EnvironmentRepository import EnvironmentRepository


class EnvironmentService:
    def __init__(self) -> None:
        self.environmentRepository = EnvironmentRepository()

    def setTemperature(self, temp):
        new_temperature = self.environmentRepository.setTemperature(temp)
        return list(new_temperature)
