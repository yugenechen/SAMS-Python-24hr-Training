'''Class from "Python SAMS, Ch14, p155)
# Ingredient Class
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


class Ingredient(object):
    '''   This class is for Chapter 13-15 teaching about classes, subclasses,\
    and properly documenting code.  The "Ingedient" class object is used to \
    add to Inventory and Recipe objects.

    INPUTS:
        :name (str):        - name of the item as it will be stored in the \
                              database.
        :description :(str) - description of the 'name'd item.
    '''
    def __init__(self, name, description=""):

        while not name:
            name = input("Input the ingredient name: ")

        self.name = name
        self.description = description

    def __str__(self):
        return self.name


# *** MAIN Program
def main():
    '''This tests out the Ingredient class
    '''
    bannana = Ingredient('Bannanas')
    bannana.description = "A crescent shaped sweet yellow skinned fruit."
    print(bannana)
    print("bannana name = " + bannana.name)
    print("bannanna descr = " + bannana.description)


if __name__ == "__main__":
    pass
