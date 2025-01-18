import random
class Student:
    def __init__(self, name):
        self.name = name
        self.roll_number = random.randint(1000, 9999)
        