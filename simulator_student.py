from random import *
class Student:

    def __init__(self, name):

        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study!")
        self.progress += 0.12
        self.gladness -= 10

    def to_sleep(self):
            print("Finally some sleep!")
            self.gladness += 3

    def to_rest(self):
        print("Rest time!")
        self.progress -= 0.1
        self.gladness += 5

    def is_alive(self):

        if self.progress < - 0.5:
            print("Game over fr...")
            self.alive = False

        elif self.gladness < 0:
            print("Depression, huh?...")
            self.alive = False

        elif self.progress > 5:
            print("Too smart for that life...")
            self.alive = False

    def end_of_day(self, day):
        print("\n")
        print()
        print("-" * 20)
        print(f"Num of the day: {day}")
        print(f"Progress: {self.progress}")
        print(f"Gladness: {self.gladness}")
        print("-" * 20)
        print()
        print("\n")



    def live(self, day):

        live_cube = randint(1,3)
        # live_cube = int(input("Enter your choice 1 - study \n2 - sleep \n3 - rest"))

        if live_cube == 1:
            self.to_study()

        elif live_cube == 2:
                self.to_sleep()

        elif live_cube == 3:
            self.to_rest()

        self.end_of_day(day)
        self.is_alive()


student_Evelina = Student("Evelina")

for day in range(1,365):

    if student_Evelina.alive == False:
        break

    student_Evelina.live(day)
