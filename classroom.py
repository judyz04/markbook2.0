from student import *
from teacher import *
from Person import *
from typing import List 

class Classroom:
    class_list = []

    def __init__(self, course_name: str, course_code: str, period: int, teacher: Teacher, class_list: List):
        '''init method of Teacher obj
            Args:
                course_name(str): the course name
                course_code(str): the course code
                period(int): the period in which the class is held in.  
                teacher(Teacher): the teacher of said class
            Return -> None
        '''
        self._course_name = course_name
        self._course_code = course_code
        self._period = period
        self._teacher = teacher

    @classmethod
    def add_student(cls, student: Student):
        '''add a student to the classroom list.
        Return -> None
        '''
        cls.class_list.append(student)

    @classmethod
    def remove_student(cls, student: Student):
        '''remove the student from the classroom list.
        Return -> None
        '''
        cls.class_list.remove(student)
    
    def get_course_name(self):
        '''get the name of the course
        Return -> str
        the course name
        '''
        return self._course_name
    
    def get_course_code(self):
        '''get the course code
        Return -> str
        the course code
        '''
        return self._course_code

    def get_period(self):
        '''get the period in which the class is held
           Return -> int
           period of class
        '''
        return self._period
    
    def set_period(self, new_time: int):
        '''set the name of teacher
        Args:
            new_time(int): the new period of the class.
        Return -> int
        the new period of the class
        '''
        assert type(new_time) is int, "The period can only be an int value."
        self._period = new_time
        return self._period

    def get_teacher(self):
        '''get the teacher of class
        Return -> str
        the teacher of the class
        '''
        return self._teacher

    def set_teacher(self, new_teacher: Teacher):
        '''set the teacher of the class
        Args:
            new_teacher(Teacher): the teacher of said class
        Return -> str
        the new teacher
        '''
        self._teacher = new_teacher
        return self._teacher

    

        