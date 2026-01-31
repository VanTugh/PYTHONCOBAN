from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def __init__(self, seats):
        self.seats = seats
    def start_engine(self):
        if self.seats > 0 and self.seats <= 4:
            print("Car engine started.")
        else:
            print("Invalid number of seats for a car.")
    def stop_engine(self):
        if self.seats < 0 or self.seats > 4:
            print("Invalid number of seats for a car.")
    def drive(self):
        if self.seats > 0 and self.seats <= 4:
            print("Car is driving.")
        else:
            print("Invalid number of seats for a car.")
class Motorcycle(Vehicle):
    def __init__(self, fuel):
        self.fuel = fuel
    def start_engine(self):
        if self.fuel > 0:
            print("Motorcycle engine started.")
        else:
            print("Not enough fuel to start the motorcycle.")   
    def stop_engine(self):
        if self.fuel <= 0:
            print("Not enough fuel to start the motorcycle.")
    def drive(self):
        if self.fuel > 0:
            print("Motorcycle is driving.")
        else:
            print("Not enough fuel to start the motorcycle.")
def main():
    car = Car(4)
    car.start_engine()
    car.drive()
    car.stop_engine()

    motorcycle = Motorcycle(5)
    motorcycle.start_engine()
    motorcycle.drive()
    motorcycle.stop_engine()
if __name__ == "__main__":
    main()