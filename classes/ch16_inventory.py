'''
# ***********
# EXCERCISE: P. 181 Alter Inventory program to accomodate file read/write
# ***********
  
# 1) You already have a basic inventory program that opens a file and gets
# all items in the current inventory.  Round out the program by adding
# functions:
# a. One that allows the user to add items to the Inventory
# b. One that allows the user to remove items from the inventory
# c. One that allows the user to save the inventory after making changes
# 
'''

# from classes.ingredients import Ingredient
# from ingredients import Ingredient

class Inventory(object):
    '''A class that is basically an extension of the Dictionary class object.
    Inventory.items is a dictionary object.
    Inventory.<methods> are added to auto increment item
    values as items are added into inventory (and decrement when removed).
    
    Initialization INPUT:
        :items[] (str/tuple/list/dict):- can be any of the following objects \
                                         upon initialization:
                - string object - a text name of an inventory item. Example
                                  'itemName'
                - tuple  object - a tuple of string names formatted as follows:
                                  ('item1', 'name2', 'third',...'nthItemName')
                - list object   - a list of string names, of following format:
                                  ['item1', 'name2', 'third',...]
                - dict object   - a dictionary paring of {'name':qty} items.
    '''
    def __init__(self,
                 items=[],
                 invFileName="C:/Users/Lifygen/projects/python/data/" +
                             "Inventory.txt"
                 ):
        self.items = {}
        try:
            inventory_file = open(invFileName)
        except IOError as error:
            print(error.filename + " - file does not exist.\n" +
                  error.strerror + ":\n" +
                  " > " + invFileName
                  )
            inventory_file = open(invFileName, 'w+')

        readLines = inventory_file.readlines()
        inventory_file.close()

        for line in readLines:
            line = line.strip('\n')    # Strip EOL off the string
            line = line.split('\t')    # Split line at the Tab and put
            #                            results into a list.
            # Put the item name and quantity into a dictionary <items>
            # DISAGREE with SAMS book example (for now) item does not need to be
            # an <Ingredient> object.  Just make it a string so that users can
            # create a file manuallly using "<item>\t<quantity>\n" format.
            # If not done this way then a string "egg" in the file will not
            # match an egg<Ingredient> object and two "egg" entries are written
            # to the file and then you'd have to read the file, write it out and
            # read it back to get rid of duplicates. That would work because
            # the files stores strings and NOT objects and the .add() looks for
            # duplicates of dictionary keys for incrementing quantity where the
            # key is the name of the item.
            # item = Ingredient(name =line[0])   # *** commented out this line ***
            item = line[0]
            qty = line[1]
            if not items:
                items = {}
            #Must be self.items on next line.
            self.items[item] = int(qty)
        # Add items to self.items
        self.add(items)
        self.invFileName = invFileName

    def add(self, items, qty=1, fileUpdate=False):
        '''.add method receives an item=<string>, optionally a \qty=<integer>
        results in incrementing the named item by the qty amount.
        The code detects the item <data type>.  
        A list type(standard list, tuple, or dictionary) results in each
        item in the list being added to the Inventory and incremeted by
        qty (default =1).  If the item already exists in inventory, then
        inventory quantity is updated.  If the code detects a
        a <dict> object then it pulls the 'key' to use as item name and
        the 'value' to use as the qty value.

        Note:  the DocString has to start at the same indent level as
               normal code, otherwise it is ignored.
        '''
        if items:
           if (type(items) is str):
              # If items is a string then put it in a list so it can be handled
              # by handled by the same code used for list, tuple, dict. 
               items=[items]
           if ((type(items) is tuple) or
               (type(items) is list) or
               (type(items) is dict)
              ):
              for eachItem in items:
                 if (type(items) is dict):
                    qty = items[eachItem]
                 # Python 3 uses 'keyname' in dictionary
                 # in place of Python 2's dict.has_key('keyname')
                 if eachItem in self.items:
                    self.items[eachItem] += qty
                 else:
                    self.items[eachItem] = qty
           if fileUpdate:
              if self.store():
                 print("Inventory file updated:  " + self.invFileName)
        else:
            print("INVALID ENTRY, nothing added to the inventory.")

    def remove(self, items, qty=1, fileUpdate =False):
        ''' .remove method receives an item=<string>, optionally a qty=<integer>.
                    results in decrementing the named item by the qty amount.
                    Code detects item type as in .add(), see the .add() desc.
        '''
        if items:
          # Create a single item list if the user input is a string object
           if (type(items) is str):
               # If items is a string then put it in a list so it can be handled
               # by handled by the same code used for list, tuple, dict.
               items=[items]

           if ((type(items) is tuple) or 
               (type(items) is list) or
               (type(items) is dict)
              ):                    
              for eachItem in items:
                 if (type(items) is dict):
                    qty = items[eachItem]
                 # Python 3 uses 'keyname' in dictionary
                 # in place of Python 2's dict.has_key('keyname')
                 if eachItem in self.items:
                    if self.items[eachItem] > 0:
                     self.items[eachItem] -= qty
                 else:
                    print("We are out of " + eachItem + "(s)!!!")
           if fileUpdate:
              if self.store():
                 print("Inventory file updated:  " + self.invFileName)
        else:
            print("INVALID ENTRY, nothing removed from the inventory.")

    def check(self, item): 
        ''' takes a single item <type string>, looks for the item in inventory
        and returns the item name and quantity in inventory as a dictionary obj
        or if none in inventory then a null dictionary object is returned)
        '''
        if self.items.has_key(item):
           return {item:self.items[item]}
        else:
           return {}

    def print_inventory(self):
        ''' prints_method() - prints out the contents of the inventory as text 
                              in "item" - qty format.
        '''
        # 'Shows Inventory items and quantities
        for item in self.items:
              print(item, "-", self.items[item])

    def show(self):
        ''' Overloads the print()
            :print(<Inventory_obj>): - prints out the contents of the \
                                       inventory in |"item" - qty| format.
        '''
        # 'Shows Inventory items and quantities
        # ex. using iterable function:  
        #     max([len(song.name) for song in self.songList])
        invBackup = []
        maxLen = max([len(item) for item in self.items])
        for item in self.items:
              print(item + " "*(maxLen-len(item)+1) + "-", self.items[item])
              invBackup.append([item + "\t" + str(self.items[item]) + "\n"])
        return invBackup

    def store(self):
        try: 
            print("*************")
            print("Inventory Obj (from memory)")
            print("*************")
            self.show()
            print("Show from memoery complete!!!")

            # Open file for R/W
            inventory_file = open(self.invFileName,'w+')
            print("")
            print("*************")
            print("Inventory Obj (from oldFile)")
            print("*************")
            inventory_file.seek(0)
            oldFile = inventory_file.readlines()
            print(oldFile, "\n*** OldFile Printout Complete ***")

            # Write the inventory object info (in memory) to file (overwriting file)
            writeLines=[]
            print(self.items)
            if not self.items:
                print("Empty inventory.")
                inventory_file.writelines(oldFile)
            else:
               for item in self.items: 
                 writeLines.append(item + "\t" + str(self.items[item]) + "\n")
                 inventory_file.seek(0)
                 inventory_file.writelines(writeLines)
        except:
            print("File could not be updated:\n" + self.invFileName)

        # Close file
        inventory_file.close()

if __name__ == "__main__":
   '''This tests out the Inventory class
   '''

   # Tuple Test Passes
   print("Tuple fed to Inventory Test")
   aTuple =('apple', 'orange','bannana')
   print(aTuple)
   tI=Inventory(aTuple)
   tI.print_inventory()
   print('\n')

   # Dict Test Passes
   print("Dict fed to Inventory Test")
   aDict={'apple':1, 'orange':3,'bannana':5}
   print("Dict Print:", aDict)
   dI=Inventory(aDict)
   print("dI.print_inventory():")
   dI.print_inventory()
   print('\n')

   # List Test Passes
   print("List fed to Inventory Test")
   aList=['Mary Anne', 'Cindy', 'Stan']
   print(aList)
   lI=Inventory(aList)
   lI.print_inventory()
   print('\n')

   # String Test Passes
   print("String fed to Inventory Test")
   aStr = "Gene"
   print(aStr)
   sI=Inventory("Gene")
   sI.print_inventory()
   print('\n')

   # Remove single string item Test Passes
   print("Inventory.remove():  dI.remove('bannana')")
   dI.remove('bannana')
   dI.print_inventory()
   print('\n')

   # Add single string item Test Passes
   print("Inventory.add():  dI.add('apple')")
   dI.add('apple')
   dI.print_inventory()
   print('\n')

   print("*** Hello World END ***")
    
    