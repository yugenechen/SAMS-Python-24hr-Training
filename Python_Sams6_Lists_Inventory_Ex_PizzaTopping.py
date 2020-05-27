#Python_Sams6_Ex.py
# 1) How would you count how many times an item is in a list?
# [answer]:  use the <list>.count("item") method to count how many times an item appears in a list.

# 2) How do you add a new item to a list?
# [answer]:  Use the the following techniqutes:
#    1. <List1>.append(<"item">) method,
#    2. <List1>.extend(<List2>) method,
#    3. insert(<index>, <item>) method
#    4. <List1> += <List2>; #add two lists together and store result in first list


# 3) What is the difference between reverse() and sort()?
# [answer]:  reverse() puts a list in reverse order (from existing order).
#            sort() puts a list in ascending order (by number adn then by alphs)
# Note: Put a list in descending order by running a <list>.sort() then, <list>.reverse()

# 4) How would you get a list of names to be sorted in reverse alphabetical order?
# [answer]:  set the "Note" in respose to #3 above.

#Excercise 6.1
# Write a program that allows the user to input two favorite toppings.
# If a topping is in a list of in-stock toppings then the topping is added to a
# new list.  Otherwise, a message is printed apologizing for being out of stock.
# Given:  Toppings in stock = pepperoni, peppers, cheese, sausage
def toppings():
    toppingOrder = []
    itemSuffix = {'1':'st', '2':'nd', '3':'rd'}
    toppingInv = ['pepperoni', 'cheese', 'sausage', 'peppers']
    number_of_toppings = raw_input("How many toppings would you like? \n[Enter #]:")
    if (number_of_toppings == "") :
        number_of_toppings = 2
    else:
        number_of_toppings = int(number_of_toppings)

    while (len(toppingOrder) < number_of_toppings): 
        print ("Please enter your " + "".join(str(len(toppingOrder)+1)+itemSuffix.get(str(len(toppingOrder)+1),'th')) + " topping (or enter [q] to exit. Or enter [c] to cancel)")
        topping = raw_input(": ")
        topping = str(topping)
        if (topping == "q"):
            while (len(toppingOrder) < number_of_toppings):
                toppingOrder += ["none"]
                print toppingOrder
        elif (topping == "c"):
            toppingOrder = []
            print "\n***Cancelled***\nYour order has been cancelled.\n"
        elif (topping in toppingInv):
            toppingOrder.append(topping)
        elif (toppingOrder == []):
              print "Try again."
        else:
            print "We our out of " + topping + " toppings."
            print "Try a topping in stock:  \n" , toppingInv
                
    print str(len(toppingOrder) - toppingOrder.count("none")) + " toppings were chosen."
    if ((len(toppingOrder) - toppingOrder.count("none"))>0):
        outMsg = "You chose " + str(len(toppingOrder) - toppingOrder.count("none")) + " topppings:  "
        for item in range(len(toppingOrder) - toppingOrder.count("none")) :
            print "\tItem #" , item+1, toppingOrder[(item)]
            
        
