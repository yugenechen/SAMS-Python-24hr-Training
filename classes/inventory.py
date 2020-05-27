'''Class from "Python SAMS, Ch14, p155)
# Inventory Class
#Inventory class should include the following:
#       1. A list of ingredients
#       2. How many of each ingredient is on-hand
#       3. A way to search the ingredients
#       4. A way to add items to the inventory
#       5. A way to remove items from the inventory
#
#   Hint:  Think what data type would work best for the ingredients;
#          it is not a list!
#
#
'''
class Inventory(object):
    ''' #A class that is basically an extension of the Dictionary class object.
    #Inventory.items is a dictionary object.
    #Inventory.<methods> are added to auto increment item
    #values as items are added into inventory (and decrement when removed).
    
    Initialization INPUT:
        items[] - can be any of the following objects upon initialization:
                  string object - a text name of an inventory item. Example
                                  'itemName'
                  tuple  object - a tuple of string names formatted as follows:
                                  ('item1', 'name2', 'third',...'nthItemName')
                  list object   - a list of string names, of following format:
                                  ['item1', 'name2', 'third',...]
                  dict object   - a dictionary paring of {'name':qty} items.
    '''
    def __init__(self, items=[]):
        self.items={}
        if not items:
           print('You have created an empty inventory.\n' +
                 'Input an ingredient or ingredient list. using the <inv_obj>.add(items);/n' +
                 'where <items> can be a tuple, list, dictionary{''item'':quantity}, or string.\n'
                 )
        else:
           self.add(items)     #populates self.items

    def add(self, items,qty=1):
        '''.add method receives an item=<string>, optionally a qty=<integer> 
                results in incrementing the named item by the qty amount.
                The code detects the item <data type>.  A list type
                (standard list, tuple, or dictionary) results in each item
                in the list being added to the Inventory and incremeted by
                qty.  (if the item already exists in inventory then the 
                inventory quantity is updated.  If the code detects a 
                a <dict> object then it pulls the item name as the key and
                the qty as value.
           Note:  the DocString has to start at the same indent level as normal code.
                  Otherwise it is ignored.
        '''

        if items:
           if (type(items) is str):
              #If items is a string then put it in a list so it can be handled
              #by handled by the same code used for list, tuple, dict. 
               items=[items]
           if ((type(items) is tuple) or 
               (type(items) is list) or
               (type(items) is dict)
              ):                    
              for eachItem in items:
                 if (type(items) is dict):
                    qty = items[eachItem]
                 if self.items.has_key(eachItem):
                    self.items[eachItem] += qty
                 else:
                    self.items[eachItem] = qty                

    def remove(self, items, qty=1):
        ''' .remove method receives an item=<string>, optionally a qty=<integer>.
                        results in decrementing the named item by the qty amount.
                        Code detects item type as in .add(), see the .add() desc.
        '''   
        if items:
          #Create a single item list if the user input is a string object  
           if (type(items) is str):
              #If items is a string then put it in a list so it can be handled
              #by handled by the same code used for list, tuple, dict. 

               items=[items]
           if ((type(items) is tuple) or 
               (type(items) is list) or
               (type(items) is dict)
              ):                    
              for eachItem in items:
                 if (type(items) is dict):
                    qty = items[eachItem]
                 if self.items.has_key(eachItem):
                    if self.items[eachItem] > 0:
                     self.items[eachItem] -= qty
                 else:
                    print "We are out of " + eachItem + "(s)!!!"

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
        ''' prints_method() - prints out the contents of the inventory as text in
                     "item" - qty format.
        '''
        #'Shows Inventory items and quantities
        for item in self.items:
              print item, "-", self.items[item]

    def print_me(self):
        ''' prints_method() - prints out the contents of the inventory as text in
                     "item" - qty format.
        '''
        #'Shows Inventory items and quantities
        #ex. using iterable function:  max([len(song.name) for song in self.songList])
        invBackup = []
        maxLen = max([len(item) for item in self.items])
        for item in self.items:
              print item + " "*(maxLen-len(item)+1) + "-", self.items[item]
              invBackup.append([item + "\t" + str(self.items[item]) + "\n"])
        return invBackup
        

if __name__ == "__main__":
    '''This tests out the Inventory class
    '''
    
    aTuple=('apple', 'orange','bannana')
    print aTuple
    tI=Inventory(aTuple)
    tI.print_inventory()
    print '\n'

    aDict={'apple':1, 'orange':3,'bannana':5}
    print aDict
    dI=Inventory(aDict)
    dI.print_inventory()
    print '\n'

    aList=['Mary Anne', 'Cindy', 'Stan']
    print aList
    lI=Inventory(aList)
    lI.print_inventory()
    print '\n'

    aStr = "Gene"
    print aStr
    sI=Inventory("Gene")    
    sI.print_inventory()
    print '\n'

    print "Inventory.remove():  dI.remove('bannana')"
    dI.remove('bannana')
    dI.print_inventory()
    print '\n'

    print "Inventory.add():  dI.add('apple')"
    dI.add('apple')
    dI.print_inventory()
    print '\n'

    print "*** Hello World END ***"
    