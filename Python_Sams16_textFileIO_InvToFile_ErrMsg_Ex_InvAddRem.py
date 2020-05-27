'''
#  SAMS Python Chapter 16 (pp 170 - 181) Training snippets, Quiz and Excercise
#  "Working with Program files and directories (read, write)
#
#**********************
# Course Training -
#**********************
# 1] see textfile experimenting with file read/write:  users.txt

    # Write Only MODES     (also creates file if it does not exist)
    # <file>.
    # .open(<filename>,'a') = append, file is opened with write pointer at
                              end of file.
    # .open(<filename>,'w') = write (wipes the file upon opening)

    # Read/Write MODES     (also creates file if it does not exist)
    # .open(<filename>,'w+') = opens file for read/write
                               but wipes the file first.
    # .open(<filename>,'r+') = opens file for read/write
                               without clearing the file.

      NOTE: Writes are made at the pointer [set by .seek()] but
            the file is truncated at the end of the written text.
            i.e. keeps all text above the write and deletes all
            text below it.

    # .open(<filename>,'a+')= appends to the end of the file regardless of
                              where the pointer iswhen a .write() or
                              .writelines() is made.

    # Read Only MODES
    # .open(<filename>) or .open(<filename>, 'r')

    # Move Pointer       (works for reads, and both r+ & w+ writes)
    # .seek(<integer>) = moves the read/write pointer to
                         the <character> location.
                         Note:  yes, CHARACTER location and NOT_LINE location.

      a.  #Create a file to experiment with -
          createF= ['Mary Anne is the most beautiful girl I ever met!\n',
           'Mary Anne is the smartest girl I know too!!\n',
           'Too bad she smoked (:o(-<;'
          ]

          myFile=open('users.txt', 'w')
          myFile.writelines(createF)

          myFile.close()

#     b.  #Open file for read only:

          myFile = open('users.txt')

          #read one line and put point at beginning of next line
          #result is null if no more data exists.
          line = readline()

          #Read all lines in the file
          allLines = readlines()

          myFile.close()

      c.  #Open a file to WRITE/Create file, overwrites data if file exists.
          #
          #     NOte:  Opening this way WIPES the file out just by calling and
          #            closing it (even if no write command id performed).
          #            BE CAREFUL when exiecuting this style of OPEN.

          myFile = open('users.txt', 'w')
          myFile.close()

          #*** NOTE the above will wipeout the user.text file. ***

      d.  #<file>.writelines() - Open a file and write contents
                                 (multiple lines) into it.

          myFile = open('users.txt','w')
          myFile.writelines(createF)
          myFile.close()

          # Note:  createF is a list  of strings. each string has to have an
          #        EOL (or /n) at the end of each intended line otherise the
          #        data is continually written to the smae line.


      e. #<file>.write() - Open a file and write a single line at at time.

         text = ""; t="";
         # Creates single string that is <createF data with EOL> wihtin the str
         for t in createF:  text += t
         myFile = open('users.txt','w')
         myFile.writelines(createF)
         myFile.close()

         NOTE:  CANNOT write or insert into the middle of a file.
                Can only write at the beginning or append to the
                end of the file.

      f. #Append a file ('a' mode)

         myFile = open('user.txt', 'a')
         myFile.write('A new line')
         myFile.close
         myFile = open('user.txt')
         allLines = myFile.readlines()
         myFile.close()
         print allLines

       g. #myFile = open('users.txt', "r+w')
         #.lines() = reads the whole file; if multiple lines exist then a
         #           list object containg each line as a string is returned.
         #.line() = reads a single line

# 2]  Directory (aka Path) Navigation:
      import os
      currentDir = os.getcwd() : Current working directory
      os.chdir(c:/<newpath>)   : Sets new current working directory
      inDir = os.listdir(currentDir) = returns list of DIRs and Files in the
                                       directory fed to it.
      os.walk() =  allows navigation through a directory.
      os.makedir = makes directories, single string puts the directoyr in the
                   current directory.  If a full pathis provied then the new
                   directory id created at the path location provided.

    Walk() Example:
    >>> import os
    >>> Directory = os.walk('.")   #Directoroy object is made from the current
                                    directory and contains the path tree.
    >>> Directory.next()           #Each time the .next() method is invoked,
                                    a tuple is returned showing the directory
                                    and files wihtin the current directory.
                                    1) The first .next() gets the current
                                       directory contents.
                                    2) The second .next() gets the contents of
                                       the first directory shown in the initial
                                       tuple.  Subsequent .next() will step
                                       through all the directories in the
                                       folder.  Once the last directory is
                                       reached, invoking .next() will go back
                                       to the parent directory and get the next
                                       directory (if it exists) and then step
                                       through that and so on until all
                                       directories have been mapped.

# 3]  Get File Status info:
      >>> import os
      >>> stats = os.stat(<filename>)    #returns the file info
      >>> stats.st_atime     #Last datetime the file was accessed in
                              Unix time (since 00:00:00 Jan 1, 1970)
      >>> import datetime
      >>> datetime.fromtimestamp(stats.st_atime)
          retuns a tuple (yyyy, mm, dd, hh, mm, ss)
          for when the file was last accessed.

      >>> stats.st)mtime     #Last time file was Manipulated or edited
      >>> stats.st_size      #Size of the file
'''


# **********************
#     a.  sys.path : provides a list of folders in the directory
#                    (i.e. parent folder)

#     b.  use __init__.py :  usualy an empty file that indicats to Python to
#                            search for [packages] in the dir where this is
#                            located.  putting this empty file in the folder
#                            tells Python that the folder is a [package] folder
#
#     c. RULE:  DO NOT USE "-" dashes in filenames (use udnerscore "_" instead)
#                              Python reserves dashes for special meaning.
# **********************

'''
#**********************
# Questions:
#
# 1) What is the built-in for opening a file? what does it return?
#   [Answer]:  Open(<filename>, <mode>); returns a file i/o stream.
#
# 2) How do you open a file so that you start at the end of the file?
#   [Answer]:  Open(<filename>, <mode>), Open(<filename>, 'a') =
#              appends a file.  use 'a+' mode to allow read/write.
# 3)  What is shorthand for 'current directory'?
#   [Answer]:  Use a dot '.'
#              >>> import os
#              >>> currentDir = os.getcwd()
#***********
# EXCERCISE: P. 181 Alter Inventory program to accomodate file read/write
#***********
#
# 1) You already have a basic inventory program that opens a file and gets
#    all items in the current inventory.  Round out the program by adding
#    functions:
#    a. One that allows the user to add items to the Inventory
#    b. One that allows the user to remove items from the inventory
#    c. One that allows the user to save the inventory after making changes
#
#  [Answer]:  See the ingredients.py, inventory.py, recipes.py in
#             the "classes" folder and main() below;
'''
# ===================================================
from classes.ingredients import Ingredient
from classes.ch16_inventory import Inventory


# *** MAIN Program
def main():
    # Attempt to Open a file for Read Only
    f = open('data\\Ch16_Inventory.txt')
    lines = f.readlines()
    f.close()
    items = {}
    for line in lines:
        line_wo_EOF = line.strip('\n')  # Remove EOL from the text
        line_wo_Tab = line.split('\t')  # Split the screen wherver a Tab is
        #                                 located and return a list of strings
        #                                 based on the split
        line = line_wo_Tab
        item = Ingredient(name=line[0])
        items[item] = int(line[1])
    # Creates new Inventory object with data from items
    inventory = Inventory(items)
    inventory.print_inventory()
    print("")
    inventory.show()


if __name__ == "__main__":
    # [Test #1] Test the kitchen classes:  Ingredient(), Recipe(), Inventory()
    # from classes.ingredients import Ingredient
    # from classes.recipes import Recipe

    # Main() performs a file open READ ONLY
    main()

    # Create a file to experiment with Reading and Writing -
    createF = ['Mary Anne is the most beautiful girl I ever met!\n',
               'Mary Anne is the smartest girl I know too!!\n',
               'Too bad she smoked (:o(-<;'
               ]
    f = open('user.txt', 'w+')
    f.writelines(createF)
    f.close()

#    f.read
#
#    f.readline()    # Reads a single whole line at the pointer
#    f.readlines()   # Reads all lines or whole file
#    f.write()       # Writes a string
#    f.writelines()  # Writes any iterable object or sequence of stinrgs.

    # ***** ***************
    # Mode: W+ (read/write)
    # ***** ***************
    t = ['Hello Bunny:\n', '\n', "I miss you.\n", "\n", "Love,\n\n", "Gene\n"]
    f = open('user.txt', 'w+')
    f.writelines(t)
    f.seek(0)
    read = f.readlines()

    # the <>.seek moves the pointer the designated number of characters.  If it
    #             gets to the end of the line then it starts moving down the
    #             next line.
    f.seek(26)
    f.write("  This should write a new whole line.\n")
    f.seek(0)
    read2 = f.readlines()

    if read == read2:
        print("they are the same; unchanged")
    else:
        print("they are DIFFERENT!!!")

    # ***** ***************
    # MOde: r+ (read/write)
    # ***** ***************
    f = open('user.txt', 'r+')
    f.writelines(t)
    f.seek(0)
    read = f.readlines()

    # the <>.seek moves the pointer the designated number of characters.  If it
    #             gets to the end of the line then it starts moving down the
    #             next line.
    f.seek(27)
    f.write("  This should write a new whole line.\n")
    f.seek(0)
    read2 = f.readlines()

    if read == read2:
        print("they are the same; unchanged")
    else:
        print("they are DIFFERENT!!!")

# *** ************************
# Training / Practice = Test Scripts to check file Read/Write/Append
# *** ************************

# ***** ***************
# Mode: W+ (read/write)
# ***** ***************
t = ['Hello Bunny:\n', '\n', "I miss you.\n", "\n", "Love,\n\n", "Gene\n"]
f = open('user.txt', 'w+')
f.writelines(t)
f.seek(0)
read0 = f.readlines()


# ***** ***************
# MOde: r+ (read/write)
# ***** ***************
# Initialize the file: user.txt
# Do this by opeing with write capability and write 't' variable from above
f = open('user.txt', 'w')
f.writelines(t)
f.close()

# Test Read #1
# Open with R/W using r+
# Change to 'a+', 'r+', 'w+' mode and view diff results.
f = open('user.txt', 'r+')
read1 = f.readlines()

# Test Read #2
# Place the pointer at the line between body and signature and write new text.
pointer = 0
for i in range(0, 3):
    pointer += len(read[i])
f.seek(pointer+1)
f.write("  This should write a new whole line.")
f.seek(0)
read2 = f.readlines()
f.close

# Test Read #3
# Open with R/W using r+; perform write, move to top and read whole file
f = open("user.txt", "r+")
f.write("#")
f.seek(0)
read3 = f.readlines(0)
f.close()

# Test Read #1
# Open with R/W using a+; perform write, move to top and read whole file
f = open('user.txt', 'a+')
f.write("@")
f.seek(0)
read4 = f.readlines()
f.close()


import os
currentDir = os.getcwd()
b = os.walk(currentDir).next()


# *** ************************
# Excercise = Test Script to check implementation
# *** ************************
# ----------------------------
# Intilalize variables and file info
# ----------------------------
from classes.ch16_inventory import Inventory
try:
    f = open('C:/Users/Lifygen/projects/python/Ch16_Inventory.txt')
except IOError:
    f = open('C:/Users/Lifygen/projects/python/Ch16_Inventory.txt', 'w+')
    f.writelines(["eggs\t48\n",
                  "flour (lb)\t25\n",
                  "tomato sauce (cans)\t20\n",
                  "mozz cheese (lb)\t10\n",
                  "milk (gal)\t10\n"
                  ])
    f.seek(0)
lines = f.readlines()
f.close()
items = {}

# ----------------------------
# Script to test while printing the steps for parsing the file lines
# ----------------------------
for line in lines:
    print("1) ", line)
    line_woEOL = line.strip('\n')
    print("2) ", line_woEOL)
    line_woTab = line_woEOL.split('\t')    # Split line at the Tab and put
    #                                        results into a list.
    print("3) ", line_woTab)
    line = line_woTab
    item = Ingredient(name=line[0])    # put the line (list of items) into item
    print("4) ", item)            # item here is the name of an item
    items[item] = int(line[1])   # create a <dict> out of the item name and qty
    print("5) ", items[item])

inventory = Inventory(items)
inventory.print_inventory()
print("")
inventory.print_inventory()
inventory.show()

# ----------------------------
# Script to test w/o printing parsing steps
# ----------------------------
# Intilalize variables and file info
import os
currentDir = os.getcwd()
print("Current Working Dir: ", currentDir)
os.chdir("C:/Users/Lifygen/projects/python")
lastDir = currentDir
currentDir = os.getcwd()
print("Current Working Dir: ", currentDir)

from classes.ch16_inventory import Inventory
from classes.ingredients import Ingredient


try:
    f = open('C:/Users/Lifygen/projects/python/data/Ch16_Inventory.txt')
except IOError:
    f = open('C:/Users/Lifygen/projects/python/data/Ch16_Inventory.txt', 'w+')
    f.writelines(["eggs\t48\n",
                  "flour (lb)\t25\n",
                  "tomato sauce (cans)\t20\n",
                  "mozz cheese (lb)\t10\n",
                  "milk (gal)\t10\n"
                  ])
    f.seek(0)
lines = f.readlines()
f.close()
items = {}
invTest = ""
item = ""
# Create Items dictionary from the file info
i = 0
for line in lines:
    i += 1
    print("\n" + str(i) + ")" + "fileline:  ", line)
    line = line.strip('\n')
    line = line.split('\t')    # Split line at Tab and put results into a list.
    item = Ingredient(name=line[0])   # put the line (list of items) into item.
    print("a) Item:  ", item)         # <item> here returns the name of an item
    #                                    because <Ingredient> uses a __str__
    #                                    overload.
    # Create a dictionary out of <Ingredients> class obj and its qty value
    itemName = item.name
    items[itemName] = int(line[1])
    print("b) Qty:  ", items[itemName])
print("\nPrint the contents of the items<dict>\n" +
      "-------------------------------------")
for each in items:
    print(str(each) + ":" + " "*(25-len(each)+1), items[each])
# Create an <Inventory> from items<dict>
invTest = Inventory(items)
print("\nPrint invTest.print_inventory()\n-------------------------------")
invTest.print_inventory()
print("\n")
invTest.show()


# ----------------------------
# ERROR Testing:  Try/Except
# ----------------------------
invFileName = 'Gene.txt'
try:
    inventory_file = open(invFileName)
except IOError as e:
    print("s.message:  ", e.message)
    print("e.strerror:  ", e.strerror)
    print("e.filename:  ", e.filename)
    print("e.errno:  ", e.errno)
    print("e.args:  ", e.args)
    print("")
    print("I/O error({0}): {1}".format(e.errno, e.strerror))

#    inventory_file= open(invFileName, 'w+')
#
#    readLines = inventory_file.readlines()
#    inventory_file.close()


# *** **********************
# Store Dictionary in a file
# *** **********************
import os
os.chdir("C:/Users/Lifygen/projects/python")
aDict = {'tomato sauce (cans)': 20, 'eggs': 48, 'milk (gal)': 10,
         'mozz cheese (lb)': 10, 'flour (lb)': 25}
afile = open('')
