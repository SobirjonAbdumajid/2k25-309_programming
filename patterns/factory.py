# # from abc import ABC, abstractmethod
# #
# # class ToyABC(ABC):
# #     @abstractmethod
# #     def play(self):
# #         pass
# #
# # class Car(ToyABC):
# #     def play(self):
# #         print("Car playing")
# #
# # class Doll(ToyABC):
# #     def play(self):
# #         print("Doll playing")
# #
# # class ToyFactory:
# #     @staticmethod
# #     def create_toy(toy: str) -> Car | Doll | None:
# #         if toy == "car":
# #             return Car()
# #         elif toy == "doll":
# #             return Doll()
# #         return None
# #
# # if __name__ == "__main__":
# #     toy1 = ToyFactory.create_toy("car")
# #     toy1.play()
# #
# #     toy2 = ToyFactory.create_toy("doll")
# #     toy2.play()
# #
# #     toy3 = ToyFactory.create_toy("roll")
# #     toy3.play()
#
#
# from abc import ABC, abstractmethod
#
#
# class ToyABC(ABC):
#     @abstractmethod
#     def create(self):
#         pass
#
#
# class Car(ToyABC):
#     def create(self):
#         print("Creating a car")
#
#
# class Doll(ToyABC):
#     def create(self):
#         print("Creating a doll")
#
#
# class ToyFactoryABC(ABC):
#     @abstractmethod
#     def build_toy(self) -> ToyABC:
#         pass
#
#     def build(self) -> str:
#         toy = self.build_toy()
#         return f"ToyFactory: {toy.create()}"
#
#
# class CarFactory(ToyFactoryABC):
#     def build_toy(self):
#         return Car()
#
#
# class DollFactory(ToyFactoryABC):
#     def build_toy(self):
#         return Doll()
#
#
# if __name__ == "__main__":
#     car = CarFactory()
#     car.build()
#     doll = DollFactory()
#     doll.build()

from abc import ABC, abstractmethod


class ToyABC(ABC):
    @abstractmethod
    def create(self):
        pass


class Car(ToyABC):
    def create(self):
        print("Creating a car")


class Doll(ToyABC):
    def create(self):
        print("Creating a doll")


class ToyFactoryABC(ABC):
    @abstractmethod
    def build_toy(self) -> ToyABC:
        pass

    def build(self) -> str:
        toy = self.build_toy()
        return f"ToyFactory: {toy.create()}"


class CarFactory(ToyFactoryABC):
    def build_toy(self):
        return Car()


class DollFactory(ToyFactoryABC):
    def build_toy(self):
        return Doll()


if __name__ == "__main__":
    car = CarFactory()
    car.build()
    doll = DollFactory()
    doll.build()
