from Vehicle import Verhicle
from Car import Car
from ElectricCar import ElectricCar
def main():
    vc1 = Verhicle("HONDA")
    print(vc1.description())
    c1 = Car("TOYOTA","RTX98")
    print(c1.description())
    ce1 = ElectricCar("YAMAHA","GGD12",50000)
    print(ce1.description())
if __name__ =="__main__":
    main()