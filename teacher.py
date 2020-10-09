from main import *
import copy

#REQUIRMENTS & ISSUES:
#classroom object
#a method to print a brief discription of a classroom (__repr__ or __str__)
#a static method to create a classroom: Classroom.create_classroom(*args)
#a self method to get a dict of attributs if certain classroom: obj.get_self_date()
#a method to enter the menu of a classroom: obj.show()
#a set_parent method of classroom: obj.set_parent(self)
#the parent menu(object) (can be access from where), a method to enter that menu: parent.show()

#INTERFACE FROM OUTSIDE:
#see Teacher doc strings

class Teacher:
    '''Public Attributes: -
        Static Attributes: PARENT, TEACHER_LIST
        Self Methods: get_name, get_self_date, set_name, get_classrooms, add_classroom, del_classroom, del_teacher, set_parent, show
        Public Static Methods: get_all_teacher, create_teacher, get_data, print_header, print_line

        =>To access the menu of a teacher, use obj.show()  example: show_teacher = Teacher('', '', []).show()

        =>To create a teacher, use the static mehod create_teacher

        =>To get all teachers' information, use the static method get_all_teacher

        =>The object contents a __repr__ method to print out a brief profile

        =>To save data, call static method get_data to get a json data string

        =>To reset the parent call class method set_parent

        Private Attributes: __last_name, __first_name, __classroom, __parent
        Private Methods: __access_classroom
    '''

    PARENT = None #the last menu's object for example: Classroom
    TEACHER_LIST = []#A list includes all teacher obj

    def __init__(self, last_name: str, first_name: str, classrooms: List[object]) -> None:
        '''init method of Teacher obj
            Args:
                last_name(str): teacher's last name
                first_name(str): teacher's first name
                classrooms(List[Classroom]): a list that contents all Classroom objects the tacher can access
            Return -> None
        '''
        self.__last_name = last_name
        self.__first_name = first_name
        self.__classrooms = classrooms
        self.__parent = self.PARENT

        Teacher.TEACHER_LIST.append(self)
    
    def __repr__(self):
        return f'{self.__first_name} {self.__last_name}'

    def get_name(self) -> str:
        '''get the name of teacher
        Return -> str:
            teacher's full name
        '''
        return f'{self.__first_name} {self.__last_name}'
    
    def set_name(self, last_name, first_name) -> None:
        '''set the name of teacher
        Args:
            last_name(str): teacher's last name
            first_name(str): teacher's first name
        Return -> None
        '''
        self.__last_name, self.__first_name = last_name, first_name

    def get_classrooms(self) -> List:
        '''get the classroom list
        Return -> List[Classroom]
        '''
        return self.__classrooms

    def add_classroom(self, classroom: object) -> None:
        '''add a classroom the teacher's classroom list
        Return -> None
        '''
        self.__classrooms.append(classroom)
    
    def access_classroom(self, classroom: object) -> object:
        '''access the classroom using the method in Classroom
        Return -> function obj
        '''
        if classroom in self.__classrooms:
            return None#waiting for connector to next position
    
    def del_classroom(self, classroom: object) -> None:
        '''remove a classroom from the classroom list
        '''
        if classroom in self.__classrooms:
            self.__classrooms.remove(classroom)
    
    @staticmethod
    def create_teacher(first_name: str, last_name: str, classrooms: List[object]=[]) -> object:
        '''create a teacher object
                 Args:
                last_name(str): teacher's last name
                first_name(str): teacher's first name
                classrooms(List[Classroom]=[]): a list that contents all Classroom objects the tacher can access
            Return -> Teacher obj
        '''
        teacher = Teacher(last_name, first_name, classrooms)
        Teacher.TEACHER_LIST.append(teacher)

        return teacher

    @staticmethod
    def get_all_teacher() -> List(object):
        '''get all Teacher object in a list
            Return -> List[Teacher]
        '''

        return Teacher.TEACHER_LIST
    
    @staticmethod
    def get_data() -> List:
        '''get a list of dicts in json format. Use to save files
            Return -> List (json)
        '''
        list = []
        for teacher in Teacher.TEACHER_LIST:
            dict = teacher.get_self_date()
            list.append(dict)

        json_data = json.dumps(list, indent=4)

        return list

    def get_self_date(self) -> dict:
        '''get a dictionary of this object attributes
        Return -> dict:
            {
                'last_name': self.last_name,
                'first_name': self.first_name,
                'classrooms':[]
            }
        '''
        dict = {
                'last_name': self.last_name,
                'first_name': self.first_name,
                'classrooms':[]
            }
        for classroom in self.get_classrooms():
            dict['classrooms'].append(classroom.get_self_date)#wait for completion

        return dict

    def del_teacher(self) -> None:
        '''completely remove object
        Return -> None
        '''
        Teacher.TEACHER_LIST.remove(self)
        del self

    
    #Two staticmethod to print lines
    @staticmethod
    def print_header(string: str) -> str:
        return '{:=^40}'.format(string)
    @staticmethod  
    def print_line(string: str) -> str:
        return '{:-^40}'.format(string)   
    
    def set_parent(self, parent) -> None:
        #set the parent Menu of class Teacher
        self.__parent = parent
    

    def show(self) -> object:
        #show everything, need the connectors from other classes
        print('\n'*10)
        Teacher.print_header(f'{self.get_name()}')
        Teacher.print_line(f'Profile')
        print(f'Last Name: {self.__last_name}\nFirst_name: {self.__first_name}')
        Teacher.print_line('Classrooms')
        for index, classroom in enumerate(self.__classrooms):
            #print(f'[{index}] {classroom}') still wait for connector
            pass
        print(f'[{len(self.__classrooms)}] to add a new classroom')
        print(f'[{len(self.__classrooms)+1}] to remove a classroom')
        print(f'[{len(self.__classrooms)+2}] reset the name of teacher')
        print(f'[{len(self.__classrooms)+3}] back to last menu')
        print()

        while True:#get input                
            result = input(f'type the index[0-{len(self.__classrooms)+2}]')

            try:
                result = int(result)
            except:
                print('invalid input')
                continue

            if 0 <= result < len(self.__classrooms):#enter
                self.__classrooms[result].set_parent(self)
                return self.access_classroom(self.__classrooms[result])

            elif 0 == len(self.__classrooms):#add
                #waiting for classroom object, add one exist classroom or create a new classroom
                pass

            elif 0 == len(self.__classrooms)+1:#remove
                Teacher.print_line('choose the classroom to remove')
                for index, classroom in enumerate(self.__classrooms):
                    #print(f'[{index}] {classroom}') still wait for connector
                    pass
                print(f'[{len(self.__classrooms)+2}] back to last menu')
                while True:
                    result = input(f'type the index[0-{len(self.__classrooms)-1}]')
                    try:
                        result = int(result)
                    except:
                        print('invalid input')
                        continue

                    if 0 <= result < len(self.__classrooms):#remove
                        return self.del_classroom(self.__classrooms.index[result])
                    
                    elif result == len(self.__classrooms):#back
                        return self.show()
                
            elif result == len(self.__classrooms)+2:#setname
                while True:
                    first_name = input(f'enter the first name')
                    last_name = input(f'enter the last name')
                    assurance = input(f'the new name is {first_name}{last_name}. are your sure?[y/n]')
                    if assurance == 'y':
                        self.set_name(last_name, first_name)
                        return show()
                    elif assurance == 'n':
                        return show()
                    else:
                        print('invalid input')
                        continue

            elif result == len(self.__classrooms)+3:#back
                return self.__parent.show()

            else:
                print('invalid input')
                continue
