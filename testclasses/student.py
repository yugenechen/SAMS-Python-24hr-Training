# ######################
#SAMS Python chapter 11:  student.py
# ######################
class Student(object):
    #Always use <self> and <attr> that you want to initialize as attributes
    #in the __init__().
    def __init__(self,
                 name="",
                 school="",
                 grade="",
                 ):
        if not name:
            name = raw_input("what is the student's name?")
        if not school:
            school = raw_input("What is the {}'s school?").format(name)

#    #Original student.py code:
#        if not grade:
#            grade = raw_input("What is the student's grade?")

        self.name = name
        self.school = school
        self.grade = grade
#       #New Code     ****************************
        #Check to see if self.grade is valid and assign it as appropriate
        self.get_grade()
#       #End New Code ****************************        
#    #Original student.py code:
#    def get_grade(self):
#        while True:
#            grade = raw_input("What is the student's grade? [K, 1-5]: ")
#            if grade.lower() not in ['k', '1', '2', '3', '4', '5']:
#                print ("I'm sorry, but {} isn't valid. Please try again."\
#                       .format(grade)
#                       )
#            else:
#                return grade
#   #New Code    ****************************
    #Always check <grade> for valid input and solicit input if invalid
    def get_grade(self):
        while (self.grade.lower() not in ['k', '1', '2', '3', '4', '5']):
            if self.grade:
                print ("I'm sorry, but <{}'s> grade of <{}> isn't valid. Please try again."\
                       .format(self.name, self.grade)
                       )
            self.grade = raw_input("What is <{}'s> grade? [K, 1-5]: ".format(self.name))            
#       #End New Code ****************************        

    def print_me(self):
        print "Name: {}".format(self.name)
        print "School: {}".format(self.school)
        print "Grade: {}".format(self.grade)                                

    # ######################
    #SAMS Python chapter 11:  ch12_student2.py
    # ######################
    #  Same as student.py with print_roster() fucntion added.
    #  (i.e. this is an independent function and not a a method of Student Class
    #
    #  print_roster() prints all students in the system to the screen.

    def print_roster(students):
    #<students> arguement is expected to be a list of students
        print "Students in the system:"
        #********
        #Added as part of the Excercise to enhane the code.
        # len(max(students, key=len)) #is the same function as the following
        #     but only works if <students> is a list of names.
        #     In this case <students> is a list of objects of class type "Student"
        #     so, student.name exists but s.
        # but it is more readable to [for me] to  show it as a loop:
        maxStudentName = max([len(student.name) for student in students])\
                     +len("Name: ")
        recordSeparator = "*" * maxStudentName
        #********
        for student in students:
            print recordSeparator
            student.print_me()
        print recordSeparator
            
