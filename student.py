from main import *
from person import *

class Student:
    """"
    attributes: name, grade, teacher & assignment.
    methods: get grade, show student's assignments, show student's teacher.
    """
    def __init__(self, first_name: str, last_name: str, grade: int, teacher: str, assignments: List[Assignment]) :
        """
        args:
                first_name(str): student's first name
                last_name(str): student's last name
                grade(int): student's grade
                teacher(str): student's teacher
                assignment(List[Assignment]): list of assignments student has
        Return -> None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.teacher = teacher
        self.assignments = assignments
        
# METHODS
  
  def get_grade(self) -> int :
    """ 
    finds the student's grade
    Return -> int
    """
    return self.grade
        
  def get_assignments(self) -> List :
    """
    finds the student's assignments
    Return -> List[Assignment]
    """
    return self.assignments
    
  def get_teacher(self) -> str :
    """
    shows the student's teacher 
    Return -> str
    """
    return self.teacher