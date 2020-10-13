from main import *
from person import *

class Student:
    """
    attributes: name, grade, teacher & assignment.
    methods: get grade, show student's assignments, show student's teacher.
    """
    def __init__(self, first_name: str, last_name: str, grade: int, teacher: str, assignment: List[Assignment]) :
        """ 
        args:
                first_name(str): student's first name
                last_name(str): student's last name
                grade(int): student's grade
                teacher(str): student's teacher
                assignment(List[Assignment]): list of assignments student has
        Return -> None
        """
        