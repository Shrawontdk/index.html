class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0

    def get_speed(self):
        return self.speed

# Create instances (objects) of the Car class
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Accord", 2021)

# Use object methods to interact with the objects
car1.accelerate()
car1.accelerate()
car1.accelerate()
car1.brake()
car2.accelerate()
car2.accelerate()

# Get the current speed of each car
print(f"{car1.make} {car1.model} speed: {car1.get_speed()} km/h")
print(f"{car2.make} {car2.model} speed: {car2.get_speed()} km/h")