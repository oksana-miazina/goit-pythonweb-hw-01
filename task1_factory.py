import logging
from abc import ABC, abstractmethod
from typing import ClassVar

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    _SPEC: ClassVar[str] = "US Spec"

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, f"{model} ({self._SPEC})")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, f"{model} ({self._SPEC})")


class EUVehicleFactory(VehicleFactory):
    _SPEC: ClassVar[str] = "EU Spec"

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, f"{model} ({self._SPEC})")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, f"{model} ({self._SPEC})")


# Використання
if __name__ == "__main__":
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    us_vehicle1 = us_factory.create_car("Toyota", "Corolla")
    us_vehicle1.start_engine()

    us_vehicle2 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
    us_vehicle2.start_engine()

    eu_vehicle1 = eu_factory.create_car("Toyota", "Corolla")
    eu_vehicle1.start_engine()

    eu_vehicle2 = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
    eu_vehicle2.start_engine()
