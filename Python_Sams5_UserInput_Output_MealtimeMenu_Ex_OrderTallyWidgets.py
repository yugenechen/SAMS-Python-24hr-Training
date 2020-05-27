#1) What is the difference between input() and input_raw?
# [answer]:  input() takes in "raw data" from the user.  It attempts to convert
#                    the user info into all the same data type so string and
#                    numerics cannot be mixed.
#            input_raw() converts all data into a string

#2) What do you collect user input securely (hide their response)?
# [answer]:  Use getpass() function. <<must "import getpass" from the get pass library>>

#3 How do you remove whitespace form the end of a string?
# [answer]:  use rstrip() function => s.rstrip() where s = "the string"

#4)a. How do you insert one string within another?
#   [answer]:  use any of the following: %s, S.join(), replace(), format()
#  b. How do you indcate where the new string is inserted?
#     for %s, place the %s at the location within the original string
#     for s.Join() use "".join() where the "" text is placed between each item
#     for replace(), use replace("find text", "replace with text"
#     for format(), use {} in the target string where user input will be entered into

#5)  Ho do you convert a string to a float?  ... to an integer?
# [answer]:  convert string to float using float(s)
#            convert string to integer using int(s)

#-----------
#Excercises:
#-----------
# 1.  The cook's script could be more robust.  Rewrite it so that it
#     does not matter what whether the waiter entered extra whitespace or
#     happened to capitalize some or all the letters.

# 2.  Ask a user for the name of an item, the number being purchased
#     and the cost of the item.  Then print out the total and thank the user.

#Excercise #1 - python specials.py
#Original code:  The Cook's Script

breakfast_special = "Texas Omelet"
breakfast_notes = "Contains brisket, horseradish cheddar"
lunch_special = "Greek patty melt"
lunch_notes = "Like the regular one, but with tzatziki sauce"
dinner_special = "Buffalo steak"
dinner_notes = "Top loin with hot sauce and blue cheese. NOT BUFFALO MEAT."

meal_time = raw_input('Which mealtime do you want? [breakfast, lunch, dinner]')
print "specials for {}:".format(meal_time)
if meal_time == 'breakfast':
    print breakfast_special
    print breakfast_notes
elif meal_time == "lunch":
    print lunch_special
    print lunch_notes
elif meal_time == "dinner":
    print dinner_special
    print dinner_notes
else:
    print "Sorry, {} isn't valid.".format(meal_time)

#Modified Code #1.1; modified as follows:
#    1)  Made it a function so it can be called instead of typing or
#        having to scroll back all the time.
#    2)  Simplified it so that that whitespace and upper/lower case
#        does not matter and added allowance of both -
#              enumerated numeric and
#              first letter entries
#       for the ultimate in simplification.
#    3) Added header label for the specials being printed out for clarity
def python_specials1_1():
    breakfast_special = "Texas Omelet"
    breakfast_notes = "Contains brisket, horseradish cheddar"
    lunch_special = "Greek patty melt"
    lunch_notes = "Like the regular one, but with tzatziki sauce"
    dinner_special = "Buffalo steak"
    dinner_notes = "Top loin with hot sauce and blue cheese. NOT BUFFALO MEAT."

    mealtime = raw_input('Which mealtime do you want? [(1)|b|reakfast, (2)|l|unch, (3)|d|inner]')
    print 'Specials menu for your "{}" selection:'.format(mealtime)
    if ("1breakfastbrkfst".find(mealtime.lower()) >-1):
        print "----------------------\n| Breakfast Specials |\n----------------------"
        print breakfast_special
        print "\t-" + breakfast_notes
    elif ("2lunch".find(mealtime.lower()) >-1):
        print "------------------\n| Lunch Specials |\n------------------"
        print lunch_special
        print "\t-" + lunch_notes
    elif ("3dinner".find(mealtime.lower()) >-1):
        print "-------------------\n| Dinner Specials |\n-------------------"
        print dinner_special
        print "\t-" + dinner_notes
    else:
        print "Sorry, {} isn't valid.".format(mealtime)
    return;    

#Modified Code #1.2; modified to use LIST object for more precise and accurate result in checking input:
#    1)  Modified v#1.1, a.k.a. "pthon_specials1_1"
def python_specials1_2():
    breakfast_special = "Texas Omelet"
    breakfast_notes = "Contains brisket, horseradish cheddar"
    lunch_special = "Greek patty melt"
    lunch_notes = "Like the regular one, but with tzatziki sauce"
    dinner_special = "Buffalo steak"
    dinner_notes = "Top loin with hot sauce and blue cheese. NOT BUFFALO MEAT."

    mealtime = raw_input('Which mealtime do you want? [(1)|b|reakfast, (2)|l|unch, (3)|d|inner]')
    print 'Specials menu for your "{}" selection:'.format(mealtime)
    if ( mealtime.lower() in ["1", "b", "breakfast", "brkfst", "br", "break"]):
        print "----------------------\n| Breakfast Specials |\n----------------------"
        print breakfast_special
        print "\t-" + breakfast_notes
    elif (mealtime.lower() in ["2", "L".lower(), "lunch", "lu", "LT".lower()]):
        print "------------------\n| Lunch Specials |\n------------------"
        print lunch_special
        print "\t-" + lunch_notes
    elif (mealtime.lower() in ["3", 'd', 'dinner', 'di', 'din', 'supper', 'sup']):
        print "-------------------\n| Dinner Specials |\n-------------------"
        print dinner_special
        print "\t-" + dinner_notes
    else:
        print "Sorry, {} isn't valid.".format(mealtime)
    return;    


#Excercise #2 - pythex5_2()
#     Ask a user for the name of an item, the number being purchased
#     and the cost of the item.  Then print out the total and thank the user.
def pythex5_2():
    item_name = raw_input("What item would you like to purchase? [Item Name]:")
    quantity = raw_input("How many " + item_name + "(s) would you like? [Quantity #]:")
    price = raw_input ("What is the price of each " + item_name + "? [Unit Price #.##]:")

    # Handle the case where the user inputs a '$' as part of the price, ex. $0.01
    price = float(str(price).strip("$"))
    total = int(quantity) * float(price)
    
    # If keys are used in the <transaction_msg> then those keys must be assigned in the s.format
    transaction_msg = "Thank you for your purchase of {quantity} {item_name}(s). \nYour total is ${total}"
    print "\n[Style 1a]:  s.format() with {keys}\n" + transaction_msg.format(quantity= quantity, item_name = item_name, total = str(format(total,'.2f')))

    # If keys are not used or if numeric indexes are used in the <transaction_msg> then
    # those keys are assigned in the s.format.  The variables fed are used in order of each 
    # field placeholder '{}'.  Cannot mix auto-numbering and manual-numbering
    # (nor mix with keying fields).  Must use the same field style {},{0}, {key} throughout.
    transaction_msg = "Thank you for your purchase of {} {}(s).\nYour total = ${}"
    print "\n[Style 1b]):  s.format() with {}; auto-field-numbering\n" + transaction_msg.format(quantity, item_name, str(format(total,'.2f')))

    transaction_msg = "Thank you for your purchase of {0} {1}(s).\nYour total = ${2}"
    print "\n[Style 1c]):  s.format() with manual-field-numbering{0..n}\n" + transaction_msg.format(quantity, item_name, str(format(total,'.2f')))

    # Example using oldstyle '%s' placeholder,
    # whereith the '%' list is defined at the end of the assignment or print statement
    print "\n[Style 2]):  uses %s holders\n" + "Thank you for purchasing %s %s(s). \nYour total is $%s" %(quantity, item_name, str(format(total,'.2f')))

    # Example using inilne string addition '+' operator
    print "\n[Style 3]):  uses '+' operator to joing strings + (string variables)\n" + "Thank you for your business.  Your purchase of " + quantity + " " + item_name + "(s) \ntotals to $", format(total,'.2f')

    # Example using s.join()
    print "\n[Style 4]):  s.join()\n" + " ".join(["Thank you for your shopping with us.  Your purchase of ", quantity , item_name, "(s) \ntotals $", str(format(total,'.2f'))])
    
    # Example using s.replace()
    transaction_msg = "Thank you for your purchase of @qty @item(s).\nYour total = $@total"                                     
    print "\n[Style 5]):  uses multiple chained .replace() methods; 's.replace().replace().replace()'\n" + transaction_msg.replace("@qty", quantity).replace("@item",item_name).replace("@total",str(format(total,'.2f')))
#To run use:  pythex5_2()
