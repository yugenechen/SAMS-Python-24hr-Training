# -*- coding: utf-8 -*-
"""
Helper Classes and Function tools to augment Python built-in methods

1.  testArgs(name, *path) - tests passing *args
                            (unNamed optional arguments to a function)
2.  str_to_float_or_int(value_str, showExtended=False)
                                   showExtended is for testing.
3.  isfloat(numAsStr) - returns True if can be converted to a `<float>`
                        returns False if otherwise,

Created on Thu May 14 07:27:17 2020

@author: Lifygen
"""


def testArgs(name, *path):
    '''
    Tests the *args technique in function declarations allowing optional,
    unnamed values to be passed into a function.  The values are delivered
    as a tuple.
    '''
    #print("name = " + str(name))
    #print("path = " + path)
    print("name: ", name)
    print("path: ", path)
    print("*path Tuple length: ", len(path),
          "\nTuple = ", value=path)
    for each in path:
        print("\t" + str(len(each)) + " of " + str(len(path)) + "value:", each)


"""
Python_Sams18, p 203, Excercise:  Recreate cook's Inventory() using SQLite
Implemented this test script and function:
        str_to_float_or_int(value_str, showExtended=False)
        isFloat(numAsStr)
to properly implement data checking in InventorySQL.py.

Built-in string functions do not cover 'isfloat()':
print(qty.isalnum(), "is alnum")      - tests for alpha numeric (not float)
    A character c is alphanumeric if one the following returns True:
    c.isalpha(), c.isdecimal(), c.isdigit(), or c.isnumeric().
print(qty.isalpha(), "is alpha")      - tests for all alphabetic
print(qty.isdecimal(), "is decimal")  - tests for numbers 0-9 only
print(qty.isdigit(), "is digit") - tests for numbers 0-9
                                   (incl languages, superscript, subscript)
print(qty.isidentifier(), "is identifier")      - does not include float chk
print(qty.isnumeric(), "is numeric")  - tests for numbers 0-9 (incl fractions)


Created on Wed May 13 16:28:53 2020

@author: Lifygen
"""


def str_to_float_or_int(value_str, allFloat=False, showExtended=False):
    '''Convert a number stored as a string to a <float> or an <int>.  \
Although all integers can be floats, an <int> is returned wherever is the
tighter visual type such as when INPUT:
 - input = a whole number. \n
 - input = a characteristic with a 0 mantissa ('1.0').
 - input = a characteristic without a mantissa ('1.').

INPUTs:
    :value_str (str): - value as a string.
    :allFloat (bool): - True, causes only floats to be returned (i.e. no <int>)

OUTPUTs:
    :return (<float>): - the value_str converted to <float> or <int>
    :return (<bool>): - False, if value_str cannot be converted to <float>\
                        or <int>.
    '''

    # Default condition is that the number is a <float>
    if isfloat(value_str):
        isafloat = True
        value = float(value_str)
        # Parse the string value (candidate number) into two parts;
        # integer = before the decimal and mantissa is after the decimal.
        # split returns a list [integer,mantissa]
        # Tehcnically, use of the term 'integer' here is the 'characteristic'
        # but I used 'integer' beause it is shorter length in coding
        numberParsed = str(value_str).split(".")

        if len(numberParsed) > 1:
            integer = numberParsed[0]
            mantissa = numberParsed[1]

            if integer.isdecimal() and mantissa.isdecimal() and not allFloat:
                if int(mantissa) == 0:
                    # value is an integer; mantissa is 0
                    isafloat = False
                    value = int(integer)
            elif integer.isdecimal():
                # value is an integer; only integer is a value and mantissa is null
                isafloat = False
                value = int(integer)
        elif not allFloat:
            # value is an integer because .split() returned a single value list
            isafloat = False
            value = int(value_str)
    else:
        # value_str is cannot be converted to a <float> or <int>
        return False
    if showExtended:
        print("testValue: " + value_str + " | splits into: ", numberParsed,
              "\n value: ", value)
        if isafloat:
            print("It's a <float> (;o)\n")
        else:
            print("It's an <int> {:o)~\n")
    return value


def isfloat(numAsStr):
    '''returns True if can be converted to a `<float>` otherwise returns False.
    Only checks for one "." and no "," separators in the string.
    '''
    return str(numAsStr).replace(".", "", 1).isdecimal()


def main():
    print("\nHelper Classes and F(x) tools to augment Python built-in methods:\n" +
          "\n1. testArgs(name, *path) - tests passing *args\n" +
          " " * 7 + "(i.e. unNamed optional arguments to a function)\n" +
          "\n2. str_to_float_or_int(value_str, allFloat=False, showExtended=False)\n" +
          " " * 7 + "default - returns float or Int based on smallest type.\n" +
          " " * 7 + "allFloat - causes all values to be returned as float.\n" +
          " " * 7 + "showExtended - is for testing.\n" +
          "\n3. isfloat(numAsStr) - returns True if can be converted to a " +
          "<float>\n" + " " * 23 + "returns False if otherwise.\n"
          )


if __name__ == "__main__":

    main()


# --- Write Test Scripts below here ---
# testArgs("gene", "c:\\users\\lifygen\\projects\\python\\")
# testArgs("gene")