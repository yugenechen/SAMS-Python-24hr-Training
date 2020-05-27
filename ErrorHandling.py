# -*- coding: utf-8 -*-
"""
Exception Handling Tips
https://docs.python.org/3/tutorial/errors.html

Created on Wed May 27 11:35:27 2020

@author: Lifygen
"""
# ----------------------------
# ERROR Testing:  Try/Except
# ----------------------------
invFileName = 'Gene.txt'
try:
    inventory_file = open(invFileName)
except IOError as e:
    print("s.message:  ", e.message)
    print("e.strerror:  ", e.strerror)
    print("e.filename:  ", e.filename)
    print("e.errno:  ", e.errno)
    print("e.args:  ", e.args)
    print("")
    print("I/O error({0}): {1}".format(e.errno, e.strerror))
except Exception as e:
    print("s.message:  ", e.message)
    print("e.strerror:  ", e.strerror)
    print("e.filename:  ", e.filename)
    print("e.errno:  ", e.errno)
    print("e.args:  ", e.args)
    print("")
    print("I/O error({0}): {1}".format(e.errno, e.strerror))
    print("***************************************************************")
    print(type(e))    # the exception instance
    print(e.args)     # arguments stored in .args
    print(e)          # __str__ allows args to be printed directly,
                      # but may be overridden in exception subclasses
    # unpack args
... # x, y = inst.args
... # print('x =', x)
... # print('y =', y)


#    inventory_file= open(invFileName, 'w+')
#
#    readLines = inventory_file.readlines()
#    inventory_file.close()
