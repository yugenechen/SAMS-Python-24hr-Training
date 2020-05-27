'''
#  SAMS Python Chapter 18 (pp 197 - 208) Training snippets, Quiz and Excercise
#  "Database and SQL (SQL Lite)"
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
# Training on SQLite database files:
# the following is a SCRIPT, p 200

# Python_Sams18_SQL.py
#

'''********************************************
   # Goal/Lesson: #1] Create an SQLite database
   ********************************************'''
def ch18Lesson1():
    '''
    Python_Sams18, p 199  |  Creating a Database

    Write data into the SQL database:  'mytest.db'
    that was created in Lesson#1.

    Created on Tue May 12 18:04:12 2020
    @author: Lifygen
    '''
    # Create an SQLite database
    import sqlite3
    # Open an SQLite connection; this creates the database identified in quotes
    conn = sqlite3.connect('mytest.db')
    # create a cursor, that is used to move around the database, execute SQL
    # statements, and get data. (I like to think of it as a pointer or 'ptr')
    ptr = conn.cursor()
    # The following 'sql' variable is an sql statement broken out over several
    # lines.  So, NO, it is NOT a comment.
    # YES, it is an SQL command to create a DB.
    # This creates a table called students with three columns labelled as shown
    #  with data expected as shown:
    sql = '''create table students (
        name text,
        username text,
        id int)'''
    # cursor.execute(<sql statement>) executes the sql statemetn or command
    ptr.execute(sql)
    # closes the connection tothe DB (akin to closing a file connection)
    ptr.close()


'''**********************************************
   # Goal/Lesson: #2] Write to an SQLite database
   **********************************************'''
def ch18Lesson2():
    '''
    Python_Sams18, p 202  |  Adding Data

    Write data into the SQL database:  'mytest.db' that was created in
    Lesson#1.

    Created on Tue May 12 18:04:12 2020
    @author: Lifygen
    '''
    # Add Students into the SQLite database: 'mytest.db'
    import sqlite3
    # open SQLite connection - to database created in Lesson 1
    conn = sqlite3.connect('mytest.db')
    ptr = conn.cursor()

    print("Let's add students to the SQLite database!")
    addNames = True
    while addNames:
        name = input("Student's name: ")
        username = input("Student's username: ")
        id_num = input("Student's id number: ")
        # Insert consists of 3 things:
        # 1) Table to insert into:  students
        # 2) Columns getting data:  (name, username, id)
        # 3) the data values:  (:st_name, :st_username, :id_num)
        # Note: the data uses 'named parameters" <:stringName> where the
        #      stringName is a string w/o using quote marks but is referenced
        #      again with quote marks in the "ptr.execute" statement.
        sql = '''insert into students
                   (name, username, id)
                   values
                       (:st_name, :st_username, :id_num)'''
        # Note: NO WHITESPACE should be after the colon;
        #      [SQL syntax (NOT Python syntax)]
        ptr.execute(sql, {'st_name':name,
                          'st_username':username,
                          'id_num':id_num
                          })

        # Writes or commits the data to the database
        conn.commit()
        response = input("Another student?")
        if response:
            if response[0].lower() in ('n', 'q', 'e'):
                addNames = False
    # Don't forget to close the IO stream connection to the db
    ptr.close()


'''**********************************************
   # Goal/Lesson: #3] Query an SQLite database
   **********************************************'''
def ch18Lesson3_get_data():
    '''
    Python_Sams18, p 203  |  get_data.py

    Gets SQL data from the Student table out of the mytest.db.

    Created on Tue May 12 18:49:16 2020
    @author: Lifygen
    '''
    import sqlite3

    # Open an iostream connection to the SQLite database
    conn = sqlite3.connect('mytest.db')
    ptr = conn.cursor()
    # Setup the SQL query statement
    sql = "Select * from students"
    # Execute the SQL statement and store results in <results> variable
    results = ptr.execute(sql)
    # Fetch all the items in results and put them into all_students
    all_students = results.fetchall()
    # Print the names of the students in the database
    for student in all_students:
        print(student)
    # Don't forget to close the IO stream connection to the db
    ptr.close()


def getSqlData(sql):
    '''
    Execute and sql statement and print the results.\n
    INPUT:\n
        sql = SQL query statement.\n
    OUTPUT:\n
        prints out the results of the query
    '''
    import sqlite3
    # Open an iostream connection to the SQLite database
    conn = sqlite3.connect('mytest.db')
    ptr = conn.cursor()
    # Setup the SQL query statement
    # nothing to do; the SQL is passed into the function.
    # Execute the SQL statement and store results in <results> variable
    results = ptr.execute(sql)
    # Fetch all the items in results and put them into all_students
    all_results = results.fetchall()
    # Print the names of the students in the database
    for dataPkg in all_results:
        print(dataPkg)
    # Don't forget to close the IO stream connection to the db
    ptr.close()


# Try getting only the student names:
getSqlData("select name from students")
# Try getting names and IDs:
getSqlData("select name, id from students")
getSqlData("select name, id from students order by id")
# Note:  Like is case insensitve, Order By <criteria> ASC/DESC
getSqlData('''SELECT 
                    name, id 
              FROM 
                    students 
              WHERE 
                    name like 'm%' 
              ORDER BY 
                    id DESC 
           '''
              )
# Note:  Try getting any combination of valid column data (can filter also)
#        see for example queries:  https://www.sqlitetutorial.net/sqlite-select/

# ===================================================

# **********************
'''
# Questions (p 207):
'''
# 1) What types of data can SQLite store?
#   [Answer]:  All kinds, including blob data which is a bulk data that a user
#              custom user defines the form for interpretation.
#              [official answer]:  null values, int, float, str, blobs
#
# 2) What is blob data?
#   [Answer]:  see resposne to question #1.
#              [official answer]: blob is a binary large object.  ex. picture, 
#                                 music file, zip file.
#
# 3)  What is a cursor?
#   [Answer]:  A pointer into the database.
#              [official answer]: a cursor is the object we use to move around
#                                 the database.
'''
# ***********
# EXCERCISE (p 208):
# Excercise [1] Inventory Program using SQLite instead of JSON
#           Given the basic inventory program that the cook wrote.  Write a
#           function that allows her to search through the database for a
#           particular item.  You'll need to - 
#           a) Write a SELECT query
#           b) Print out how many of each of the search items are in inventory
#           c) If search item is not found then pritn a message stating the item
#              is not in inventory.
#
# ***********
'''
'''
# [Answer]:  see Python_Sams18_Ex_InventorySQL.py
#
'''

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

