class Student:
    print("Hi")

    # метод ініціалізації
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def print_info(self):
        print(f"Im alive, my name is {self.name}")
        print(f"My height {self.height} cm \n")



student_Nazar = Student("Nazar", 174)
student_Nazar.print_info()

"""
height_Nazar = student_Nazar.height

print(f"height of Nazar: {height_Nazar}")
"""

student_Max = Student("Max", 190)
student_Max.print_info()