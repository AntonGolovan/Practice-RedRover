class Car:

    def __init__(self, model, creation_year, engine_volume, price, mileage, numbers_wheel = 4):
        self.model = model
        self.creation_year = creation_year
        self.engine_volume = engine_volume
        self.price = price
        self.mileage = mileage
        self.numbers_wheel = numbers_wheel

    def description(self):
        description = (f"Модель автомобиля - {self.model}, год выпуска - {self.creation_year},"
                       f" пробег автомобиля - {self.mileage }",
                       f" объем двигателя - {self.engine_volume}",
                       f" стоимость автомобиля - {self.price}",
                       f" количество колес автомобиля - {self.numbers_wheel}"
                       )
        print(description)

class Trucks(Car):

    def __init__(self, model, creation_year, engine_volume, price, mileage, numbers_wheel = 8):
        super().__init__(model, creation_year, engine_volume, price, mileage, numbers_wheel)

        self.numbers_wheel = numbers_wheel

new_car = Car("BMW", "2010", "2.5", 5000, 50000)
new_car.description()

new_truck = Trucks("Камаз", "2000", "4.1", 6000, 100000)
new_truck.description()