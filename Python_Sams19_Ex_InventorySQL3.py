# -*- coding: utf-8 -*-
"""Python_Sams19, p 220, Using SQL to get more out of datbases \
(more SQL Statements).  \
Last chapter created a DB, a Table, write new records and read
This chapter covers, UPDATE, Uniqute (DISTINCT), DELETE, and more complex \
queries.

Created on Tue May 17 10:41:18 2020

@author: Lifygen

# ****************
# Questions, p 220
# ****************
  1] What is the % sign used for in queries?
     [Answer]:  % is a wildcard character(s) replacement similar to \
                Microsoft Windows * search.  Use format where users repalce
                <ch> with one or more string characters:
                  - '<ch>%' : gets all matches beginning with "<ch>"
                  - '%<ch>' : gets all matches ending with "<ch>"
                  - '<ch>%' : gets all matches containing "<ch>"

  2] What happens when more than one item matches the WHERE clause in an
     UPDATE statement?
     [Answer]:  All matches are updated with the data in the UPDATE statement.

  3] How do you sort order the results of a SELECT query?
     [Answer]:  use ORDER by and/or GROUP BY statements.  Examples:
                - ORDER BY [col_name] ASC   #sorts col_name by ascending order
                - ORDER BY [col_name] DESC  #sorts col_name by descending order
                - ORDER BY col1, col2, coln  #sorts by all columns listed

# *****************************************************************
Excercise:  Ch 19 Ex #1, p220 Revise cook's Inventory() from ch 18.
# *****************************************************************
            This Ch 19 Ex #1 excercise description:

#   [1] Inventory Program using SQLite to add

#      a) Ability for the cook to Delete an item from inventory.
#         1. Cook selects Delete item, feeds it a name and the item is
#            immediately deleted from the inventory
#      b) Increment an item quantity found in inventory when an item is added.
#      c) Decrement an item quantity when an item is taken out of inventory.
#      d) Add "Item Description" property (column)
#      e) Allow chef to edit an item, i.e. change an item's -
#         e.1) Name
#         e.2) Description
#         e.3) unit of measure
#         e.4) quantity
#         e.5. Food Category
#      f)  Convert Ch. 18 code to pass the SQLite_connection_obj instead of
#          pointer (aka cursor) and instead of 'connTuple' (or 'dbConnTuple')
#      g)  Convert Ch. 18 Main()), Test Scripts, AddItem() into subdivided
#          functions.
#
#   NOTE:  This file contains the comments and description of Ch 18 Ex #1
#          item 7) so reviewers can view the program criteria all in one place.
#          Ch19 criteria supersedes Ch18 criteria wherever differences exist.
           This Ch 19 criteria is repeated in the overall descrptoin below.
# ***********
"""
"""
Planning:  Workplan/Architecture
Review Requirements and create a workplan:
1)  Create an SQLite db
#  #[status]:  Done, open_db(dbName, *path)

2)  Create a table within the db
#  #[status]:  Done, createTable(conn, TableName)

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
        a.  addNewInvItem()
        b.  removeInvItem() - interpretted this as DELETE
                              Changed in Ch19 to have two functions:
                                  decrInvItem() and
                                  deleteInvItem()
        c.  showInv()
        d.  importInv() - from existing Invntory.txt file
            Existing Text format:  <itemName_str><sp><(unit_str)><tab><qty_int>
#  #[status] Done, use importInv(conn, importFile) and feed return into
             addNewInvItem()

5)  SearchInv() - a. creates an SQL query based on UserInput
                  b. executes the SQL query
                  c. prints results
                    c1.  msg # of items in Inv
                    c2.  msg "Item is not in Inv"
#  #[status]: Done, a. checkForItem(conn, searchItem=""), returns item and qty
                    b. itemInDb(), returns True if item in Db otherwise False

6)  Extra Credit:
    6.1)  Create function that outputs whole Inventory (to screen)
#  #[status]: Done, see showInv(conn, toScreen=True, sendRet=False)

    6.2)  alter 6.1 so that it Shows -
                whole Inventory, or
                filtered by Category, and/or
                by "begins with" letter(s) of item name
#  #[status]: Done, see output of  checkForItem(conn, searchItem="")

    6.3)  Optionally print and/or return the Inventory (as <dict> "item":qty)
#  #[status]: Done, Demonstrated in the return of both importInv() & showInv()

    6.4)  Eliminate duplicates in SQLite db and have duplicate adds increment\
          the quantity in the Inventory.db (which is a SQLite db)
#  #[status]: Done, consolidatation done in Script, addInvItems()
"""
"""
#   7. Chapter 19 Excercise #`
#   [1] Inventory Program using SQLite to add
#      a) Ability for the cook to Delete an item from inventory.
#          1. Cook selects Delete item, feeds it a name and the item is
#             immediately deleted from the inventory
#       [Status]:  Done, deleteInvItem(conn, itemName)

#      b) Increment an item quantity found in inventory when an item is added.
#       [Status]: Done, incrInvItem()

#      c) Decrement an item quantity when an item is taken out of inventory.
#       [Status]: Done, decrInvItem()

#      d) Add "Item Description" property (column)
#       [Status]: Done, addTableField()
                  Created above f(x) instead of having t always perform manual
                  action below:
                  # Add a column to an existing Table:
            ptr.execute("ALTER TABLE Inventory ADD COLUMN Description text")
                   a = ptr.execute("PRAGMA table_info(Inventory);")
                   a.fetchall()
                  [(0, 'itemName', 'text', 0, None, 0),
                   (1, 'unit', 'text', 0, None, 0),
                   (2, 'qty', 'int', 0, None, 0),
                   (3, 'FoodCategory', 'text', 0, None, 0),

            if "Description" NOT FOUND" then SQL Command:
            ptr.execute("ALTER TABLE Inventory ADD COLUMN Description text")
            result this added to table: (4, 'Description', 'text', 0, None, 0)]

#      e) Allow chef to edit an item, i.e. change an item's -
#         e.1) Name
#         e.2) Description  [note:  run addTableField() manually
#                                   instead of from menu.]
#         e.3) unit of measure
#         e.4) quantity
#         e.5) Food Category
#       [Status]: Done, editItem(conn, itemName), addTableField()

#      f)  Convert Ch. 18 code to pass the SQLite_connection_obj instead of
#          pointer (aka cursor) and instead of 'connTuple' (or 'dbConnTuple')
#       [Status]:  Done.  Verify by inspection of code.

#      g)  Convert Ch. 18 Main(), Test Scripts, AddItem() into subdivided
#          functions.
#       [Status]: Done, main(), tablePrint(), check_itemName_format(),
                        main_menu(), importInv()

#      h)  Consolidate Duplicates - tally up qty of duplicates, update the
           master item with the new (consolidated) quantity and delete the
           duplicates.
        [Status]: Done, see consolidateInvItem(conn, itemName).  Wrote f(x)
                  from the script that was created in Ch18 excercise.

"""

import sys
import os
import sqlite3
from datetime import datetime
from classes.ytcClasses import isfloat
from classes.ytcClasses import str_to_float_or_int


def open_db(dbName, path=""):
    """Attempt to open an SQLite db. If it does not exist then create it.\n
    Package Requirements:  sqlite3, \
                           os

    INPUTs:
    ------
    :dbName (str): - SQLite database filename.
    :path (karg str): - key argument string of the path to the folder where\
                          the SQLite database resides.

    OUTPUTs:
    ------
    :return (SQLite_IOconn_obj): -  a database connection_obj.
    """
    print("path = ", path)
    # Handle the optional path input, ensure it has a / or \\ ending and
    # create the full file path name to use in creating/opening the db.
    if not path:
        fullPathFileName = os.getcwd() + '\\data\\' + dbName
        print("set in NOT PATH")
    else:
        length = len(path) - 1
        if path[length] in ('\\', '/'):
            fullPathFileName = path + dbName
        else:
            fullPathFileName = path + '\\' +  dbName
    # Get SQLite database connection (file iostream)
    conn = sqlite3.connect(fullPathFileName)
    print("path = ", path)
    print("fullPathFileName = ", fullPathFileName)
    return (conn)


def createTable(conn, TableName):
    """Create the proper Inventory table structucture within the database.\n
    Package Requirements:  (sqlite3):

    INPUTS:
    ------
        :conn (cursor_obj): - pointer into the opened SQLite database.

    OUTPUTS:
    -------
        :return (bool): - True:  Sucessfully created table.
                        - False: Failed to create table.
    """
    ptr = conn.cursor()
    sql = """create table :TableName (
        itemName text,
        unit text,
        qty int,
        FoodCategory text)"""
    try:
        ptr.execute(sql, {"TableName": TableName})
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
        print("An unexpected error occurred in createTable(conn):",
              sys.exc_info()[0])
        full_errMsg = ""
        for errMsg in err.args:
            full_errMsg += (errMsg.capitalize() + ".  ")
        print(full_errMsg)
        ptr.close()
        return False
    ptr.close()
    return True


def addTableField(dbName, tableName, newColumn, newColDataType, path=""):
    """Add a new column to a database Table.  Checks for the existence of the
    column before trying to add a new one.
    """
    fieldAlreadyExists = False
    if not path:
        fullPathFileName = os.getcwd() + '\\data\\' + dbName
    else:
        length = len(path) - 1
        if path[length] in ('\\', '/'):
            fullPathFileName = path + dbName
        else:
            fullPathFileName = path + "/" + dbName
    # Get SQLite database connection (file iostream)
    conn = sqlite3.connect(fullPathFileName)
    # Check if the Field (a.k.a. column) already exists in the Table
    ptr = conn.cursor()
    # This Works
    sqlPragma = ("PRAGMA table_info={aTable};".
                 format(aTable=tableName)
                 )
    ptr.execute(sqlPragma)
    # PRAGMA returns a list of tuples, where each tuple contains Table Field
    # info, including the fieled Name.
    existingFields = ptr.fetchall()
    # Check to see if the newField to be added is already in the Table
    for field in existingFields:
        if newColumn in field:
            fieldAlreadyExists = True
            break
    # Go ahead and add the newField if it does not already exist
    if not fieldAlreadyExists:
        sqlNewField = ("ALTER TABLE {aTable} ".format(aTable=tableName) +
                       "ADD COLUMN {fieldInfo}".
                       format(fieldInfo=(newColumn+ " " + newColDataType))
                       )
        ptr.execute(sqlNewField)
        conn.commit()
    else:
        print("[" + newColumn + "] is arleady a field column in the [" +
              tableName + "] SQLite table."
              )
    ptr.close()



def addNewInvItem(conn, itemName="", unit="", qty="", FCat="", item=[]):
    """Add inventory item into the SQLite database\n
    Package Requirements:  sqlite3, \
                           ytcClasses.isfloat,\
                           ytcClasses.str_to_float_or_int

    INPUT:
    ------
      :conn (cursor_obj): - pointer into the opened SQLite database.
     :itemName (str or tuple list):   - name of item or a list of items in\
                                        [(item_data)] formaat.
     :unit (str):       - unit of measure,
                          (ex. lb, oz, each, can, frzn, bag, box, jug, \
                           bottle, etc.)
     :qty (float/int):  - item quantity
     :FCat (str):       - Food Category:  (none, veg, fruit, meat, grain, \
                          dairy, oil, spice)
     :item (list[(tuple)]): - item entry as a list of one or more tuples.
                           Formatted as follows:  [(itemName, unit, qty, FCat)]

    OUTPUT:
    ------
        :return (bool): - True:  for successful addition;
                        - False: otherwise

    Input conditioning/handling:
    Check input format, if the <item> arg is a list object with a single item
    or two item tuple then assume it is [(itemName)] or [(itemName, qty)]
    format and re-assign the values in the item[()] tuple list such that the
    tuple within the list is a 4-element-tuple:  [(itemName, , qty, )].  If a
    single item (itemName) was passed without other values then assign: qty = 0

    Code was implemented in this way to provide convenience in performing
    manual f(x) calls (presumption of adding existing items) and allowing
    auotomated textfile database imports.
    """
    # Initialize variables
    status = False
    duplicate = False
    exitList = ('quit', 'exit', 'q', 'x', 'e')
    FCatList = ('none', 'veg', 'fruit', 'meat', 'grain', 'dairy', 'oil',
                'spice')

    # Pre-condition inputs in case multiple info overloaded into <itemName>
    if ((not item) or (item == []) or (item == [()])):
        addItemsManually = True
        if (type(itemName) is list):
            item = itemName
            itemName = item[0][0]
            if len(item[0]) == 2:
                if isfloat(item[0][1]):
                    qty = str_to_float_or_int(item[0][1])
                else:
                    unit = item[0][1]
            item = []
    else:
        addItemsManually = False

    # Handle and condition inputs
    if ((not item) or (item == [()])):
        print("Let's add an item(s) to the inventory!")
        while addItemsManually:
            while not itemName:
                itemName = input("[Add New Item Menu] - Enter Item's name " +
                                 "(or [q]uit/e[x]it): ")
                if not itemName:
                    print("Invalid name, try agin.")
                elif itemName.lower() in exitList:
                    status = True
                    addItemsManually = False
                    # used to break out of the top level While w/o executing
                    # the other sub-While loops.
                    itemName = 'quit'

            """Check for itemName in SQLitedb"""
            # If in SQLdb then collect qty and add that qty to the db
            # otherwise keep processing as normal.
            duplicate = itemInDb(conn, itemName)

            while not unit and itemName != 'quit' and not duplicate:
                unit = input("Input item's unit of measure " +
                             "[default = '(each)']: ")
                if not unit:
                    unit = "(each)"
                elif str(unit)[0] != "(":
                    unit = "(" + str(unit) + ")"

            while ((not qty) and (itemName != 'quit')):
                qty = input("Input quantity: ")
                if isfloat(str(qty)):
                    qty = str_to_float_or_int(qty)
                else:
                    print("Invalid quality.  Try Again.")
                    qty = 0

            while ((not FCat) and (itemName != 'quit')) and not duplicate:
                FCatListTxt = ""
                for each in FCatList:
                    FCatListTxt += each + ", "
                FCat = input("Input Food Category: \n[{}]: ".
                             format(FCatListTxt))
                if ((not FCat) or (FCat not in FCatList)):
                    FCat = "none"

            if (itemName != 'quit'):
                if not duplicate:
                    # create an item list of tuples for the write segment
                    item.append((itemName, unit, qty, FCat))
                elif duplicate:
                    # Handle the Duplicate by adding it's qty to SQLite db
                    # Note, duplicates are not put into the <item> list of tuples
                    incrInvItem(conn, itemName, qty)
            else:
                # Exec Should never get here, if it does something went wrong!
                itemName = 'quit'
                status = False
                print("Something went drastically wrong in " +
                      "addNewInvItem()!\n" +
                      "However, execution is continuing...")
            # Reset variables for next item addition iteration
            itemName = ""
            unit = ""
            qty = ""
            FCat = ""
    # Write Segement, also handles and conditions  <input> argument
    if itemName != quit:
        # type(itemName) in (list, tuple) and not duplicate
        # Items are in item[] list; add these to the database.
        for each in item:
            if len(each) == 1:
                each = (each[0], "", 0, "")
            elif len(each) == 2:
                if isfloat(item[0][1]):
                    each = (each[0], "", each[1], "")
                else:
                    each = (each[0], each[1], 0, "")
            elif len(each) == 3:
                each = (each[0], each[1], each[2], "")
            itemName = each[0]
            # check for duplicate
            if itemInDb(conn, itemName):
                # Handle Duplictes by adding their qty to SQLite db
                incrInvItem(conn, itemName, qty)
            unit = each[1]
            if not unit:
                unit = "(each)"
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
        writeInv(conn, (itemName, unit, qty, FCat))
        status = True
    return status


def writeInv(conn, itemTuple):
    """Writes inventory data into the SQL database and commits the changes.\n
    Package Requirements:  sqlite3.

    INPUTS:
    ------
      :conn (cursor_obj):\
          - Tuple of the datbase connector and cursor (aka pointer).   \
            Format:  (conn_obj, ptr_obj)
      :itemTuple (tuple):\
          - Tuple of the item to be added to the database. Format:     \
            (itemName, unit, qty, FCat), where FCat is the Food Category.\n
    OUTPUTS:
    ------
        none
    """
    # Write item and commit Inventory change to SQLite db.
    ptr = conn.cursor()
    # Gets a list of all duplicate items
    # (first item in the duplicate is omitted)
    sql = """insert into Inventory
            (itemName, unit, qty, FoodCategory)
             values
                 (:itemName, :unit, :qty, :FoodCategory)"""
    ptr.execute(sql, {'itemName':itemTuple[0],
                          'unit':itemTuple[1],
                           'qty':itemTuple[2],
                  'FoodCategory':itemTuple[3]})
    # Writes or commits the data to the database
    conn.commit()
    ptr.close()


def getSqlData(conn, sqlQuery, sqlQueryDict={}):
    """Execute the SQL query statement and return the results.\n
    Package Requirements:  sqlite3.

    INPUT:
    ------
      :conn (cursor_obj): - pointer into the opened SQLite database.
      :sqlQuery (SQLquery_obj): - SQL query statement.
      :sqlQueryDict (dict): - dictionary definining variables in sqlQuery

    OUTPUT:
    ------
:return (list): - the results of the query in a list.
    """
    ptr = conn.cursor()

    # Execute the SQL statement and store results in <results> variable
    sqlResults = ptr.execute(sqlQuery, sqlQueryDict)
    # Fetch all the items in sqlResults
    retValue = sqlResults.fetchall()
    ptr.close()
    return retValue


def itemInDb(conn, itemName):
    """Check for an item name in Inventory.  Return True/False"""
    ptr = conn.cursor()
    sqlResults = ptr.execute("SELECT * \
                              FROM Inventory \
                              WHERE itemName=:itemName",
                             {"itemName": itemName})
    if not sqlResults.fetchall():
        ptr.close()
        return False
    ptr.close()
    return True


def putProperty(conn, itemName, propValue, propName=""):
    """Edit an Inventory item property, i.e. take the User's input and write/\
    commit the input as a change in the database.
    """
    ptr = conn.cursor()
    ptr.execute("UPDATE Inventory SET " + propName + " = " + propValue +
                " WHERE itemName = '" + itemName + "';")
    conn.commit()
    ptr.close()
    return True


def incrInvItem(conn, itemName, addQty):
    """Decrement the quantity of an inventory 'item' in the SQLite database.

    INPUT:
    ------
      :conn (cursor_obj): - pointer into the opened SQLite database.
      :itemName (str): - name of the item to be removed from inventory.
      :addQty (float/int): - quanity of item being added to inventory.

    OUTPUT:
    ------
        :return (float): - New quantity of the item's qty in inventory.
    """
    ptr = conn.cursor()
    # since item is already in the db, update the SQLite item's qty
    sqlQuery = ("SELECT qty \
                 FROM Inventory \
                 WHERE itemName = :itemName")
    ptr.execute(sqlQuery, {'itemName': itemName})
    sqlItemQty = ptr.fetchone()
    # sqlItemQty should be a single item <tuple>
    newQty = float(addQty) + float(sqlItemQty[0])
    # UPdate the SQLite db item with the new Qty
    ptr.execute("UPDATE Inventory \
                 SET qty = :qty \
                 WHERE itemName = :itemName;",
                {'qty': newQty, 'itemName': itemName}
                )
    conn.commit()
    ptr.close()
    return True


def decrInvItem(conn, itemName, remQty):
    """Decrement the quantity of an inventory 'item' in the SQLite database.

    INPUT:
    ------
      :conn (cursor_obj): - pointer into the opened SQLite database.
      :itemName (str): - name of the item to be removed from inventory.
      :remQty (float/int): - quanity of item being removed from inventory.

    OUTPUT:
    ------
        :return (float): - New quantity of the item's qty in inventory.
                           A negative value means more items were attmpted for\
                           removal than were in inventory.  Inventory qty will\
                           show 0 qty but the remainder of items attempted for
                           removal are returned as a negative number. (i.e. \
                           the chef or buyer needs to buy these many items to
                           fulfill the recipe item request.
    """
    ptr = conn.cursor()
    # Decrement the item already in the SQLite db by the item's remQty.
    sqlQuery = ("SELECT qty \
                 FROM Inventory \
                 WHERE itemName = :itemName")
    ptr.execute(sqlQuery, {'itemName': itemName})
    sqlItemQty = ptr.fetchone()
    newQty = float(sqlItemQty) - float(remQty)
    if newQty < 0:
        newQty_stored = 0
    else:
        newQty_stored = newQty
    # UPdate the SQLite db item with the new Qty
    ptr.execute("UPDATE Inventory \
                 SET qty = :qty \
                 WHERE itemName = :itemName;",
                {'qty': newQty_stored, 'itemName': itemName}
                )
    conn.commit()
    ptr.close()
    return newQty


def deleteInvItem(conn, itemName):
    """Deletes all records (i.e. rows) that meet the sql statement criteria. \
    :conn (connect_obj):= SQLite IOstream connection object.
    :itemName (str): = item name
    """
    ptr = conn.cursor()
    sql = 'DELETE FROM Inventory WHERE itemName=?'
    ptr.execute(sql, (itemName,))
    conn.commit()
    ptr.close()


def consolidateInvItem(conn, itemName):
    """ Consolidate duplicate rows, keeps lowest numbered ID and adds \
    duplicate items' qty to it.

    INPUTS:
      :conn (cursor_obj):\
          - Tuple of the datbase connector and cursor (aka pointer).   \
            Format:  (conn_obj, ptr_obj)
    """
    ptr = conn.cursor()

    # This query gets All of a specfic itemName;
    # (the first one and all its duplicates)
    ptr.execute("Select itemName, qty \
                               from Inventory \
                               WHERE itemName = :item",
                               {'item': itemName})
    sql_ItemName = ptr.fetchall()
    newQty = float(0)
    for record in sql_ItemName:
        newQty = newQty + float(record[1])
    ptr.close()

    print("\nAfter newQtyCalc")
    tablePrint(showInv(conn, toScreen=True, sendRet=True))

    # Update the Quantity of the item
    ptr_update = conn.cursor()
    # This works:
    #sql_update = '''UPDATE Inventory
    #                SET qty = "{qty}"
    #                WHERE itemName = "{name}"
    #                AND rowid IN (SELECT min(rowid)
    #                              FROM Inventory
    #                              WHERE itemName = "{itemName}")'''
    #sql_update = sql_update.format(qty=newQty, name=itemName, itemName=itemName)
    #ptr_update.execute(sql_update)
    ptr_update .execute('''UPDATE Inventory
                           SET qty = :qty
                           WHERE itemName = :itemName
                           AND rowid IN (SELECT min(rowid)
                                          FROM Inventory
                                          WHERE itemName = :itemName
                                          )''',
                        {'qty': newQty,'itemName':itemName}
                        )
    conn.commit()
    print("After UPdate")
    tablePrint(showInv(conn, toScreen=True, sendRet=True))
    ptr_update.close()

    # DELETE all a specific itemName's duplicates (excluding original one)
    ptr_delete = conn.cursor()
    sql_DuplicateItems = "DELETE \
                          FROM Inventory \
                          WHERE itemName = :itemName \
                          and rowid not in (SELECT min(rowid) \
                                            from Inventory \
                                            group by itemName)"
    ptr_delete.execute(sql_DuplicateItems, {"itemName": itemName})
    conn.commit()
    ptr_delete.close()

    print("\nThis is the new quantity Total: {} \n".format(newQty))
    print("After Delete")
    tablePrint(showInv(conn, toScreen=True, sendRet=True))


def showInv(conn, toScreen=True, sendRet=False):
    """Show all items in the inventory [itemName, unit, qty, category].

    Package Requirements:  sqlite3.

    INPUTS:
    ------
        :conn (cursor_obj): - pointer into the opened SQLite database.
        :toScreen (bool): - True:  prints to screen.
                          - False:  no print, only return value

    OUTPUTS:
    ------
        :print to screen: - prints to screen if 'toScreen' is True
        :return (dictionary): - {name:[qty, unit, FCat]}, \
                               where FCat = Food Category
    """
    sqlQuery = "Select * from Inventory"
    all_results = getSqlData(conn, sqlQuery)
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


def checkForItem(conn, searchItem="", SeachLike = False):
    """Check to see if an item is in the inventory SQLite database.

    INPUT:
    ------
      :conn (cursor_obj): - pointer into the opened SQLite database.
      :searchItem (str): - name of the item to be searched for in inventory.

    OUTPUT:
    ------
      :return (tuple): - Tuple, if item is in inventory. \
                             Format:  (itemName, unit, qty, category)
                        - Tuple if item has a 0 qty and print message:  \
                          "Out of stock."
                        - NULL Tuple, if item is not found and print message:  \
                          "Item type does not exist in the inventory; try \
                          adding it with qty=0."
    """
    # Build Select statement
    if (type(searchItem) == str and searchItem):
        if SeachLike:
            sqlQuery = ("SELECT * " +
                        "FROM Inventory " +
                        "WHERE itemName like '" + searchItem + "%' " +
                        "ORDER BY itemName ASC"
                        )
        else:
            sqlQuery = ("SELECT * " +
                        "FROM Inventory " +
                        "WHERE itemName ='" + searchItem + "' " +
                        "ORDER BY itemName ASC"
                        )
        queryResult = getSqlData(conn, sqlQuery)
        if not queryResult:
            print('\n"' + searchItem + '" type does not exist in the ' +
                  'inventory; try adding it with qty=0.\n'
                  )
        else:
            qty = str(queryResult[0][2])
            unit = queryResult[0][1]
            itemName = queryResult[0][0]
            print('\nSearch for "' + searchItem +
                  ' yielded the following results":'
                  )
            tablePrint(queryResult)
            if queryResult[0][2] == 0:
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
                 "          3 - return [itemName, Food Category]\n" +
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
    startsWith = input("Add ""Search-by-name"" by entering an item name or " +
                       "the first few letters of it, or press \n" +
                       "[Enter] to skip.\n" +
                       "[IN]: ")
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

    all_results = getSqlData(conn, sqlQuery)

    tablePrint(all_results)
    return all_results


def editItem(conn, itemName):

    sqlEditQuery = ('''Select itemName, unit, qty, FoodCategory, Description
                    FROM Inventory
                    WHERE itemName = :itemName''')
    sqlQueryDict = {'itemName': itemName}
    resultsEditQuery = getSqlData(conn, sqlEditQuery,sqlQueryDict)
    # convert results to a dictionary with itemName as the key
    #
    resultDict = {resultsEditQuery[0][0]:[]}
    for i in range (1,len(resultsEditQuery[0])):
        resultDict[resultsEditQuery[0][0]].append(resultsEditQuery[0][i])
    print(resultsEditQuery)
    print(resultDict)
    tablePrint(resultDict)
    if resultsEditQuery[0][4]:
        print("\n[" + itemName + " Description]:  " + resultsEditQuery[0][4])
    else:
        print("\n[" + itemName + " Description]:  *blank*")
    # Show edit menu
    selection = ""
    FCatList = ('none', 'veg', 'fruit', 'meat', 'grain', 'dairy', 'oil',
                'spice')
    itemProperty = {1:'itemName',2:'qty',3:'unit',
                    4:'FoodCategory',5:'Description'}
    while not selection:
        response = ""
        selection = input("[Edit Menu] - Select a property# to edit:\n" +
                          "[1]item name\n" +
                          "[2]qty\n" +
                          "[3]unit\n" +
                          "[4]Food Category\n" +
                          "[5]Description\n" +
                          "[q]uit\n" +
                          "[<-{IN]: "
                          )
        if isfloat(selection):
            selection = int(selection)
        if str(selection).lower() in ["q"]:
            selection = ""
            return
        elif selection in [1]:
            response = input("Enter new Item NAME: ")
            response = "'" + response.strip('"').strip("'") + "'"
        elif selection in [2]:
            while not isfloat(response):
                response = input("Enter new Item QUANTITY: ")
            putProperty(conn, itemName, response, itemProperty[selection])
            return
        elif selection in [3]:
            response = input("Enter new Item UNIT of measure: ")
            if str(response)[0] != "(":
                response = "(" + str(response) + ")"
        elif selection in [4]:
            while not response:
                print(FCatList)
                response = input("Enter new Item Food Category: ")
                if response not in FCatList:
                    response = ""
        elif selection in [5]:
            response = input("Enter new Item Description: ")
        else:
            print("INVALID selection, try again.")
        # Allow using a contraction like <can't> without the user having to
        # enter double quotes.
        response = response.strip('"').strip("'")
        response = response.replace("'","''").replace('"','""')
        response = "'" + response.strip('"').strip("'") + "'"
        putProperty(conn, itemName, response, itemProperty[selection])

                #Continue to finish code here ********************************************


def importInv(connSQL, importFile, debug=False):
    """Import inventory items from existing "Inventory.txt" file and translate
       them into the new SQLite database.

    Old [*.txt] database format:  <itemName_str><sp><(unit_str)><tab><qty_int>

    INPUTS:
    ------
      :connSQL (cursor_obj): - pointer into the opened SQLite database.
      :importFile (str): - full path filename of the text database to
                           translate into the SQLite database.

    OUTPUTS:
    ------
        none, just performs writes to the new SQLite database.

    Developed from test script. Could be further subdivided into three f(x):
        - f1(x): get_oldTextDb:
        - f2(x): examine_oldTextDb_AddOrUpdate:
        - f3(x): consolidateInvItem(conn, itemName):
    """
    ptrSQL = connSQL.cursor()

    # --------------------------
    # Get old text file database
    # --------------------------
    # Open textfile IOStream connection
    f = open(importFile)
    oldTxtDb = f.readlines()
    f.close()
    # Build a dictionary to hold the data from the textfile
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

    # --------------------------------------------------
    # Examine old textfile data and either -
    #      - UPDATE qty in the SQLite database or
    #      - ADD newitem record to the SQLite database.
    # --------------------------------------------------
    # Should now be able to just construct a tuple list and use:
    # "addNewInvItem(conn, item=[])" and comment out this code.
    newQty = 0
    for record in oldTxtDB:
        if itemInDb(connSQL, record):
            # If item is already in the db then update the SQLite item's qty
            # Get SQLite qty for the item, used to calc new total qty (newQty)
            sqlQuery = ("SELECT itemName, qty \
                        FROM Inventory \
                        WHERE itemName = '" + record + "'")
            sqlItemQty = getSqlData(connSQL, sqlQuery)
            newQty = float(sqlItemQty[0][1]) + float(oldTxtDB[record][1])
            # UPdate the SQLite db item with the new Qty
            ptrSQL.execute("UPDATE Inventory \
                            SET qty = :qty \
                            WHERE itemName = :name;",
                           {'qty': newQty, 'name': record}
                           )
            connSQL.commit()
        else:
            # Item not in db so add it.
            itemRecord = [(record,
                          oldTxtDB[record][0],
                          oldTxtDB[record][1],
                          oldTxtDB[record][2])]
            addNewInvItem(connSQL, item=itemRecord)

    # ----------------------------------------------------------------------
    # Lastly, remove any duplicates in the SQLite database.
    # Or really this should be run once and should not have to be run again.
    # ----------------------------------------------------------------------
    # Should no longer need this after Conolidate is run the once.  The new
    # AddInvItem() should handle duplicates UPDATED vs. newItems ADDED.
    # Call "consolidateInvItem(conn, itemName) once from main() as an option.
    # ----------------------------------------------------------------------
    # Check for and remove duplicates in the SQLite database.
    itemDict = showInv(connSQL, toScreen=True, sendRet=True)

    if debug:
        print("\nInventory BEFORE consolidation of duplicates:",
              tablePrint(itemDict))

    sql_DuplItemsQuery = "SELECT itemName \
                            FROM Inventory \
                            WHERE rowid not in (select min(rowid) \
                                                from Inventory \
                                                group by itemName) \
                            GROUP BY itemName"
    DuplItemsList = getSqlData(connSQL, sql_DuplItemsQuery)
    if debug:
        print("\nDuplicates List: ", DuplItemsList)
    # Consolidate any duplicates in the SQLite db
    for name in DuplItemsList:
        # name is a Tuple
        consolidateInvItem(connSQL, name[0])

    if debug:
        itemDict = showInv(connSQL, toScreen=True, sendRet=True)
        print("\nInventory AFTER consolidation of duplicates:",
              tablePrint(itemDict))

    return itemDict


def invList_to_Dict (invList):
    """Convert an inventory record list or list of ingredient tuples or \
               a list of dictionary itmes into a dictionary format (<dict>).  \
               Primarily useful for printing it to screen using the \
               tablePrint(itemDict). Note, SQL queries returns lists of tuples.
    """
    dictionary = {}
    if type(invList) == dict:
        dictionary = invList
    elif type(invList) == list:
        if type(invList[0]) == dict:
         # If fed a list of dictionary items then convert the list into a
         # dictionary
         for dictRecord in invList:
             dictionary.update(dictRecord)
        elif type(invList[0])in (list, tuple):
        # If fed a list of sublists or tuples then convert the tuple or sublist
        # into dictionary entries where the first item is the key for each entry
        # and put these all into one dictionary.
            for record in invList:
                dictRecord = {record[0]:[]}
                # 'i' is the record # of the list/tuple location within the
                # parent list.
                for i in range (1,len(record)):
                    dictRecord[record[0]].append(record[i])
                    dictionary.update(dictRecord)
        elif type(invList[0]) == str:
        # Looks like a list of records (as a tuple or list_ was fed in
            dictRecord = {invList[0]:[]}
            # 'i' is the field position within the record
            for i in range (1,len(invList)):
                dictRecord[invList[0]].append(invList[i])
                dictionary.update(dictRecord)
        else:
            print("invList_to_Dict() ERROR #1, did not know how to " +
              "the input type.  Use a dictionary, list of dictionaries, or " +
              "handle list of inventory records (either a list or tuple).")
    else:
        print("invList_to_Dict() ERROR #2, did not know how to " +
              "the input type.  Use a dictionary, list of dictionaries, or " +
              "handle list of inventory records (either a list or tuple).")
    return (dictionary)


def tablePrint(itemDict):
    """Print the Inventory out as a table to the screen.\n
    Updated to allow an SQL_Query_return or list of tuples (which is the same
    thing as a list of inventory records). as the input.

    INPUTS:
    ------
      :itemDict (<dict>/<list>): - single item in dictionary format
                                 - a list of items in dictionary format
                                 - a list of item records (in either list \
                                   or tuple format)


    OUTPUTS:
    ------
        :return (<dict>): - dictionary list in the following format:
                            [{itemName: qty, unit, category, Description}]
"""
    # Condition the input.  Convert it to dictionary format if it is not
    # already in that format. (single item or list of items)
    itemDict = invList_to_Dict (itemDict)
#    if type(itemDict) in (tuple, list):
#        itemDict = invList_to_Dict (itemDict)

    Header = (" Item Name".ljust(31, " ") + "|" +
                    " Qty".ljust(6, " ") + "|" +
                    "Unit".ljust(7).rjust(10) + "|" +
          " Food Category".ljust(15)
              )
    print("\n" + Header)
    print(" " + "-"*60)
    if itemDict:
        for each in itemDict:
            itemName = str(each).ljust(30, ".")
            # Unit .rjust(calc).ljust() centers the text in the field
            unit = itemDict[each][0]
            unit = unit.rjust(len(unit) + int((10-len(unit))/2),
                              " ").ljust(10, " ")
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
    else:
        print("[tablePrint() | Error]:  NULL item passed into itemDict.")


def main_menu():
    """Allows user to choose an item from te main_menu. return is the \
       selection in all lower case.
    """
    """Note:  I think this code is fine to have in 'main()' but they
              Python module shows this as a separate f() so I have
              broken this out to a separate f(x) module.
    """
    selection = input("[Main Menu] - Do you want to: \n" +
                      "[a]dd an item\n" +
                      "[d]elete an item\n" +
                      "[e]dit an item\n" +
                      "[s]earch for an item in inventory\n" +
                      "[p]rint the whole inventory\n" +
                      "[i]mport old textfile Inventory database.\n" +
                      "[q]uit\n" +
                      "[IN]: "
                      )
    return selection.lower()


def check_itemName_format(itemName="", debug=False):
    """Check the itemName to see if it should be converted to a list item.
    OUTPUT:
    ------
    return: (tuple): - tuple of the (itemName, searchLike), where searchLike \
                       is a flag to turn on/off the SQL seach "Like" wildcard.
    """
    searchLike = False
    if not itemName:
        itemName = input('<-{INput "Search text"]: ')
        searchLike = True
    itemName = itemName.strip("[").strip("]").strip("(").strip(")")
    itemName = itemName.split(",")
    i = 0
    for each in itemName:
        itemName[i] = itemName[i].strip(' ').strip('"').strip("'")
        i += 1
    itemName = [tuple(itemName)]
    if len(itemName[0]) in (1, 2, 4):
        if len(itemName[0]) == 1:
            itemName = itemName[0][0]
    else:
        print("Unrecognized input format, try again.")
        return ""
    return (itemName, searchLike)


#
# *** MAIN Program
# ===================================================
def main():
    """ MAIN PROGRAM that solicts input from the User until Quit is selected.
    # 1)a: Add new SQLite Inventory db items.
    # 2)d: Delete an item from the SQLite database.
    # 3)e: Edit a database item.
    # 4)s: Search for an item in the SQLite Inventory db.
    # 5)p: Print the whole inventory to screen.
    # 6 i: Import old textfile Inventory database.
    # 7)q: Quit the program
    print("Create Table resuls: ", createTable(conn, "Inventory"))
    NOTE:  SQLqueries return a list of tuples [()].
    """
#    print("\nHello World!\t",
#          datetime.today().strftime("%a, %b %d, %Y    %I:%M:%S")
#          )
    dbName = 'Inventory.db'
    path = "C:\\Users\\Lifygen\\projects\\python\\data\\"
    exitList = ('quit', 'exit', 'q', 'x', 'e')

    open_db(dbName, path)
    conn = open_db(dbName, path)

    menuSelection = ""
    itemName = ""
    while not menuSelection:
        menuSelection = main_menu()
        if menuSelection == "q":
            itemName = ""
        # [I]mport inventory from old textfile database
        elif menuSelection == "i":
            # No need to get input from User; should be a known static db names
            importDbName = 'Inventory.txt'
            fullPath_importDbName = path + importDbName
            # importInv() returns a <dict> of the database.
            # debug=True, Shows SQLite database before and after the import.
            txtDbInfo = importInv(conn, fullPath_importDbName, debug=True)
        # [P]rint the iventory as a table to the screen
        elif menuSelection == "p":
            # Show Inventory as a printed Table
            itemDict = showInv(conn, toScreen=True, sendRet=True)
            tablePrint(itemDict)
        # [S]earch for an item in the inventory
        elif menuSelection == "s":
            # Turn Off the wildcard Search for 'like" flag by default
            SearchLike = False
            # SQL Search for an item
            itemName = input(
                "\n" +
                "Enter an item Name or just press [Enter] if you'd like " +
                "to perform a SEARCH by partial name or Food Category.\n" +
                "[itemName]: "
                )
            itemName = check_itemName_format(itemName)
            SearchLike = itemName[1]
            itemName = itemName[0]
            if itemName in exitList:
                # itemName = ""
                menuSelection = ""
                continue
            itemCheckMsg = checkForItem(conn, itemName, SearchLike)
            if not itemCheckMsg:
                print("Try again or choose a new menu item.")
            else:
                print("\nSQL Results: \n", tablePrint(itemCheckMsg))
        # [E]dit an item in inventory
        elif menuSelection == "e":
            itemName = ""
            # First ensure that the new [Description] field exists
            addTableField(dbName, "Inventory", "Description", "text", path)
            # Second Check that the item exists in the Inventory database
            while not itemName:
                itemName = input(
                        "\n" +
                        "Enter a single itemName (as text) to EDIT,\n" +
                        "[itemName]: ")
                if itemName.lower() in exitList:
                    itemName = ""
                    menuSelection = ""
                    break
                itemCheckMsg = checkForItem(conn, itemName)
                if not itemCheckMsg:
                    print('Since "' + str(itemName) + '" is not in the ' +
                          'inventory database,  Try Again.'
                          )
                    itemName = ""
                else:
                    itemName = itemCheckMsg[0][0]
                    if len(itemCheckMsg) > 1:
                        print('Search for ""' + itemName + '"" turned up ' +
                              'multiple items.  Refine your entry, quit, or ' +
                              'continue with the selection shown.')
                        for each in itemCheckMsg:
                            print(each)
                        tablePrint(itemCheckMsg)
                    print("\nCurrent selection = " + itemName)
            # Call up the edit menu
            if itemName and itemName not in exitList:
                editItem(conn, itemName)
                tablePrint(checkForItem(conn, itemName))
        # [D]elete an item from inventory
        elif menuSelection == "d":
            itemName = input(
                "\n" +
                "Enter a single itemName to DELETE as text,\n" +
                "[itemName]: ")
            deleteInvItem(conn, itemName)
        # [A]dd an ingredient to the inventory
        elif menuSelection == "a":
            itemName = input(
                "\n" +
                "Enter an itemName in one of the following formats:\n" +
                " itemName, a single item name as a text\n" +
                " tuple(Item_Name, Unit_of_Meas., Qty, Food_Category)\n" +
                " list of tuples (as decribed above)\n" +
                "[itemName]: "
                )
            itemName = check_itemName_format(itemName)[0]
            print(itemName)
            if len(itemName[0]) > 2:
                print(addNewInvItem(conn, item=itemName), "\n")
            else:
                print(addNewInvItem(conn, itemName), "\n")
        else:
            menuSelection = ""
        # Double check that the User really meant to exit the program.
        if menuSelection == "q":
            menuSelection = input("Quit and close database?\n" +
                                  "([Enter] to continue or [q]uit,): "
                                  )
            conn.close()
            exit
            # raise SystemExit()
        else:
            menuSelection = ""
    conn.close()


# ===================================================

if __name__ == "__main__":
    # [Test #1] Test the kitchen classes:  Ingredient(), Recipe(), Inventory()
    # from classes.ingredients import Ingredient
    # from classes.recipes import Recipe

    # 'aTuple' is a list of tuples, each tuple is an inventory record
    aTuple = [('bannana', '(each)', 41, 'none', None),
              ('butter', '(stick)', 32, 'dairy', 'Creamy milk goodness.'),
              ('buttercup', '(bunch)', 20, 'veg', None)]
    print("\ntablePrint(aTuple):\n", aTuple)
    tablePrint(aTuple)

    # 'dicts' is a list of dictionary records
    aDict = {'bannana': ['(each)', 41, 'none', None],
             'butter': ['(stick)', 32, 'dairy', 'Creamy milk goodness.'],
             'buttercup': ['(bunch)', 20, 'veg', None]}
    print("\ntablePrint(aDict):\n", aDict)
    tablePrint(aDict)

    # Example of a list of <str> as an inventory record
    aStr = ['apple', 'bushel', 30, 'fruit']
    print("\ntablePrint(aStr):\n", aStr)
    tablePrint(aStr)

    # 'aList' is a list of sublists, each sublist is an inventory record
    aList = [['bannana', '(each)', 41, 'none', None],
             ['butter', '(stick)', 32, 'dairy', 'Creamy milk goodness.'],
             ['buttercup', '(bunch)', 20, 'veg', None]]
    print("\ntablePrint(aList):\n", aList)
    tablePrint(aList)

    main()

    # --- Write Test Scripts below here ---
    # testArgs("gene", "c:\\users\\lifygen\\projects\\python\\")
    # testArgs("gene")
'''
    #  # Import old Inventory.txt database into the SQLite Inventory.db
    # Step1 - Retireve old Inventory.txt database info into txtDbInfo
    importDbName = 'Inventory.txt'
    dbName = 'Inventory.db'
    path = "C:\\Users\\Lifygen\\projects\\python\\data\\"
    conn = open_db(dbName, path)
    ptr = conn.cursor()

    # Import the old Inventory text file database
    fullPath_importDbName = path + importDbName

    #COMMENT OUT CODE
    # importInv() returns a <dict>
    txtDbInfo = importInv(conn, fullPath_importDbName)
    # Step 2 - Add each item to the SQLite Inventory.db
    #          UPDATE qty if iem already exists
    #          ADD newItem if it isn't already in the Inventory.
    newQty = 0
    for record in txtDbInfo:
        if itemInDb(conn, record):
            # If item is already in the db then update the SQLite item's qty
            sqlQuery = ("SELECT itemName, qty \
                        FROM Inventory \
                        WHERE itemName = '" + record + "'")
            sqlItemQty = getSqlData(conn, sqlQuery)
            newQty = float(sqlItemQty[0][1]) + float(txtDbInfo[record][1])
            # UPdate the SQLite db item with the new Qty
            ptr.execute("UPDATE Inventory \
                        SET qty = :qty \
                        WHERE itemName = :name;",
                        {'qty': newQty, 'name': record}
                        )
            conn.commit()
        else:
            # Item not in db so add it.
            itemRecord = [(record,
                          txtDbInfo[record][0],
                          txtDbInfo[record][1],
                          txtDbInfo[record][2])]
            addNewInvItem(conn, item=itemRecord)
    # Lastly, remove any duplicates in the SQLite database.
    # Or really this should be run once and should not have to be run again.
    itemDict = showInv(conn, toScreen=True, sendRet=True)
    tablePrint(itemDict)

    print("\nInventory after consolidation of duplicates:", itemDict)
    tablePrint(showInv(conn, toScreen=True, sendRet=True))

    sql_DuplItemsQuery = "SELECT itemName \
                            FROM Inventory \
                            WHERE rowid not in (select min(rowid) \
                                                from Inventory \
                                                group by itemName) \
                            GROUP BY itemName"
    DuplItemsList = getSqlData(conn, sql_DuplItemsQuery)
    print("Duplicates List: ", DuplItemsList)
    for name in DuplItemsList:
        # name is a Tuple
        consolidateInvItem(conn, name[0])

    itemDict = showInv(conn, toScreen=True, sendRet=True)
    tablePrint(itemDict)
    ptr.close()
    conn.close()
'''  # End of COMMENT OUT

""" Beg NOTES:
----------------------------
NOTES and Reference Examples:
----------------------------
#    # Create an SQLite database
    import sqlite3
    conn = sqlite3.connect('mytest.db')
    ptr = conn.cursor()
    sql = "create table students (name text,
                                  username text,
                                  id int
                                  )"
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

    # This query gets All of a specfic itemName (first first one and all its \
      duplicates)
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


    # Create a UNIQUE KEY on a Table
    CREATE [UNIQUE] INDEX index_name
            ON table_name (c1,c2,...)


    # pragma checks the schema of the table
      PRAGMA table_info(tbl_status);
      PRAGMA [database.]table_info( table_name );
      a = ptr.execute("PRAGMA table_info(Inventory);")
      a.fetchall()
      [(0, 'itemName', 'text', 0, None, 0),
       (1, 'unit', 'text', 0, None, 0),
       (2, 'qty', 'int', 0, None, 0),
       (3, 'FoodCategory', 'text', 0, None, 0),
       (4, 'Description', 'text', 0, None, 0)]

    # Add a column to an existing Table:
    ALTER TABLE <table>
    ADD COLUMN column_definition;

    http://www.sqlite.org/lang_altertable.html
    https://stackoverflow.com/questions/2614728/add-column-to-sqlite-db-if-not-exists-flex-air-sqlite/2614737

    "ALTER TABLE <table>
    ADD COLUMN  <new column info>"

    ALTER TABLE Inventory
    ADD COLUMN Description text"

    # Parameterized PRAGMA Trys DO NOT WORK!!!!!!!!:
    This Works (Build a query string prior to feeding to ptr.exeute())
    sqlPragma = ("PRAGMA table_info(" + tableName + ");")
    sqlPragma = ("PRAGMA table_info = Inventory;")
    NOTE:  "Pragma table_info(x)" is equivalent to "Pragma table_info=x"

    NOTE:
    ***A parameterised query cannot have a [table name] or [field name] as a
    parameter. The only way to do that is to dynamically code the table name
    into the query string BEFORE feeding the query into the ptr.execute().
    https://stackoverflow.com/questions/11312737/can-i-parameterize-the-table-name-in-a-prepared-statement
    ***
    Thus the following Fails:
    # Fail: ValueError: operation parameter must be str
    # sqlPragma = ("PRAGMA table_info(?);", [tableName])
    # sqlPragma = ("PRAGMA table_info(?);", (tableName))
    # sqlPragma = ("PRAGMA table_info(?);", [(str(tableName))])
    # sqlPragma = ("PRAGMA table_info(:aTable);", {'aTable':tableName})
    # sqlPragma = ("PRAGMA table_info(:tableName);", {'tableName':tableName})
    # sqlPragma = ("PRAGMA table_info(?);", tableName)
    # sqlPragma = ("PRAGMA table_info = ':x';", {'x':tableName})
    # sqlPragma = ("PRAGMA table_info = :x;", {'x':tableName})
    # Try These two together:
    # tableName = "'Inventory'"
    # sqlPragma = ("PRAGMA table_info=:x;", {'x':tableName})


    # Use an Alias, assign alias
    Select DISTINCT [itemName][Item Name <alias>] FROM Inventory
"""  # End Notes