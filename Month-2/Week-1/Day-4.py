# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░     ⭐ INHERITANCE ⭐     ░░  => Allows a class to inherit attributes and methods from another class. Helps with Code reusability and extensibility.
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    Just like how a Child can inherit from his parents. format=> class Child(Parent)

class Animal():
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")

    
class Dog(Animal):
    def speak(self):
        print("WOOF!!")

class Cat(Animal):
    def speak(self):
        print("MEOW!!")


class Mouse(Animal):
    def speak(self):
        print("SQUEAK!!")

dog = Dog("Alex")
cat = Cat("Olive") 
mouse = Mouse("Alferd")


mouse.speak()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░    ⭐ MULTIPLE INHERITANCE ⭐    ░░  => Inherit from multiple Parent Classes.
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    C(B, A)

# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░    ⭐ MULTILEVEL INHERITANCE ⭐     ░░  => Inherit from a parent which inherits from another parent.
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    C(B) <- B(A) <- A


class Animal():
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is Sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is Hunting")

class Rabbit(Prey):              #Mutilevel inheritance coz "class rabbit" is taking from "class Prey" and "class Prey" is taking from "class Animal"
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):   #Multiple Inheritance
    pass

rabbit = Rabbit("Chimmy")
hawk = Hawk("Giyu")
fish = Fish("Blue")

rabbit.flee()
hawk.hunt()
fish.hunt()
fish.eat()
rabbit.eat()
hawk.eat()
rabbit.sleep()
