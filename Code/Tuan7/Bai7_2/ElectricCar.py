from Car import Car
class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size
    def description(self):
        return super().description() + f" Battery : {self.battery_size}|"