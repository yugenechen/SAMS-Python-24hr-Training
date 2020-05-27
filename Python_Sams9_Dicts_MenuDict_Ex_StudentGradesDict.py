#  SAMS Python Chapter 9 (p 101) Quiz and Excercise

# Questions:

# 1) What pairs do you store in dictionaries?
#   [Answer]:  Key and values.  {'key':'value'}

# 2) Which of the following is true?
#     [Evaluate Statement for True/False]                    [Answer]
#       --------------------------------               ---------------------
#    a. Keys are always unique.                         TRUE
#    b. Values are always unique.                       FALSE
#    c. Both keys and values must be unique.            FALSE
#    d. Neither keys nor values have to be unique       FALSE

# 3) How do you get all the keys out of a dictionary?
#   [Answer]: <dictionary>.values() returns all the values in a dictionary and
#             <dictionary>.keys() returns all the keys in a dictionary.

# 4) How do you store a new value in a dictionary?
#   [Answer]:  use format of:
#              dictionary["new_key"] = value_at_the_key

#***********
# EXCERCISE:
#***********
  
# Make use of the "if __name__ == "__main__": main()" technique
# that allows this file to run as a script.
#   See last line of this doc.  
# ****************
#1) Create a program that pairs a student's name to his class grade. The user
#   should be able to enter as many students as needed and then get a printout
#   of all the students' names and grades.
#   Sample output/input should be similar to the following:
#   >>>Please give me the name of the student (q to quit): [INPUT]
#   >>>Please give me their grade: [INPUT]
#      [AND SO ON...]
#   >>>Please give me the name of hte student (q to quit): q
#   >>>Okay, printing grades!
#   >>>Student    Grade
#   >>>Student1    A
#   >>>Student2    D
#      [AND SO ON...]
     
#   Criteria: I wrote for planning
#   1.  User enters as many students as needed
#   2.  User enters a class grade associated with the student.
#   3.  Program associates student name with class grade.
#   4.  Quit option then prints out the list of
#       Student Names and associated grade for each.


def main():
    classList = {}
    name = ""
    validQuit = ['q', '"q"', "'q'"]
    #Do not check for upper case "Q" so it can be used as a name
    
    print "Welcome to student and class grade storage program."
    print "Enter the student names and grades.  A full list of names and grades is printed upon exit."
    
    while not(name in validQuit):
        name = raw_input("Enter a student name in 'First_Name Last_Name' format\n:")
        if not(name.replace(" ", "").replace("-","").replace('"', "").replace("'","").isalpha()):
            print "Invalid input, try again" 
            continue
        elif (name in validQuit):
            print "Entries complete; see Students and Grades below:"
            show_Students_and_Grades(classList)
            break
        else:
            getGrades(name, classList)
            
def getGrades(name, classList, grade=" "):
    validGrade = ['A+', 'A', 'B', 'C', 'D', 'F']

    while not(grade in validGrade):
        grade = raw_input("Enter " + name + "'s class grade " + str(validGrade).replace("'","") + ":")
        if (grade.replace('"',"").replace("'","").upper() in validGrade):
            grade = grade.replace('"',"").replace("'","").upper()
            classList[name] = grade
            return
        print "Invalid entry, Try Again."

def show_Students_and_Grades(classList):
    students = classList.keys()
    s_label = " Student Name"
    #max() is iterable:  max(iterable [, key=f(iterable])
    #max() using internal loop: max([f(x) for x in ListVariable])
    # len(max(students, key=len)) #returns the length of the longest student name
    maxLength = max(max([len(student) for student in students]),len(s_label))
    print "max using iterable : " + str(maxLength)
    print len(max(students, key=len))
    wrapper =  "[" + "*"*(maxLength + len("  Grade")) + "]"
    print wrapper
    print s_label + " " * (maxLength - len(s_label)) + 3*" " + "Grade"
    print " " + "-"*(maxLength) + "  " + "-"*len("Grade")

    for student in classList:
        print " " + student + " "*(maxLength - len(student) + 4) + classList[student]         

    print wrapper


if __name__ == "__main__":
    main()





#"".join([cypher.get(ch, ch) for ch in myText])




























