# -*- coding: utf-8 -*-
"""Test, explore, passing arguments to a Python script and executable 
(both .pyc and .exe)
Created on Fri Jun 12 16:11:33 2020

@author: ychen
"""

import sys
print("Number of arguments:", len(sys.argv), "arguments.")
print("Argument List:", str(sys.argv))

"""Run the following line from the DOS command line within the directory 
   containing the pythone script file (in this case "testArg2.py"):
python testArg1.py fn=Add_Example_temp.py a=-3 b=-55 -echo baseball names cheeks
"""