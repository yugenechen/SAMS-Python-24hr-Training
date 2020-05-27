#  SAMS Python Chapter 13 (pp138 - 147) Training snippets, Quiz and Excercise
#  "Batteries Included"  Python Modules - random package, datetime module, 
#   where to find more modules and packages
# Course Training -
#**********************
#  1] random package
# ######################
# Hierarchy ->  Libraries contain Packages
#    Packages contain Modules
#    Packages are akin to directories and Modules are akin to files
#
#  Common Packages to know:
#    random  - generate random numbers
#    os          - interact with operation system
#    json       - create adn read JavaScript Object Notation files.
#    sqlite3    - create, edit, reate, SQLite databases
#    datetime - get, manipulate, display, perform math operations on date and time
#    getpass - get password, get sensitive info from a user
#    this        - An Easter egg! check it out by typing "import this"
#    pprint     - print data in an easer-to-read format 
#
# Package References  -  http://docs.python.org/2/library/
#     -  http://docs.python.org/library/
#     -  The Python Standard Library by Exmaple by Doug Hellmann
#     -  http://wiki.python.org/moin/UsefulModules
#     -  search "Python Modules" with web search engine


#  random package()
#  random.random generates random number between 0 and 1.
#  randint(a,b) generates random integer numbers between and including a and b.

from random import randint
for i in range(10):
    randint(1,10)

#OR <import random> and use the random.<function> syntax
import random
random.random()
a=1; b=10
random.randint(a,b)

# choice(myLIst) will randomly pick an item out of the list <myList>

#  Already have a good understanding of random number generator from 1980's
#  coding - Apple, Atari game programming, Honeyell systems and Labview (both
#  used in simulating plant process and device transmitter signals).
#  It is interesting that Python provides both a <real> and <integer> random
#  number generator.  See the Chapter 3 (Python_Sams3_Ex.py)
#  Chapter 8 (Python_Sams8_Ex.py and Python_Sams8_Ex_main.py) random
#  number experiments.

#**********************
#  2] Time datetime package
# ######################
# import datetime
# pcTime =  datetime.now()
# lunchtime = datetime.time(12,30)
# from datetime import time; lunch = time(11, 30)
# lunch.hour; lunch.minute; lunch.second
# tdiff = lunchtime = lunch
# mytime = datetime.datetime(year = 2020, day=27, month=5)
# jt = datetime.datetime(year=2001, day = 14, month = 4)
# dayDiff = hm - jt

# Now add a week to today's date
# aWeekOffset = datetime.timedelta(days=7)
# aWeekFromNow = datetime.datetime.now() + aWeekOffset
# print datetime.datetime.now()
# print aWeekFromNow

#**********************
# Questions:

# 1) How do you import just one function from a module
#   [Answer]:  Use the following syntax:  "from <module_name> import <function_name>
#                    

# 2) What does a timedelta object contain?  
#   [Answer]:  The difference between two time objects in days or seconds.
#               
# 3)  How do you get more information about a module?
#   [Answer]:  Two ways:
#                    (1) import it and then try using the "help <module_name>" within Python environment
#                    (2) google (or search engine) Python <module name>

#***********
# EXCERCISE:
#***********
  
#1) Supposedly, the random function from the random module will never return zero or one.
#    Write a function to help prove this.  You should save how many times you've tested to see
#    if zero or one is returned, but you don't have to save any of the data produced by calling
#    random().

# [My Random # Checker ANSWER]
def CheckRndEndpoints(capCount=10000000):
    # Test that random.random() generates numbers between 0-1 without reaching 
    # the boundary endpoints.  Note:  0 and 1 boundaries should never be reached.
    # capCount limits the looping to prevent an infinite loop.
    import random
    rollCount = 0
    rnd = 0.1
    print "This function tests for random.random() reaching its 0-1 " +
          "boundaries.\nPress [Ctrl]+[C] to break."
    while ((rnd > 0) and (rnd < 1)):
        rollCount += 1
        rnd = random.random()
        if rollCount % 1000000 == 0:
            # FORMAT with comma separator for 1000s:   '{:,}'.format(value)
            print '{:,}'.format(rollCount) + " generated random numbers and counting..."

        if rollCount >= capCount:
           # FORMAT with comma separator for 1000s:   '{:,}'.format(value)
            print('{:,}'.format(rollCount) + " random numbers generated!!!\n" +
                  "Enough is enough; stopping calculations.")
            break
        
    msg = "\nBoundary reached or breached in {rolls} random number generations".format(rolls=str(rollCount))
    if (rnd < 0 or rnd > 1):
        msg += "\nThe upper/lower boundary was breached with a roll of {}".format(str(rnd))
    else:
        msg += "\nThe upper/lower boundary was reached with a roll of {}".format(str(rnd))
        

#2) Now that you've been introduced to the random module, it's time for the time honored
#    tradtion of writing a number-guessing game!  Have a user guess a number between one
#    and ten.  If the computer's number is too hight or too low, the program should let her
#    know and allow her to guess again.  Once the user guesses correctly, the program
#    should congratulate her and then stop.  Here is some sample output:
#    >>>Welcome to the number guessing game!
#    >>>I have my number...
#    >>>What is your guess [1-10]? 5
#    >>>That's too high. Try again!
#    >>>What is your guess [1-10]? 1
#    >>>That's too low. Try again!
#    >>>What is your guess [1-10]? 3
#    >>>You got it!  Thanks for playing!
#
#   Extra Credit:  Think about and incorporate ways to make the game more interesting.
#                        1.  Optionally limit the number of turns
#                        2.  Increase/decrease the range of numbers the player can guess from.

def GuessingGame(guessLimit=5, lowBound=1, upperBound=10):
    # generates an integer number between lowBound and xSidedDie
    import random
    target = randint(lowBound, upperBound)
    guesses=0
    guess = ""
    response = "N"

    # Start of new game - Intro to player.
    print "Welcome to the guessing game.  Great for numbers, " +
          "terrible for communicating with significant others.\n"

    while response.upper() in ("N"):
        player = raw_input("Enter your name:")
        if not player:
            player = "Player"
        response = raw_input("Is {player} your correct name? " + 
                             "<enter [Y/N]:>".format(player = player))
        if not response:
            response = "Y"

    # Query for new Game Setup
    response = ""
    while not str(response).upper() in ("Y", "N"):
        response = raw_input("\nThe games is currently set for you to take " +
                              str(guessLimit) + 
                             " guesses\n" +
                             "to guess a number between " +
                             str(lowBound) + " and " + str(upperBound) + "\n" +
                             "\nWould you like to change these parameters?" + 
                             "<Enter [Y/N]>:"
                             )
        try:
                     response = int(response)
                     next
        except:
                     continue
        print "Invalid entry, please try again."
                             
    # Player chose for a New Game Setup
    while str(response).upper() in ("Y"):
        # Get new guess limit
        old_setting = guessLimit
        while True:
            response = raw_input("The games is currently set to a " + 
                                 str(guessLimit) + 
                                 " guess limit. \n" +
                                 "Enter the new number of guesses " +
                                 "([<any integer #> ] or [Enter] to continue):"
                                 )
            try:
                     if not response:
                         guessLimit = old_setting
                     else:
                         guessLimit = int(response)
                     break
            except:
                     print "Invalid entry, please try again."
                     continue

        #Get new Lower Bound for the target number
        old_setting = lowBound
        while True:
            response = raw_input("\nThe games is currently set for you to " +
                            "guess a number between " +
                            str(lowBound) + " and " + str(upperBound) +
                            ".\n" +
                            "Enter the new LOWER Boundary " +
                            "([<any integer #> ] or [Enter] to continue):")
            try:
                    if not response:
                         lowBound = old_setting
                    else:
                         lowBound = int(response)
                    break
            except:
                    print "Invalid entry, please try again."
                    continue

        #Get new Upper Bound for the target number
        old_setting = upperBound
        while True:
            response = raw_input("\nThe games is currently set for you to " +
                            "guess a number between " +
                            str(lowBound) + " and " + str(upperBound) + 
                            ".\n"+
                            "Enter the new UPPER Boundary " +
                            "([<any integer #> ] or [Enter] to continue):")
            try:
                    if not response:
                         upperBound = old_setting
                    else:
                         upperBound = int(response)
                    break
            except:
                    print "Invalid entry, please try again."
                    continue

        response = "N"  #CLOSE WHILE:  [Player chose for a New Game Setup]

    # Commence with the Guessing Game:  Get new guesses and check for a match
    while ((guesses < guessLimit) and (guess !=target)):
        guess = raw_input("\n{player}, make a guess between {lower} and {upper}:".format(
                         player = player,
                         lower = lowBound,
                         upper = upperBound
                         ))
        # IOptional IMPROVEMENT:  use <try><exception> to handle non-integer entry.
        guess = int(guess)
        if guess > target:
            print "Hey {player}, your guess was too HIGH!  Have another go at it.".format(
                     player = player
                     )
        elif guess < target:
            print "{player}, your guess was too LOW!  Have another go at it.".format(
                     player = player
                     )
        
        guesses += 1
        print ("You have {guesses} out of {guessLim} left".format(
                  guesses = guessLimit-guesses,
                  guessLim = guessLimit
                 ))

    #End the Guessing Game:  Determine Award vs. Failure
    if (guess == target):
      print ('Wow!!!, You must be some kind of psychic!!!\nI dub thee "{player} the Psychic"'.format(
                 player = player
                 ))
    else:
      print ("Sorry {player}, your ran out of guesses before getting the TARGET number of {target}".format(
                 player = player,
                 target = target
                 ))
            
	
# *** MAIN Program
def main():
    #Do Nothing
    DoNothing = True
  
    

if __name__ == "__main__":
                       main()
                       #This can be used to override main() defaults when
                       # executing as a script using [F5] or
                       # using the menu [Run]->[Run Module]
                       #    changing to "main(1)" would run scenario 1
                       #    changing to "main(2)" would run scenario 2
                       #User entered values override this input and
                       #command line main() would run the default (without using this override)
                       

                       
        

        
    




























