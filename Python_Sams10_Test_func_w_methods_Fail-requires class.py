# -*- coding: utf-8 -*-
"""
Created on Sat May 02 11:11:54 2020

@author: Lifygen
"""

def Test(a=0,b=0):
    #I want to see if a function can be built with methods without declaring
    #it as a class.
    #
    #[Answer]: NO.  Test().Add() or Test.Add cannot be called as a method.  
    #          However, Add() can be used by Test()
    #import sys
    def Add(x,y):
        result = x+y
        return result
    
    def getValue(x,label="first"):
        while not x: 
            try:
                x=input("Input the {label} value to add (#): ".format(label=label))
                x = float(x)
                continue
            except KeyboardInterrupt:
                print("\n\nUser initiated [Break] or [exit] detected. Stopping Progarm now....")
                raise SystemExit("User Initiated [Break]!")
                #The following line requires <import sys> package
                #sys.exit("User Initiated [Break]!")
            except Exception:
                x=""
                print("Invalid entry, please retry using a numeric entry value (real or integer #")
                continue
        return x
    
    print ("I am an adding machine. program.  Just feed me two numbers using\n"+
          "Test(x,y) format to add x and y.")
        
    if not a: 
        a = getValue(a,"first")
    if not b:
        b = getValue(b,"second")        
    
    return Add(a,b)
