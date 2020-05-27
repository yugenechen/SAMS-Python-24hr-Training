#  SAMS Python Chapter 8 Quiz and Excercise
#   Using Functions to create Reusable code, pp 81-94)

#  ------------
#History:
#  ------------
#  04/28/2020   added page number reference,
#                        edited to correct typo "inegers" -> "integers on EXCERCISE.d)
#                        added "History"
#  04/17/2020:  created and completed
#
#  ------------

#**********
#EXCERCISE:  Extra Credit program
#**********
# Write a function that calls a second custom function that utilizes -
#   a) iterations (looping)
#   b) lists
#   c) list methods list.method
#   d) integers
#   e) Reals (float)
#   f) strings
#[Answer]:  Write a dice roll generator that receives an argument that determines
#           the number of sides of the die.  A second function uses the dice function
#           to roll the dice and report out on statistics:
#           a) User inputs sided die type (i.e. indicates 6 sided, 2 sided, 10 sided)
#           b) User inputs number of rolls (if none given then 100 rolls)
#           c) Reports how many times a number is rolled
#           d) Reports % of rolls that a number shows up to two decimal place precision
#           e) Shows total rolls
#           f) Checks and shows total %
#           g) Shows sum of all rolls

def rnd(x):
	import random
	return int(random.random()*x +1)

def DieStats(dice=6, rolls=100):
    myRolls = []
    total_rolls = 0
    total_percent = 0
    sumOfRolls = 0

    for i in range(rolls):
        myRolls += [rnd(dice)]
        sumOfRolls += myRolls[i]

    print "-----------------"
    print "Dice Roll Summary"
    print "-----------------"
    for i in range(1,dice+1):
        die_side_count = myRolls.count(i)
        die_side_percent = float(die_side_count)/rolls * 100
    
        print str(i)+"'s:  " + str(die_side_count) + "    " + '%.2f' % die_side_percent + "%"
        total_rolls += die_side_count
        total_percent += die_side_percent
    
    print "----------------"
    print str(total_rolls) +" rolls| " + '%.2f' % (total_percent) +"%  | Sum of rolls = " + str(sumOfRolls)
    return sumOfRolls

#count how many rolls are required to get a 100 roll total that is = 400
# ~9000 sets generated totals ranging from 284-408 with 21 numbers outside the 300s
x=301; count=0; rollSums = []
while (x<=450) and (x>270):
    x=DieStats()
    count = count +1
    rollSums+=[x]

print "It took " + str(count) + " rolls for [total<=300] or [total>=400] with " + str(x)
	
