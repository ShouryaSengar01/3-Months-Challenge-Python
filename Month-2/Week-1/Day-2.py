       #Attributes(Variables)
class Car():
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

       #Methods(Functions)       
    def drive(self):
        print(f"Your Drive a {self.color} {self.model}")

    def stop(self):
        print(f"You stop a {self.model}")

    def describe(self):
        print(self.model, self.color, self.year)

#-----------------------------------------------------------------------

# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░      ⭐ OBJECT ⭐      ░░  => A "bundle" of related attributes(variables) and methods(functions). Ex. Phone, Cup, Book
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    You need a "Class" to create many objects.

# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░      ⭐ CLASS ⭐       ░░  => You can also call it a Blueprint Coz It's used to design the structure and layour of an object.
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    

from Objects_and_methods import Car

car1 = Car("Mustang", 2024, "Red", True)
car2 = Car("Corvette", 2022, "Yellow", True)
car3 = Car("Charger", 2025, "Black", False)

car1.drive()
