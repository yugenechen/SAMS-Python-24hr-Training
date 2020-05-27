# -*- coding: utf-8 -*-
"""
Python_Sams18, p 203, Excercise:  Recreate cook's Inventory() using SQLite
Implemented this test script and function: 
        str_to_float_or_int(value_str, ShowExtended=False)
        isFloat(numAsStr)
to properly implement data checking in InventorySQL.py.

Built-in string functions do not cover 'isfloat()'
    print(qty.isalnum(), "is alnum")      - tests for alpha numeric (not float)
        A character c is alphanumeric if one the following returns True:
        c.isalpha(), c.isdecimal(), c.isdigit(), or c.isnumeric().
    print(qty.isalpha(), "is alpha")      - tests for all alphabetic
    print(qty.isdecimal(), "is decimal")  - tests for numbers 0-9 only
    print(qty.isdigit(), "is digit")      - tests for numbers 0-9 (incl languages)
    print(qty.isidentifier(), "is identifier")      - does not include float chk
    print(qty.isnumeric(), "is numeric")  - tests for numbers 0-9 (incl fractions)



Created on Wed May 13 16:28:53 2020

@author: Lifygen
"""

testValues = ["0.80", "1.00", "5", ".1", "4."]
print("\n---------------------------------------------------\n" +
"|  Testcase:  ", testValues, " |\n" +
"---------------------------------------------------")
for number in testValues:
    # Default condition is that the number is a <float>
    isfloat = True
    integer = ''
    mantissa = ''
    value = float(number)
    numberParsed = number.split(".")
    print("'" + number + "'" + " splits into: ", numberParsed)
    if len(numberParsed) > 1:
        integer = numberParsed[0]
        mantissa = numberParsed[1]
        if integer.isdecimal() and mantissa.isdecimal():
            if int(mantissa) == 0:
                # value is an integer
                isfloat = False
                value = int(integer)
        elif integer.isdecimal():
            # <str>.split() returns two item list for "#." and ".#"
            # <str>.isdecimal() returns null when <str> value is empty or null
            # value is an integer
            isfloat = False
            value = int(integer)
    else:
        # value is an integer because there is no Mantissa
        isfloat = False
        value = int(number)

    print("integer: {Int} | Mantissa: {M}".format(Int=integer, M=mantissa))
    print("testValue: " + number + " | value: ", value)
    if isfloat:
        print("'" + number + "' is a <float> (;o): '" + str(value) + "'\n")
    else:
        print("'" + number + "' is an <int> {:o)~: '" + str(value) + "'\n")


def str_to_float_or_int(value_str, ShowExtended=False):
    '''
Convert a number stored as a string to a <float> or an <int>.\n
Although all integers can be floats, an <int> is returned wherever possible as
when: \n
\t input = a whole number. \n
\t input = a characteristic with a 0 mantissa ('1.0') \n
\t input = a characteristic without a mantissa ('1.')
    '''
    # Default condition is that the number is a <float>
    isfloat = True
    value = float(value_str)
    # Parse the string value (candidate number) into two parts;
    # integer = before the decimal and mantissa is after the decimal.
    # split returns a list [integer,mantissa]
    # Tehcnically, use of the term 'integer' here is the 'characteristic'
    # but I used 'integer' beause it is shorter length in coding
    numberParsed = value_str.split(".")

    if len(numberParsed) > 1:
        integer = numberParsed[0]
        mantissa = numberParsed[1]

        if integer.isdecimal() and mantissa.isdecimal():
            if int(mantissa) == 0:
                # value is an integer; mantissa is 0
                isfloat = False
                value = int(integer)
        elif integer.isdecimal():
            # value is an integer; only integer is a value and mantissa is null
            isfloat = False
            value = int(integer)
    else:
        # value is an integer because .split() returned a single value list
        isfloat = False
        value = int(value_str)

    if ShowExtended:
        print("testValue: " + value_str + " | splits into: ", numberParsed,
              "\n value: ", value)
        if isfloat:
            print("It's a <float> (;o)\n")
        else:
            print("It's an <int> {:o)~\n")

    return value


def isfloat(numAsStr):
    '''returns True if can be converted to a `<float>` otherwise returns False.
    Only checks for one "." and no "," separtors in the string.
    '''
    return numAsStr.replace(".","",1).isalnum()


#Run Script from the Console to test str_to_float_or_int()
testValues = ["0.80", "1.00", "5", ".1", "4."]
print("\n---------------------------------------------------\n" +
        "|  Testcase:  ", testValues, " |\n" +
        "---------------------------------------------------")
for number in testValues:
    str_to_float_or_int(number, ShowExtended=True)


for number in testValues:
    print(str_to_float_or_int(number))


for number in testValues:
    print("'" + number + "'\tis a   \t`<float>`  " + str(isfloat(number)), 
          float(number))












