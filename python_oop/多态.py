class Animal:
    def speak(self):
        print("叫叫叫")

class Dog:
    def speak(self):
        print("wang")

class Cat:
    def speak(self):
        print("喵")


animal = Animal()
dog = Dog()
cat = Cat()

def sp(x):
    x.speak()

sp(animal)
sp(dog)
sp(cat)