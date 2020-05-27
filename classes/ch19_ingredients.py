'''Class from "Python SAMS, Ch14, p155)
# Ingredient Class
#Inventory class should include the following:
#       1. A list of ingredients
#       2. How many of each ingredient is on-hand
#       3. A way to search the ingredients
#       4. A way to add items to the inventory
#       5. A way to remove items from the inventory
#
#   Modified to meet Ch 18 & 19 ingredients put into the Inventory program
#   that uses an SQLite database.
#
#
#
'''


class Ingredient(object):
    '''This class is for Chapter 13-15 teaching about classes, subclasses,and \
    properly documenting code.  The "Ingedient" is used to add to Inventory \
    and Recipe objects.

    INPUTS:
        :name (str):        - name of the item as it will be stored in the \
                              database.
        :unit (str):        - unit of measure the item quantity (in the world \
                              of controls, these are engineering units (EU).
        :qty (float):       - quantity of the item in inventory, or on hand \
                              being put in or taken out of inventory.
        :FoodCategory (str): - Food category for classification and searches.
        :description (str): - description of the 'name'd item.
    '''
    # A basic "Ingredient" class used for indredients for recipes, inventory \
    # tracking, etc.

    def __init__(self, name="",
                       unit="",
                       qty="",
                       FoodCategory="",
                       Description=""):

        while not name:
            name = raw_input("Input the ingredient name: ")

        self.name = name
        self.description = description

    def __str__(self):
        return self.name


if __name__ == "__main__":
    '''This tests out the Ingredient class
    '''
    
    bannana=Ingredient('Bannanas')
    bannana.description = "A crescent shaped sweet yellow skinned fruit."
    print(bannana)
    print("bannana name = " + bannana.name)
    print("bannanna descr = " + bannana.description)