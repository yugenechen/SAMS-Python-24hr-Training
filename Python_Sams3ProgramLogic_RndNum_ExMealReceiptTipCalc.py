# Given a number, write a snippet of code that will print
#  "You have money" if the number is positive, "You are out" if
#  it's zero, adn "You seem to be in debt" if it is less than zero.
#  your code should use "if", "elif", and "else" statements.

# Generate a random #
import random
a_number = random.random()
print "Test Generator #1:  ", a_number
if a_number > 0.4:
    sign = -1.0
elif a_number <= 0.3:
    sign = 1.0
else:
    sign = 0.0

a_number = random.random()
print "Test Generator #2:  ", a_number
a_number = a_number * sign *100
print
print "You have ", a_number, " in your wallet."
if a_number > 0:
    print "You have money!!! (:o))-{"
elif a_number == 0:
    print "You are out - loser (;(){-"
else:
    print "You seem to be in debt =(:(){-"
