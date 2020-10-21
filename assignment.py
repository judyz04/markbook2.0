from main import *


class Assignment:
    
    def __init__(self, name:str, info:str, classroom:Classroom):
        self.name = name
        self.info = info
        self.classroom = classroom
               
    def assign_assignment(self, student:Student):
        student.assignments.append(self)
        
    def get_info(self):
        print(self.name)
        print('一一一一一一一一一一一一一')
        print(self.info)
        
    def mark(self, student:Student, mark:float):
        pass
