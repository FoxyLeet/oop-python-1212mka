class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Human info:"
            f"\nName - {self.name}"
            f"\nAge - {self.age}")

class Driver(Human):


        def __init__(self, name, age, driver_license_number):
            super().__init__(name, age)

            self.driver_license_number = driver_license_number

        def info1(self):
            print(f"Driver info:"
                  f"\nName - {self.name}"
                  f"\nAge - {self.age}"
                  f"\nDriver License number - {self.driver_license_number}")


nazar = Human("Nazar", 21)
nazar.info()

ruslan = Driver("Ruslan", 13, 52354)
ruslan.info1()