class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.bigSpacesAvailable = big
        self.mediumSpacesAvailable = medium
        self.smallSpacesAvailable = small

    def addCar(self, carType: int) -> bool:

        if carType == 1 and self.bigSpacesAvailable > 0:
            self.bigSpacesAvailable -= 1
            return True
        elif carType == 2 and self.mediumSpacesAvailable > 0:
            self.mediumSpacesAvailable -= 1
            return True
        elif carType == 3 and self.smallSpacesAvailable > 0:
            self.smallSpacesAvailable -= 1
            return True
        else:
            return False


obj = ParkingSystem(1, 1, 0)
print(obj.addCar(1))
print(obj.addCar(2))
print(obj.addCar(3))
print(obj.addCar(1))
