from main import *
from person import *

class Student(Person):
     def __init__(self, name: str, age: int, student_number: int):
        super().__init__(name, age)
