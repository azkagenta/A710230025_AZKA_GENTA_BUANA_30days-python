class Cow:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print("Moooo")

class Dog:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print("Bark Bark")

class Cat:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print("Meoooww")

my_cow = Cow("Sapi")
my_cow.sound()   # Output: Moooo

my_dog = Dog("Anjing")
my_dog.sound()   # Output: Bark Bark

my_cat = Cat("Kucing")
my_cat.sound()   # Output: Meoooww
