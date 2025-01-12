#tinh da hinh
class dog:
    def sound(self):
        return "bark"
class cat:
    def sound(self):
        return "meow"
class bird: 
    def sound(self):
        return "chirp"  
         


def animal_sounds(animals):
    print(animal.sound())


animals = [dog(), cat(), bird()]
for animal in animals:
    animal_sounds(animal)

    


 

