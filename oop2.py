# класс учёта машин
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print("-"*40)
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: ({self.year})")

class Car(Vehicle):

    def __init__(self, brand, model, year,mileage):
        super().__init__(brand, model, year)
        self.mileage = mileage

    def update_mileage(self, new_mileage):
        if new_mileage < 0:
            raise ValueError("обновление километража не может быть отрицательным")
        self.mileage += new_mileage

    def info(self):
        super().info()
        print(f"mileage: {self.mileage}")


class Electric_car(Vehicle):
    def __init__(self,brand, model, year, battery_range):
        super().__init__(brand, model, year)
        self.battery_range = battery_range

    def info(self):
        super().info()
        print(f"запас хода: {self.battery_range}км.")


car1 = Car("ford", "mustang", 2023,6)
car1.info()
car2 = Electric_car("Tesla", "Model S", 2024, 340)
car2.info()

