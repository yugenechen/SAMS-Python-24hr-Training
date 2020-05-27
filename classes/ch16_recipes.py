'''Class from "Python SAMS, Ch14, p155)
# Recipe Class
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
class Recipe(object):
    '''
    The Recipe class accepts ingredients and directions on how to use the 
    ingredients to successfully execute the recipe to create a finished item.
    '''
    def __init__(self, name, ingredients=[], directions=[], note=""):
          self.name = name
          self.ingredients = ingredients
          self.directions = directions
          self.note = note

    def __str__(self):
          return self.name

    def print_recipe(self):
          print int(len(self.name))* "*"
          print self.name
          print int(len(self.name))* "*"

          #Print Recipe Ingredients
          n = 1
          print ("\n  Ingredients:" +
                 "\n  -----------")
          for ingredient in self.ingredients:
              print "  "+ str(n) + ")", ingredient
              n +=1

          #Print Recipe Directions
          n = 1
          print ("\n  Directions:" +
                 "\n  ----------")
          for direction in self.directions:
              print "  " + str(n)+ " - ", direction
              n += 1

          #Print any Recipe Notes
          if self.note:
             print ("\nSpecial note:" +
                    "\n------------")
             print self.note

				 
