class dog:
    def __init__(self, name, age):
        tail = "long"
        self.name = name
        self.age = age
    def get_description(self):
        return f"{self.name} is {self.age} years old"

    class shiba(dog):
        def __init__(self, name, age, breed):
            super().__init__(name, age)
            #ham khoi tao cua lop cha nhung nam trong lop con
            self.breed = breed
    