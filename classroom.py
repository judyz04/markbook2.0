from main import *

class Classroom:
    class_list = []

    def __init__(self, course_name: str, course_code: str, period: int, teacher: object, class_list: List):
        self.course_name = course_name
        self.course_code = course_code
        self.period = period

    @classmethod
    def add_student(cls, student: 'Student'):
        cls.class_list.append(student)
    
    def __repr__(self):
            return f"Student(Name: {self.name}, Age:{self.age})"