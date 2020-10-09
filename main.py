from typing import List

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

        def __repr__(self):
            return f"Person({self.name}, {self.age})"

class Student:
    pass

class Teacher:
    pass

class Classroom:
    class_list = []

    def __init__(self, course_name: str, course_code: str, period: int, teacher: Teacher, class_list: List):
        self.course_name = course_name
        self.course_code = course_code
        self.period = period

    def add_student(cls, student: 'Student'):
        cls.class_list.append(student)
    
    def __repr__(self):
            return f"Student(Name: {self.name}, Age:{self.age})"
    


class Assignment:
    pass

