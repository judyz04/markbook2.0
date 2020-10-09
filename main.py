class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class Student:
    pass

class Teacher:
    pass

class Classroom:
    def __init__(self, course_name: str, course_code: str, period: int, teacher: Teacher, student: Student):
        self.course_name = course_name
        self.course_code = course_code
        self.period = period
        self.teacher = teacher
        self.student = student

class Assignment:
    pass

