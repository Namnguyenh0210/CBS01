from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    

    def sleep(self):
        print("The animal is sleeping.")


class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"


dog = Dog()
cat = Cat()


print(dog.sound())  
print(cat.sound())  
dog.sleep()

       









       