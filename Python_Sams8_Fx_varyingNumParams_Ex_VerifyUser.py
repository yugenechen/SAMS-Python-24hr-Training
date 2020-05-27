#  SAMS Python Chapter 8 Quiz and Excercise
#  Using Functions to Create Reusable Code, pp 81 - 94
#  ------------
#  History:
#  ------------
#  04/28/2020 - added page number reference for this excercise module
#                        added Hisotry section.
#  04/17/2020 - created and completed
#  ------------
# Questions:

# 1) How are values passed into functions?
#   [Answer]:  using arguments in the funciton call.

# 2) When is a variable in scope?
#   [Answer]: a variable is in scope when it is held in memory.  Local variables
#             are in scope (accessible) when the local function is executing.
#             <<official answer>>:  A variable is in scope when it can be 
#                                   succesfully referenced.

# 3) What do *args and **kwargs do?
#   [Answer]:  *args and **kwargs both allow an optional and variable number of
#              arguments (a.k.a. parameters) to be passed into the function.
#              *args passes into a tuple fixed list (arg1, arg2, arg3,...) while
#              **kwargs passes into a key word dictionary {kwarg0, kwarg1, kwarg2}
#

#***********
# EXCERCISE:  p. 94 Get and verify user
#***********
  
#1) Make use of the "if __name__ == "__main__": main()" technique
#   See last line of this doc.  Adding the if __name__ allows this .py file
#   to run as a script so it runs if [Run]->"Run Module" is chosen from this menu

# ****************
#2) Write a program that gets a name from a user. If that name appears in a class
#   list, then the program should tell the user that the student is in that class.
#   If not, it should alert the user that there's no student by that name. There
#   should be a function that returns True if the student is present, and a False
#   if not.  See Chapter 8 ending for output example.
def main():
    name = ""
    print "Welcome to student enrollment checker."
    while (name.lower() <> 'q'):
        name = raw_input("Enter a student name in 'First_Name Last_Name' format\n:")
        if not(name.replace(" ", "").replace("-","").replace('"', "").replace("'","").isalpha()):
            print "Invalid input, try again in text format with quote marks around it." 
            continue
        elif (name.lower() == "q"):
            break
        else:
            nameVerified = verifyStudent(name)
            print "Name Verified:  " , nameVerified

        if nameVerified:
            print name + " is enrolled as a student.\n"
        else:
            print "No, " + name + " is NOT enrolled.\n"
            

def verifyStudent(student=""):
    classList = ['Mary Anne Chen', 'Yu-Gene Chen', 'Michel Morse', 'Paul Nowosielski', 'Cindy Jordan']
    student = student.replace("'","").replace('"',"")
    print (student in classList)
    if (student in classList):
        return True
    else:
        return False

    
def char_stat_generator():    

    Str = DiceRoll() + DiceRoll() + DiceRoll()
    Int = 3 * max(rnd(6), rnd(6), rnd (6))
    Wis = DiceRoll(6,3)
    Dex = max(DiceRoll(), DiceRoll(), DiceRoll()) + max(rnd(6), rnd(6), rnd (6)) + max(rnd(6), DiceRoll(), rnd (6))
    Con = max(DiceRoll(6,3), DiceRoll(6,3), DiceRoll(6,3), DiceRoll(6,3), DiceRoll(6,3), DiceRoll(6,3))
    Cha = (rnd(6) + rnd(6) + rnd (6))
    repl = []
    replStat = []
    for i in range(36):
        repl += [rnd(6)]
    repl.sort()
    repl.reverse()
    for i in range(0,36,3):
        replStat += [(repl[i] + repl[i+1] + repl[i+2])]

    print 'Str = ', Str
    print 'Int = ', Int
    print 'Wis = ', Wis
    print 'Dex = ', Dex
    print 'Con = ', Con
    print 'Cha = ', Cha

    i = 0
    for stat in replStat:
        print "Replacement Stat#" + str(i+1) + ": " +  str(replStat[i])
        i += 1
        if (i == 6):
            break
        
    
def rnd(xSidedDie=10, lowBound=1):
    #generates an integer number between lowBound and xSidedDie
	import random
	return int(random.random()*xSidedDie +lowBound)

def DiceRoll(dice=6, numberOfRolls=1):
    #generates an integer number between lowBound and xSidedDiemyRolls = []
    myRolls = []
    sumOfRolls = 0

    for i in range(numberOfRolls):
        myRolls += [rnd(dice)]
    for roll in myRolls :
        sumOfRolls += roll        

    return sumOfRolls

def Dice6d6Hi3():
    list6d6 =  [rnd(6), rnd(6), rnd (6),rnd(6), rnd(6), rnd (6)]
    list6d6.sort()
    list6d6.reverse()
    print list6d6[0] + list6d6[1] + list6d6[2]



if __name__ == "__main__":
    main()
