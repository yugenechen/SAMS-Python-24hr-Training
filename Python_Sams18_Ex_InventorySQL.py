# -*- coding: utf-8 -*-
"""
Python_Sams18, p 203, Excercise:  Recreate cook's Inventory() using SQLite

# ***********
# EXCERCISE (p 208):
#   [1] Inventory Program using SQLite instead of text
#       Given the basic inventory program that the cook wrote.  Write a
#       function that allows her to search through the database for a
#       particular item.  You'll need to -
#       a) Write a SELECT query
#       b) Print out how many of each of the search items are in inventory
#       c) If search item is not found then print a message stating the item
#          is not in inventory.
# ***********
#
Created on Tue May 09 58:05:11 2020

@author: Lifygen
"""
"""
Planning:  Workplan/Architecture
Review Requirements and create a workplan:
1)  Create an SQLite db
#  #[status]:  Done, open_db(dbName, *path)

2)  Create a table within the db
#  #[status]:  Done, createTable(ptr)

3)  Doc Inventory structure
    Review existing inv and requirements and develop an architecture or guiding
    document.
#  #[status]:  Done, Guidig document is below:
    May not be implemented as a dictionary, may make it a class or other form.
    However, this represents structures adn relationships.  Idea is to have an
    <item> that has an associated <name>, <quantity>,
                                  <unit of measure>, <FoodCategory>
    Example, itemName possibility -
        itemName could be of the following form: "<name> <unit>"
             where <unit> = (each, can, frzn, bottle, bag, lb, oz. gal, etc.)
    Inventory{
        "<itemName_obj>"{
            "unit":<unit.of.measure_str>
            "qty":<qty_int>
            "FoodGroup":(
                "vegetable", # "not Official USDA class": beans, legumes, tofu
                "fruit",     # fresh, dried, frozen, canned
                "grain",     # includes seeds, nuts. cereals
                "beverage",  # possible subclass(coffee, tea, juice, milk)
                "meat",      # possible subclass(beef,pork,poultry,fish,egg)
                "dairy",
                "oil",
                "spice"
             )
         }
        Note: (optional architectures)
        a. Could implement a FoodGroup Table with valid category names.
        b. Likewise, Vegetable, Fruit, Grain, Bev, Meat -tables.

4)  Create function to import/convert text file inventory into SQLite
        a.  addInv()
        b.  removeInv()
        c.  showInv()
        d.  importInv() - from existing Invntory.txt file
            Existing Text format:  <itemName_str><sp><(unit_str)><tab><qty_int>
#  #[status] Done, use importInv(ptr, importFile) and feed return into addInv()

5)  SearchInv() - a. creates an SQL query based on UserInput
                  b. executes the SQL query
                  c. prints results
                    c1.  msg # of items in Inv
                    c2.  msg "Item is not in Inv"
#  #[status]: Done, a. checkForItem(ptr, searchItem=""), returns item and qty
                    b. itemInDb(), returns True if item in Db otherwise False

6)  Extra Credit:
    6.1)  Create function that outputs whole Inventory (to screen)
#  #[status]: Done, see showInv(ptr, toScreen=True, sendRet=False)

    6.2)  alter 6.1 so that it Shows
                                     whole Inventory, or
                                     filtered by Category, and/or
                                     by "begins with" letter(s) of item name
#  #[status]: Done, see output of  checkForItem(ptr, searchItem="")

    6.3)  Optionally print and/or return the Inventory (as <dict> "item":qty)
#  #[status]: Done, Demonstrated in the return of both importInv() & showInv()

    6.4)  Eliminate duplicates in SQLite db and have duplicate adds increment\
          the quantity in the Inventory.db (which is a SQLite db)
#  #[status]: 
"""


import sys
import os
import sqlite3
from classes.ytcClasses import isfloat
from classes.ytcClasses import str_to_float_or_int


def open_db(dbName, path=""):
    """Attempt to open an SQLite db. If it does not exist then create it.\n
    Package Requirements:  sqlite3, \
                           os

    INPUTs:
      :dbName (str): - SQLite database filename.

    OUTPUTs:
      :return (tuple): -  a Tuple of the database connection_obj and \
                          cursor_obj: (conn, ptr)
    """
    print(path)
    # Handle the optional path input, ensure it has a / or \\ ending and
    # create the full file path name to use in creating/opening the db.
    if not path:
        fullFilePath = os.getcwd() + '\\data\\' + dbName
    else:
        # converts the path from a Tuple to a string
        length = len(path) - 1
        if path[length] in ('\\', '/'):
            fullFilePath = path + '\\' + dbName
        else:
            fullFilePath = path + dbName
    # Get SQLite database connection (file i)
    conn = sqlite3.connect(fullFilePath)
    ptr = conn.cursor()
    print(path)
    return (conn, ptr)


def createTable(ptr, TableName):
    """Create the proper Inventory table structucture within the database.\n
    Package Requirements:  sqlite3.

    INPUTS:
        :ptr (cursor_obj): - SQLite database pointer (or cursor) object

    OUTPUTS:
        :return (bool): - True:  successful
                        - False: failed
    """
    sql = """create table :TableName (
        itemName text,
        unit text,
        qty int,
        FoodCategory text)"""
    try:
        ptr.execute(sql,{"TableName":"Inventory"})
    # Catches if the table already exists and allows continued operation,
    # since the table already exists and does not need to be created.
    except sqlite3.OperationalError as err:
        # Print out tuple of error messages (in case other than "Table Exists")
        print("INFO Message:")
        full_errMsg = ""
        for errMsg in err.args:
            full_errMsg += (errMsg.capitalize() + ".  ")
        print(full_errMsg,
              "\n*** Continuing to process as normal. ***")
    except Exception as err:
        print("An unexpected error occurred in createTable(ptr):",
              sys.exc_info()[0])
        full_errMsg = ""
        for errMsg in err.args:
            full_errMsg += (errMsg.capitalize() + ".  ")
        print(full_errMsg)
        return False
    return True


def addInv(dbConnTuple, itemName="", unit="", qty="", FCat="", item=[]):
    """Add inventory item into the SQLite database\n
    Package Requirements:  sqlite3, \
                           ytcClasses.isfloat,\
                           ytcClasses.str_to_float_or_int

    INPUT:
     :ptr (cursor_obj): - pointer into the opened SQLite database.
     :itemName (str or tuple list):   - name of item or a list of items in\
                                        [(item_data)] formaat.
     :unit (str):       - unit of measure,
                          (ex. lb, oz, each, can, frzn, bag, box, jug, \
                           bottle, etc.)
     :qty (float/int):  - item quantity
     :FCat (str):       - Food Category:  (none, veg, fruit, meat, grain, \
                          dairy, oil, spice)
     :item (list/tuple): - item entry as a list of one or more tuples.
                           Formatted as follows:  [(itemName, unit, qty, FCat)]

    OUTPUT:
        :return (bool): - True:  for successful addition;
                        - False: otherwise
    """
    # Initialize variables
    # Return Status
    status = False
    exitList = ('quit', 'exit', 'q', 'x')
    FCatList = ('none', 'veg', 'fruit', 'meat', 'grain', 'dairy', 'oil',
                'spice')

    if (type(itemName) is tuple) or (type(itemName) is list):
        item = itemName
        if item is tuple:
            # If item is a tuple, convert it into a list of tuple: [(item1)]
            item = [item]
    if ((not item) or (item == []) or (item == [()])):
        addItemsManually = True
    else:
        addItemsManually = False
    print(addItemsManually)

    # Handle and condition inputs
    if ((not item) or (item == [()])):
        print("Let's add an item(s) to the inventory!")
        while addItemsManually:
            while not itemName:
                itemName = input("Item's name (or [q]uit/e[x]it): ")
                if not itemName:
                    print("Invalid name, try agin.")
                elif itemName.lower() in exitList:
                    # Done entering data so exit out of the function
                    status = True
                    addItemsManually = False
                    itemName = 'quit'

            """Check for itemName in SQLitedb"""
            #If in SQLdb then collect qty and add that qty to the db and exit
            # otherwise keep processing

            while not unit and itemName != 'quit':
                unit = input("Input item's unit of measure " +
                             "[default = '(each)']: ")
                if not unit:
                    unit = "(none)"
                elif str(unit)[0] != "(":
                    unit = "(" + str(unit) + ")"

            while ((not qty) and (itemName != 'quit')):
                qty = input("Input quantity: ")
                if isfloat(str(qty)):
                    qty = str_to_float_or_int(qty)
                else:
                    print("Invalid quality.  Try Again.")
                    qty = 0
            while ((not FCat) and (itemName != 'quit')):
                FCatListTxt = ""
                for each in FCatList:
                    FCatListTxt += each + ", "
                FCat = input("Input Food Category: \n[{}]: ".
                             format(FCatListTxt))
                if ((not FCat) or (FCat not in FCatList)):
                    FCat = "none"
            if (itemName != 'quit'):
                # Write the item to SQLite db
                writeInv(dbConnTuple, (itemName, unit, qty, FCat))
            # Reset variables for next item addition
            itemName = ""; unit = ""; qty = ""; FCat = ""
    else:
        # Items are in the item[]; add these to the database.
        for each in item:
            itemName = each[0]
            unit = each[1]
            if not unit:
                unit = "(none)"
            elif str(unit)[0] != "(":
                unit = "(" + str(unit) + ")"
            qty = each[2]
            if isfloat(str(qty)):
                qty = str_to_float_or_int(qty)
            else:
                qty = 0
            FCat = each[3]
            if ((not FCat) or (FCat not in FCatList)):
                FCat = "none"
            # Write the item to SQLite db
            writeInv(dbConnTuple, (itemName, unit, qty, FCat))
        status = True
    return status


def writeInv(dbConnTuple, itemTuple):
    """Writes inventory data into the SQL database and commits the changes.\n
    Package Requirements:  sqlite3.

    INPUTS:
      :dbConnTuple (cursor_obj):\
          - Tuple of the datbase connector and cursor (aka pointer).   \
            Format:  (conn_obj, ptr_obj)
      :itemTuple (tuple):\
          - Tuple of the item to be added to the database. Format:     \
            (itemName, unit, qty, FCat), where FCat is the Food Category.\n
    OUTPUTS:
        none
    """
    # Write item and commit Inventory change to SQLite db.
    conn = dbConnTuple[0]
    ptr = dbConnTuple[1]
    # Gets a list of all duplicate items 
    # (first item in the duplicate is omitted)
    sql = """insert into Inventory
            (itemName, unit, qty, FoodCategory)
             values
                 (:itemName, :unit, :qty, :FoodCategory)"""
    ptr.execute(sql, {'itemName':itemTuple[0],
                          'unit':itemTuple[1],
                           'qty':itemTuple[2],
                  'FoodCategory':itemTuple[3]
                          })
    # Writes or commits the data to the database
    conn.commit()


def getSqlData(ptr, sqlQuery):
    """Execute the SQL query statement and return the results.\n
    Package Requirements:  sqlite3.

    INPUT:
      :ptr (cursor_obj): - SQLite database cursor (or pointer).
      :sqlQuery (SQLquery_obj): - SQL query statement.

    OUTPUT:
        :return (list): - the results of the query in a list.
    """
    # Execute the SQL statement and store results in <results> variable
    sqlResults = ptr.execute(sqlQuery)
    # Fetch all the items in sqlResults
    return sqlResults.fetchall()


def itemInDb(ptr, itemName):
    """Check for an item name in Inventory.  Return True/False"""
    sqlResults = ptr.execute("SELECT * \
                              FROM Inventory \
                              WHERE itemName=:itemName",
                              {"itemName":itemName})
    if not sqlResults.fetchall():
        return False
    return True


def delInvItem(dbConnTuple, itemName):
# Deletes all records (i.e. rows) that meet the sql statement criteria
    conn = dbConnTuple[0]
    ptr = dbConnTuple[1]
    sql = 'DELETE FROM Inventory WHERE itemName=?'
    ptr.execute(sql, (itemName,))
    conn.commit()
    # Deletes duplicate rows, keeps lowest numbered ID
#    sql = 'delete * from Inventory \
#           where rowid not in (select min(rowid) \
#                               from Inventory \
#                               group by itemName,qty)
#    ptr.execute(sql, (itemName,))


def consolidateInvItem(dbConnTuple, itemName):
    """ Consolidate duplicate rows, keeps lowest numbered ID and adds \
    duplicate items' qty to it.

    INPUTS:
      :dbConnTuple (cursor_obj):\
          - Tuple of the datbase connector and cursor (aka pointer).   \
            Format:  (conn_obj, ptr_obj)
    """
    conn = dbConnTuple[0]
    ptr = dbConnTuple[1]
    # This query gets All of a specfic itemName (first one and all its duplicates)
    sql_ItemName = ptr.execute("Select itemName, qty \
                               from Inventory \
                               WHERE itemName = :item",
                               {'item':itemName}
                               )
    newQty = float(0)
    for record in sql_ItemName:
        newQty = newQty + float(record[1])
        
    input("This is the new quantity Total: ", newQty)

    # DELETE all a specific itemName's duplicates (excluding original one)
    sql_DuplicateItems = "DELETE \
                          FROM Inventory \
                          WHERE itemName = :itemName \
                          and rowid not in (SELECT min(rowid) \
                                            from Inventory \
                                            group by itemName)"
    ptr.execute(sql_DuplicateItems, {"itemName":itemName})
    conn.commit()

    # Update the Quantity of the item
    ptr.execute("UPDATE Inventory \
                 SET qty = :qty \
                 WHERE itemName = :name \
                 GROUP BY itemName", 
                 {'qty':newQty, 'name':itemName})
    conn.commit()
""" deletes the duplicate items but does not update the quantity!!!!!!!!!!!!"""

def removeInv(ptr, itemName, remQty):
    """Decrement the quantity of an inventory 'item' in the SQLite database.

    INPUT:
      :ptr (cursor_obj): - pointer into the opened SQLite database.
      :itemName (str): - name of the item to be removed from inventory.
      :remQty (float/int): - quanity of item being removed from inventory.
    """
    # Not implmeneted yet....
    pass


def showInv(ptr, toScreen=True, sendRet=False):
    """Show all items in the inventory [itemName, unit, qty, category].

    Package Requirements:  sqlite3.

    INPUTS:
        :ptr (cursor_obj): - pointer into the opened SQLite database.
        :toScreen (bool): - True:  prints to screen.
                          - False:  no print, only return value

    OUTPUTS:
        :print to screen: - prints to screen if 'toScreen' is True
        :return (dictionary): - {name:[qty, unit, FCat]}, \
                               where FCat = Food Category
    """
    sqlQuery = "Select * from Inventory"
    all_results = getSqlData(ptr, sqlQuery)
    # Print all the items in the Inventory database
    itemDict = {}
    for dataPkg in all_results:
        if toScreen:
            print(dataPkg)
        if sendRet:
            itemDict.update({dataPkg[0]: [dataPkg[1],
                                          dataPkg[2],
                                          dataPkg[3]
                                          ]})
    if sendRet:
        return itemDict


def checkForItem(ptr, searchItem=""):
    """Decrement the quantity of an inventory 'item' in the SQLite database.

    INPUT:
      :ptr (cursor_obj): - pointer into the opened SQLite database.
      :searchItem (str): - name of the item to be searched for in inventory.

    OUTPUT:
      :print to screen:    - prints to screen if 'toScreen' is True
      :return (tuple/str): - If searchItem is in inventory then return a tuple. \
                             Format:  (itemName, unit, qty, category)
                        - If item is not found, return message:  \
                          "Item type does not exist in the inventory; try \
                          adding it with qty=0."
                        - If item is found at 0 qty, return message:  \
                          "Out of stock."
    """
    # Build Select statement
    if (type(searchItem) == str and searchItem):
        sqlQuery = ("SELECT * " +
                    "FROM Inventory " +
                    "WHERE itemName like '" + searchItem + "%' " +
                    "ORDER BY itemName ASC"
                    )
        queryResult = getSqlData(ptr, sqlQuery)
        qty = str(queryResult[0][2])
        unit = queryResult[0][1]
        itemName = queryResult[0][0]
        print('\nSearch for "' + searchItem + '":', queryResult,"\n")
        if not queryResult:
            print(searchItem + " type does not exist in the inventory; try " +
                  "adding it with qty=0."
                  )
        elif queryResult[0][2] == 0:
            print(itemName + " is Out of Stock.")
        else:
            print("There are " + qty + " " + unit + " of " + itemName +
                  " in Stock."
                  )
        return queryResult

    what = input(" Enter what fields you'd like returned in additon to " +
                 "[itemName]: \n" +
                 " [1] unit\n" +
                 " [2] qty\n" +
                 " [3] Food Category\n" +
                 " [A] All\n" +
                 "example: 12 - return [itemName, unit, qty]\n" +
                 "          3 - return [itemName, Food Category]" +
                 "          A - return [itemName, unit, qty, Food Category]" +
                 "\n[IN]: "
                 )
    Select = 'SELECT itemName'
    if not what:
        Select += '*'
    else:
        if "1" in what:
            Select += ', unit'
        if "2" in what:
            Select += ', qty'
        if "3" in what:
            Select += ', FoodCategory'
        if (('A'.lower() in what.lower()) or ('*' in what)):
            Select = 'SELECT *'
    # Build Where statement
    startsWith = input('Add "Search-by-name" by entering an item name or ' +
                       'the first few letters of it, or [Enter] to skip.\n' +
                       '[IN]: ')
    Where = "WHERE "
    if not startsWith:
        Where = ""
    else:
        Where += "itemName like '" + str(startsWith) + "%' "
    category = input("Choose a category filter: \n" +
                     "[none, veg, fruit, meat, grain, dairy, oil, spice] : ")
    if (not category or ("n" in category.lower())):
        category = ""
    else:
        category = "FoodCategory like '" + category + "%' "
        if not Where:
            Where = "WHERE " + category
        elif Where and category:
            Where = Where + "AND " + category
    OrderBy = "ORDER BY itemName ASC"

    # Construct query statement
    sqlQuery = (Select + " FROM Inventory " + Where + OrderBy)
    print("SQLquery:  \n  " + sqlQuery)

    all_results = getSqlData(ptr, sqlQuery)
    print(all_results)
    return all_results


def importInv(ptr, importFile):
    """Import inventory items from existing "Inventory.txt" file and translate\
       them into the new SQLite database.

    Old [*.txt] database format:  <itemName_str><sp><(unit_str)><tab><qty_int>

    INPUTS:
      :ptr (cursor_obj): - pointer into the opened SQLite database.
      :importFile (str): - full path filename of the text database to \
                           translate into the SQLite database.

    OUTPUTS:
        none, just performs writes to the new SQLite database.
    """
    # Get old text file database
    f = open(importFile)
    oldTxtDb = f.readlines()
    f.close()
    oldTxtDB = {}
    for line in oldTxtDb:
        # Remove EOL from the text
        line = line.strip('\n')
        # Split the data at <Tab> to yield ["itemName (unit)", "qty"]
        line = line.split('\t')
        qty = line[1]
        itemName_and_unit = line[0].split('(')
        itemName = itemName_and_unit[0].strip(" ")
        if (len(itemName_and_unit) > 1):
            unit = "(" + itemName_and_unit[1]
        else:
            unit = '(each)'
        FCat = 'none'
        oldTxtDB.update({itemName: [unit, qty, FCat]})
    print(oldTxtDB)
    return oldTxtDB

def nicePrint(itemDict):
    for each in itemDict:
        itemName = str(each).ljust(30, ".")
        # Unit .rjust(calc).ljust() centers the text in the field
        unit = itemDict[each][0]
        unit = unit.rjust(len(unit)
               + int((10-len(unit))/2), " ").ljust(10, " ")
        # qty must be converted to a string first, centered on 3 digits
        qty = str(itemDict[each][1])
        qty = qty.rjust(4, " ").ljust(6)
        # FCat put one space in front of str ; sames as (" " + FCat)
        FCat = itemDict[each][2]
        FCat = FCat.rjust(len(FCat)+1, " ").ljust(15, " ")
        print(" " +
              itemName + "|" +
              qty + "|" +
              unit + "|" +
              FCat
              )

#
# *** MAIN Program
# ===================================================
def main():
    print("Hello World!")
# MAIN PROGRAM that solicts input from the User until Quit is selected.
    # 1) Add new SQLite Inventory db items, 
    # 2) Search for an item in the SQLite Inventory db
    # 3) Print the whole inventory to screen
    # 3) Quit the program
    print("Create Table resuls: ", createTable(ptr))
    response = ""
    while not response:
        response = input("Do you want to: \n" +
                         "[a]dd an item\n" +
                         "[s]earch for an item in inventory\n" +
                         "[p]rint the whole inventory\n" +
                         "[q]uit\n"
                         "[IN]: "
                         )
        if response.lower() == "q":
            ptr.close()
            break
        elif response.lower() == "p":
            # Show Inventory
            itemDict = showInv(ptr, toScreen=True, sendRet=True)
            Header = (" Item Name".ljust(31, " ") + "|" +
                      " Qty".ljust(6, " ") + "|" +
                      "Unit".ljust(7).rjust(10) + "|" +
                      " Food Category".ljust(15)
                      )
            print("\n" + Header)
            print(" " + "-"*60)
            for each in itemDict:
                itemName = str(each).ljust(30, ".")
                # Unit .rjust(calc).ljust() centers the text in the field
                unit = itemDict[each][0]
                unit = unit.rjust(len(unit)
                                  + int((10-len(unit))/2), " ").ljust(10, " ")
                # qty must be converted to a string first, centered on 3 digits
                qty = str(itemDict[each][1])
                qty = qty.rjust(4, " ").ljust(6)
                # FCat put one space in front of str ; sames as (" " + FCat)
                FCat = itemDict[each][2]
                FCat = FCat.rjust(len(FCat)+1, " ").ljust(15, " ")
                print(" " +
                      itemName + "|" +
                      qty + "|" +
                      unit + "|" +
                      FCat
                      )
        elif response.lower() == "s":
            # SQL Search for an item
            itemName = input(
                    "Enter an item Name or just press [Enter] if you'd like " +
                    "to perform a SEARCH by partial name or Food Category.\n" +
                    "[IN]: ")
            print("\nSQL Results: ", checkForItem(ptr, itemName))
        elif response.lower() == "a":
            itemName = input(
                    "Enter an itemName in one of the following formats:\n" +
                    " itemName, a single item name as a text\n"
                    " tuple(Item_Name, Unit_of_Meas., Qty, Food_Category)\n" +
                    " list of tuples (as decribed above)\n" +
                    "[ENTER]: "
                    )
            # Add item to Inventory
            # Manually add an Inventory item using User Inputs
            # (can also feed a tuple), tuple and tuple_list is now
            # handled by addInv()
            print(addInv(connTuple, itemName))

            # *** following not needed with update to addInv) ***
            # Add a whole item and properties as a tuple
            # (or even as a list of tuples)
            ''' print("Add item to Inventory results: ",
                  addInv(connTuple,
                         item=[("butter", "stick", "8", "dairy")])
                  )'''
            # **** End of comment out ***
        else:
            response = ""

        response = ("Quit and close database?\n" +
                    "([Enter] to continue or [q]uit,): ")
        if response.lower() == "q":
            ptr.close()
            raise SystemExit()
        else:
            response = ""

# ===================================================

if __name__ == "__main__":
    # [Test #1] Test the kitchen classes:  Ingredient(), Recipe(), Inventory()
    # from classes.ingredients import Ingredient
    # from classes.recipes import Recipe
    #main()

# --- Write Test Scripts below here ---
# testArgs("gene", "c:\\users\\lifygen\\projects\\python\\")
# testArgs("gene")

    #  # Import old Inventory.txt database into the SQLite Inventory.db
    # Step1 - Retireve old Inventory.txt database info into txtDbInfo
    importDbName = 'Inventory.txt'
    dbName = 'Inventory.db'
    path = "C:\\Users\\Lifygen\\projects\\python\\data\\"
    dbConnTuple = open_db(dbName, path)
    conn = dbConnTuple[0]
    ptr = dbConnTuple[1]
    
    # Import the old Inventory text file database
    fullPath_importDbName = path + importDbName
    # importInv() returns a <dict>
    txtDbInfo = importInv(ptr, fullPath_importDbName)
    # Step 2 - Add each item to the SQLite Inventory.db
    newQty = 0
    for record in txtDbInfo:
        if itemInDb(ptr, record):
            # If item is already in the db then update the SQLite item's qty
            sqlQuery = ("SELECT itemName, qty \
                        FROM Inventory \
                        WHERE itemName = '" + record + "'")
            sqlItemQty = getSqlData(ptr, sqlQuery)
            newQty += float(txtDbInfo[record][1])
            # UPdate the SQLite db item with the new Qty
            ptr.execute("UPDATE Inventory \
                        SET qty = :qty \
                        WHERE itemName = :name;",
                        {'qty':newQty, 'name':record}
                       )
            conn.commit()
        else:
            # Item not in db so add it.
            itemRecord = [(record,
                          txtDbInfo[record][0],
                          txtDbInfo[record][1],
                          txtDbInfo[record][2]
                          )]
            addInv(dbConnTuple, item=itemRecord)
    # Lastly, remove any duplicates in the SQLite database.
    # Or really this should be run once and should not have to be run again.
    itemDict = showInv(ptr, toScreen=True, sendRet=True)
    nicePrint(itemDict)
    print("Inventory before conslidation of duplictes:", itemDict)
    sql_DuplItemsQuery = "SELECT itemName \
                            FROM Inventory \
                            WHERE rowid not in (select min(rowid) \
                                                from Inventory \
                                                group by itemName) \
                            GROUP BY itemName"
    DuplItemsList = getSqlData(ptr, sql_DuplItemsQuery)
    print("Duplicates List: ", DuplItemsList)
    for name in DuplItemsList:
        # name is a Tuple
        consolidateInvItem(dbConnTuple, name[0])
        
    itemDict = showInv(ptr, toScreen=True, sendRet=True)
    nicePrint(itemDict)
    ptr.close()
    conn.close()

'''
#    # Create an SQLite database
    import sqlite3
    conn = sqlite3.connect('mytest.db')
    ptr = conn.cursor()
    sql = """create table students (
        name text,
        username text,
        id int)"""
    # ptr.execute(<sql statement>) executes the sql statement or command
    ptr.execute(sql)
    # closes the connection to the DB (akin to closing a file connection)
    ptr.close()


    # Get data from an SQLite database
    import sqlite3
    conn = sqlite3.connect('mytest.db')
    ptr = conn.cursor()

    # Construct and execute a query
    sql = "Select * FROM Inventory"
    ptr.execute(sql)
    
    # Alternate SQL statement style:  parameterized
    # This is the qmark style:
    cur.execute("insert into people values (?, ?)", 
                (who, age))
    # And this is the named style:
    cur.execute("select * from people \
                 where name_last=:who and age=:age", 
                {"who": who, "age": age})


    # Get the first item from the list in the sqlresult (i.e. one record)
    aRecord = ptr.fetchone()

    # Get all data from the database
    allRecords = ptr.fetchall()
    
    # Close the database
    ptr.close()    

    # This query gets all duplicate itemNames (omitting the first item)
    sql = 'Select * from Inventory \
           where rowid not in (select min(rowid) \
                               from Inventory \
                               group by itemName)'


    # Duplicate name (column) queries
    # This query returns a list of [itemName]s that have duplicates
    # ONce this is run, use the list to generate a list of all duplicates of
    # of each column name with duplicates.
    Select itemName from Inventory 
           where rowid not in (select min(rowid) 
                               from Inventory 
                               group by itemName) group by itemName

    # This query gets All of a specfic itemName (first one and all its duplicates)
    Select * from Inventory 
           where itemName = "tomato sauce" 

    # This query gets all duplicates of a specific itemName (except first one)
    Select * from Inventory 
           where itemName = "tomato sauce" and rowid not in (select min(rowid) 
                               from Inventory 
                               group by itemName)


    # Do whatever you want with the data (allRecords, aRecord) and then 
    # you can WRITE to the database or DELETE from the database.
    # Use DELETE instead of SELECT to delete data.
'''
