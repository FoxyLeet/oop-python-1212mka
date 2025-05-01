class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Human info:"
            f"\nName: {self.name}"
            f"\nAge: {self.age}")

class Driver(Human):


        def __init__(self, name,age, driver_license_number):
            super().__init__(name,age, driver_license_number)

            self.driver_license_number = driver_license_number

        def info(self):
            super().info()
            print(f"Driver info:"
                  f"\nSalary: {self.driver_license_number}")


nazar = Human("Nazar", 175)
nazar.info()

ruslan = Driver("Ruslan", 180, 52354)
ruslan.info()