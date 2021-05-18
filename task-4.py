class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0
        self.is_police = False

    def go(self):
        print(f"Car {self.name} is now moving!")
        self.speed += 35

    def stop(self):
        print(f"Car {self.name} has stopped!")
        self.speed = 0

    def turn(self, direction):
        print(f"Car {self.name} has turned into direction {direction}!")

    def show_speed(self):
        print(f"Current {self.name} car speed is {self.speed}")


class TownCar(Car):
    speed_limit = 60

    def show_speed(self):
        print(f"Current {self.name} car speed is {self.speed}")
        if self.speed > self.speed_limit:
            print(f"Speed limit ({self.speed_limit}) exceeded!")


class SportCar(Car):
    def go(self):
        print(f"Car {self.name} is now moving super fast!")
        self.speed += 70


class WorkCar(Car):
    speed_limit = 40

    def show_speed(self):
        print(f"Current {self.name} car speed is {self.speed}")
        if self.speed > self.speed_limit:
            print(f"Speed limit ({self.speed_limit}) exceeded!")


class PoliceCar(Car):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0
        self.is_police = True

    def arrest(self, other_car: Car):
        print(f"{other_car.name} is arrested by {self.name}!")


car1 = TownCar("MiniCar", "White")
car1.show_speed()
car1.go()
car1.turn("left")
car1.go()
car1.show_speed()
car1.stop()

car2 = SportCar("Lamborghini", "Orange")
car2.go()
car2.turn("right")
for i in range(5):
    car2.go()
car2.show_speed()
car2.stop()

car3 = WorkCar("Taxi Cab", "Yellow")
car3.go()
car3.show_speed()
car3.turn("of client")
car3.go()
car3.show_speed()
car3.stop()
car3.show_speed()

car4 = PoliceCar("Police Car", "White/Blue")
car4.go()
car4.show_speed()
car4.go()
car4.turn("of Lamborghini car")
car4.go()
car4.show_speed()
if car4.is_police:
    print("This is the police! Everyone stop")
car4.stop()
car4.arrest(car2)
