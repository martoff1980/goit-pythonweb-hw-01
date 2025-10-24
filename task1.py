import logging
from abc import ABC, abstractmethod

# Налаштування логування
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


# Абстрактний клас транспортного засобу
class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass


# Конкретні класи транспортних засобів
class Car(Vehicle):
    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Мотор заведено")


# Абстрактна фабрика
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass


# Фабрика для США
class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(f"{make} {model} (US Spec)")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, f"{make} {model} (US Spec)")


# Фабрика для Європи
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, f"{make} {model} (EU Spec)")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, f"{make} {model} (EU Spec)")


# Приклад використання
def main():
    # Використовуємо фабрику США
    us_factory = USVehicleFactory()
    vehicle1 = us_factory.create_car("Ford", "Mustang")
    vehicle1.start_engine()

    vehicle2 = us_factory.create_motorcycle("Harley-Davidson", "Street 750")
    vehicle2.start_engine()

    # Використовуємо фабрику ЄС
    eu_factory = EUVehicleFactory()
    vehicle3 = eu_factory.create_car("Volkswagen", "Golf")
    vehicle3.start_engine()

    vehicle4 = eu_factory.create_motorcycle("BMW", "R1250")
    vehicle4.start_engine()


if __name__ == "__main__":
    main()
