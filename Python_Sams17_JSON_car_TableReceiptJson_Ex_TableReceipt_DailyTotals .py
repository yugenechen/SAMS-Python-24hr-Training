'''
#  SAMS Python Chapter 17 (pp 183 - 196) Training snippets, Quiz and Excercise
#  "JSON files"
#
#**********************
# Course Training -
#**********************
#  a.  sys.path : provides a list of folders in the directory
#                 (i.e. parent folder)
#  b.  use __init__.py :  usualy an empty file that indicats to Python to
#                         search for [packages] in the diretory where this is
#                         located.  putthing this empty file in the folder
#                         tells Python that the folder is a [package] folder.
#
#  c. RULE:  DO NOT USE "-" dashes in filenames (use udnerscore "_" instead).
#                              Python reserves dashes for special meaning.
#  d. Having trouble with IMPORT <package> (especially custom ones)?
#     1.  Make sure the Python CurrentDiretory is where you expect it.
#     2.  Set the CurrentDirectory to where it should be (either your  project
#         or to the library folder.  Don't forget to change CWD back to the
#         project folder if you have changed it to the class library folder.
import os
currentDir = os.getcwd()
print("Current Working Dir: ", currentDir)
os.chdir("C:/Users/Lifygen/projects/python")
lastDir = currentDir
currentDir = os.getcwd()
print("Current Working Dir: ", currentDir)

#**********************
'''
# ===================================================
# Training on JSON files:
# the following is a SCRIPT, p185
import json
# Create a fileI/O stream object (a.k.a. IO_obj or file_obj)
f = open('car.json')
# Read the file into a variable
car = json.load(f)
# Show car object that is created (it is a <dict>!!!)
car
type(car)
# Show the <dict> keys
car.keys()
# Show contents of each key
car['mycar']
# Note:  car['mycar'] is also a <dict> child of the parent car <dict>
car['mycar'].keys()
type(car['mycar'])
car['mycar']['color']
car['mycar']['doors']
car['mycar']['make']
car['mycar']['model']
print("Calling all cars, be on the lookout for a {color}, " +
      "{door} door {make} {model} {transmission}.\n" +
      "Radio in if you spot it!!!"
      ).format(color=car['mycar']['color'],
               door=car['mycar']['doors'],
               make=car['mycar']['make'],
               model=car['mycar']['model'],
               transmission=car['mycar']['transmission']
               )
# Check out the car features:, another sub-dictionary
car['mycar']['features']
car['mycar']['features']['automatic_windows']
car['mycar']['features']["cruise_control"]
f.close()

# ---
# Read/Write JSON Files:
# Write: jsondmp(<json_dict>,<file_obj>) sends a JSON data stream.
# Read: jsondmps() - reads a JSON file and returns it as a string.
# ---
# Write:  Now change the color of the car to 'red', and save the file
# ---
car['mycar']['color'] = "red"
f = open('car.json', 'w')
json.dump(car, f)
f.close()
# Inspect the 'car.json' file & note it is all on one line.
# the formatting has been lost.
# Re-write the file with <indent> set to an integer value and reinspect
f = open('car.json', 'w')
json.dump(car, f, indent=2)
f.close()
# Yes, upon reinpsection of the json file it looks like good formatting
# ---
# Read: read the file into a string
# ---
# create the file_obj from the file
f = open('car.json', 'r')     # OR    f = open('car.json')
# Read the json contents into a variable, 'car'
car = json.load(f)

print(json.dumps(car, indent=2))
# see created:  "car.py"
from car import Car
mycar = Car(make="Ford",
            model="Explorer",
            transmission="automatic",
            color="red",
            doors=4,
            features={"stowaway_seats": True}
            )
vars(mycar)
import json
f = open('newcar.json', 'w')
json.dump(vars(mycar), f, indent=2)
f.close()
# see created:  "newcar.json"
# it contains a valid JSON for a car format but there is no named
# ojbect header or KEY.  Each car attribute is a key witht htem being
# assoicated with a 'car" key.
# Let's fix that:
#    Make a dictionary called newcar and place a "newCar" key in it
#    with the update method and vars() function:
newCar={}
newCar.update({'newCar':vars(mycar)})
f = open('newCar.json', 'w')
json.dump(newCar, f, indent=2)
f.close()

# Demonstrate class, multiple classes in a class file (pkg) and json handling.
# built a classroom.py in ~/classes containing <Classroom> and <Sudent>.
from classes.classroom import *
student1 = Student(name="Gene", grade="1")
student2 = Student(name="Chris", grade="1")
first_grade = Classroom(students=[student1,
                                  student2], room_number="B214")
print(vars(student1))
print(vars(student2))
print(vars(first_grade))
# first_grade looks off; let's look at it as a json:
import json
json.dumps(vars(first_grade))
# Json also has a problem converting it to text.

# *** INVESTIGATE ***
# Add a get_JSON_dict() method to the <Classroom> class.
# Review ~/classes/classroom.py,
# and try bulidng first_grade as a <classroom> again:
from classes.classroom import *
import classroom
student1 = Student(name="Gene", grade="1")
print(vars(student1))
student2 = Student(name="Chris", grade="1")
print(vars(student2))
first_grade = Classroom(students=[student1,
                                  student2
                                  ],
                        room_number="B214"
                        )
print(vars(first_grade))
print(first_grade.get_JSON_dict())
first_grade.get_JSON_dict()

#  Weird the system showed the get_JSON_dict() in the pop-up helper
#  but calling the method kept throwing an error:
#  attributeError: 'Classroom' object has no attribute 'get_JSON_dict'
#  even after importing as:
#      import classes.Classroom and
#      import Classroom
#      as well as the above with "from x import y" format
#  and I tried deleting the objects and classes from the 
#  Spyder Variable Explorer between each.
#  After creating (initializing) first_grade as a <Classroom>,
#  get_JSON_dict() can be called EXACTLY ONE TIME, after that it throws
#  an error!!!! (see below)
print(first_grade.get_JSON_dict())
# >>>{'students': [{'grade': '1', 'name': 'Gene'}, {'grade': '1', 'name': 'Chris'}], 'room_number': 'B214', 'd': {...}}

print(first_grade.get_JSON_dict())
# Out[]:>>>Traceback (most recent call last):
#
#  File "<ipython-input-33-e8fc526fdec8>", line 1, in <module>
#    print(first_grade.get_JSON_dict())
#
#  File "classes\classroom.py", line 40, in get_JSON_dict
#    d['students'] = student_list

#  TypeError: vars() argument must have __dict__ attribute
#
# The error is likely because the .students list format has changed!!!:
# *** .students list immediately after initialization ***
first_grade = Classroom(students=[student1,student2],room_number="B214")
first_grade.students
# Out[34]:>>>
# [<classes.classroom.Student at 0xbe54e48>,
#  <classes.classroom.Student at 0xbe54eb8>]

# *** .students list immediately after running .get_JSON_dict() ***
first_grade = Classroom(students=[student1,student2],room_number="B214")
first_grade.get_JSON_dict()
# Out[40]:>>>
# {'d': {...},
#  'room_number': 'B214',
#  'students': [{'grade': '1', 'name': 'Gene'}, {'grade': '1', 'name': 'Chris'}]}
first_grade.students
# Out[41]: [{'grade': '1', 'name': 'Gene'}, {'grade': '1', 'name': 'Chris'}]
#
# *** note how OUT[34] and OUT[41] differ in format.
student3 = Student(name="Barry", grade=12)
# Aha, there is no way to add "student3" without adding a new method.
# Should add methods:
#    1) Check for students format (JSON compatible or not) and restrict
#       use of get_JSON_dict() based on the reult.
#    2) Add an initialization check on the students datatype input. 
#       If done properly then get_JSON_dict() is not needed because the
#       the .AddStudent will handle proper formating and addition from
#       the initialization through future student adds.

first_grade = Classroom(students=[student1,student2],room_number="B214")
print(first_grade.get_JSON_dict())

first_grade = Classroom(students=[student1,student2],room_number="B214")
first_grade.get_JSON_dict()

first_grade = Classroom(students=[student1,student2],room_number="B214")
vars(first_grade)


import json
print(json.dumps(first_grade.get_JSON_dict(), indent=2))

# Python_Sams17_waiterReceipt.py


# ===================================================

# **********************
'''
# Questions (p 196):
'''
# 1) Why should you use a standardized format rater han a custom one?
#   [Answer]:  So others will know how to interpret the data and to ensure
#              other programers can re-use the data or framework without
#              reformatting it.
#
# 2) What is the difference between Json.dump() and Json.dumps()?
#   [Answer]:  jsondump(<json_dict>,<file_obj>) sends a JSON data stream.
#              jsondumps() - takes a JSON object and returns as a string.
#              The key difference is that -
#                  jsondump() creates a fileIO stream object allowing
#                             reading and writing to the fileIO through
#                             the fileIO stream.
#               while,
#                  jsondumps() converts a variable or json object to a
#                              string.
# 3)  What does vars() return?
#   [Answer]:  vars() returns all the attributes in a <dictionary> object.
'''
# ***********
# EXCERCISE (p 196):
# Excercise [1] Receipt script
#           The receipt script is not quote finished. Remember that the
#           the manager had been asking for a grand total for every day. Write
#           a functnion that provides the total for a given day.  The function
#           should accept a datetiem object for the given day and then return
#           a float containing the grand total for that day.  For this
#           excercise, you must -
#             a) figure out the name of the file,
#             b) import the  JSON, and then
#             c) total all the values within the file.
#
# ***********
'''
# [Answer]: This excercise is implemented in Python_Sams17_waiterReceipt.py:
#           get_receiptDailyTotal()   - gets a day's recept total from user
#                                       provideddate.
#           calc_dailyTotal(filename) - calculates day's receipt total receipts
#                                       in a file.
#           get_receipt_total(seats)  - calculates a table receipt total for a
#                                       given list of seats
#           mainReceipt()             - initiates the receipt colletion and
#                                       daily total retrieveal program.
#


# *** MAIN Program
# ===================================================
def main():
    print("Hello World!")

# ===================================================

if __name__ == "__main__":
    # [Test #1] Test the kitchen classes:  Ingredient(), Recipe(), Inventory()
    # from classes.ingredients import Ingredient
    # from classes.recipes import Recipe

    main()

