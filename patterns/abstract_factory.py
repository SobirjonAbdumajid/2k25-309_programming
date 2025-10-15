from abc import ABC, abstractmethod


class IEngine(ABC):
    @abstractmethod
    def release(self):
        pass


class ICar(ABC):
    @abstractmethod
    def release_car(self, engine: IEngine):
        pass


class IFactory(ABC):
    @abstractmethod
    def create_engine(self) -> IEngine:
        pass

    @abstractmethod
    def create_car(self) -> ICar:
        pass


class ChineseEngine(IEngine):
    def release(self):
        print("Releasing Chinese Engine")


class KoreanEngine(IEngine):
    def release(self):
        print("Releasing Korean Engine")


class ChineseCar(ICar):
    def release_car(self, engine: IEngine):
        engine.release()
        print("Releasing Chinese Car")


class KoreanCar(ICar):
    def release_car(self, engine: IEngine):
        engine.release()
        print("Releasing Korean Car")


class ChineseFactory(IFactory):
    def create_engine(self) -> IEngine:
        return ChineseEngine()

    def create_car(self) -> ICar:
        return ChineseCar()


class KoreanFactory(IFactory):
    def create_engine(self) -> IEngine:
        return KoreanEngine()

    def create_car(self) -> ICar:
        return KoreanCar()


if __name__ == "__main__":
    chinese_factory = ChineseFactory()
    chinese_engine = chinese_factory.create_engine()
    chinese_car = chinese_factory.create_car()
    chinese_car.release_car(chinese_engine)

    korean_factory = KoreanFactory()
    korean_engine = korean_factory.create_engine()
    korean_car = korean_factory.create_car()
    korean_car.release_car(korean_engine)
