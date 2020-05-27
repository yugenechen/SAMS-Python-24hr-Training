#  SAMS Python Chapter 11 (p 122) Quiz and Excercise
'''
# Course Training -
  Note:  'object' is passsed into a custom class.  This is becuase it is the
         basis of ALL objects (if you declare it that way).  It is a built-in
         object class provided within Python so your new Class can inherit the
         properties and methods of Python's object().
         
         If you wanted <Student> to inherit <person> then you could pass 
         'person' into Student upon class declaration:  
                 def Student(person)
         Student would then inherit both person() and object() properties and 
         methods because person was built upon object and then Student was built
         upon person.


#  1] Creating a basic Class
'''
class person(object):
    #These are defined objet attributes or properties
    age = 27
    birth = '02/23/1993'
    expire = '?'
    ping = "Hello! :)"

    #This is an object method utilizing the .age property
    def print_a(self):
        print "Hello! I am {} years old".format(self.age)

# 2]  Utlizing "__init__() funciton
#  When a new class instance is created, Python cheks to see if an __init__()
#  function.  If so, the __init__() function is run first.

class Student(object):
              def __init__(self):
                  self.name = "None"
                  self.grade = "K"
                  self.distirct = "Orange County"

studentA= Student()
studentA.name


# Questions:

# 1) How do you create a new instance of a class?
#   [Answer]:  Delcare a new class using the "Class" keyword passing <object>
#              is optional.  
#              Class delcaration example:
#              Class newClass(object):
#                    #Declare attributes here
#                    attribute1 = "some_data_as_default"
#                    attribute 2 = 1
#                    #Declare methods here
#                    def Show_attribute1(self.attribute1):
#                        print "Attribute1 = {}".format(self.attribute1)

#              Instantiate a new object of a class by declaring a <new variable
#              name> = <class>().
#              Instantation example:
#              new_Object_instance = newClass()
#

# 2) How do you call a class's method? How do you get the value out of an
#    attirbute?
#   [Answer]:  a. Call a class method by stating the
#                 instantiated objects name dot the object's method.
#              example class method call:
#              new_Object_instance.show_attribute1()
#
#              b. Get a class attribute by stating the
#                 instantiated objects name dot the object's attribute name.
#              example get class attribute:
#              new_Object_instance.attribute1
#

# 3) Why do we use self in a class?
#   [Answer]: Unambiguous way to refer to itself when defining the class since
#             the instantiated name is not yet known.
#

# 4) What method is called when a new instance is created"
#   [Answer]:  The __init__() method is automatically called and exeucted
#              (if it exists).
#


#***********
# EXCERCISE:
#***********
  
#1) Exmaine the Student list code exmaple and notice that there is only error
#   checking if the user inputs data through raw_input().  A student object can
#   created with bad data if the user sends bad data through the parameters!
#   Add code so that the grade is checked no matter how __ini__() gets that
#   value.
#  See p.117 student.py and p.118 python ch12_student2.py
#  Extra Credit:
#  1.  Determine the maximum number of characters in the longest student name
#      and use that value to generate the student record separator.

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
            
        
# ######################
#SAMS Python chapter 11:  main program
# ######################

def main(test=2):
    #modified to run a different test scenario depending on user input

    if (test==1):
    # student.py Tester
        student1= Student()
        student2 = Student(name="Yuge Chen", grade='m', school = "Woodward")

        print "\n{} is student1's name".format(student1.name)
        student1.print_me()
        print "\nnext student:"
        print "{} is student2's name".format(student2.name)
        student2.print_me()
        print ("\n")

    elif (test==2):
    # ch12_student2.py Tester
        student1 = Student(name="Yuge Chen", grade='2', school = "Woodward")
        student2 = Student(name="Mary Nowosielski", grade='3', school = "Mercy")
        student3 = Student(name="Charlyn Chen", grade='K', school = "George Marks")
        students = [student1, student2, student3]
        print_roster(students)

                           
if __name__ == "__main__":
                       main(1)
                       #This can be used to override main() defaults when
                       # executing as a script using [F5] or
                       # using the menu [Run]->[Run Module]
                       #    changing to "main(1)" would run scenario 1
                       #    changing to "main(2)" would run scenario 2
                       #User entered values override this input and
                       #command line main() would run the default (without using this override)
                       

                       
        

        
    




























