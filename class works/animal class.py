class Animal:
    def __init__(self, name, weight, age, color_fur, breed):
        self.weight = weight
        self.name = name
        self.age = age
        self.color_fur = color_fur
        self.breed = breed

    def info(self):
        print(f"Pet info:"
            f"\nName: {self.name}"
            f"\nHeight: {self.weight}"
            f"\nAge: {self.age}"
            f"\nColor hair: {self.color_fur}"
            f"\nBreed: {self.breed}")

class Dog(Animal):
    def __init__(self, name, weight, age, color_fur, breed, sound1):
        super().__init__(name, weight, age, color_fur, breed)

        self.breed = "Sharpei"
        self.sound1 = "Woof"

    def info(self):
        super().info()
        print(f"Dog info:"
              f"\nBreed: {self.breed}"
              f"\nSound: {self.sound1}")

class Cat(Animal):
    def __init__(self, name, weight, age, color_fur, breed, sound2):
        super().__init__(name, weight, age, color_fur, breed)

        self.breed = "Sokoke"
        self.sound2 = "Meow"

    def info(self):
        super().info()
        print(f"Cat info:"
              f"\nBreed: {self.breed}"
              f"\nSound: {self.sound2}")


Daisy = Dog("Daisy", 20, 3, "Black", "Sharpei", "Woof")
Daisy.info()

maksimka = Cat("Maksimka", 5, 7, "Brown", "Sokoke", "Meow")
maksimka.info()