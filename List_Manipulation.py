# -*- coding: utf-8 -*-
"""
Created on Wed May 06 16:51:14 2020

@author: Lifygen
"""

# ############################
# *** Functions ***
# ############################

def remDuplicates(myList):
    '''    
    #** ***************************
    #** Remove Duplicates in a list
    #** ***************************
    INPUTS:
       myList - list object
    OUTPUTS:
       returns the updated list (i.e. without duplicates)
    Created on Tue May  6 20:03:55 2020

    @author: Yu-Gene Chen
    '''
    for eachItem in myList:
        #Count the duplicate items.
        itemDuplicates = myList.count(eachItem)
        #Loop through the duplicate items and <list>.remove them.
        for i in range(1,itemDuplicates):
            myList.remove(eachItem)
     #return myList
     #OR a shorter way:  cast as <dict> removes duplicates (dup keys not allowed) 
     #   and recast back to <list>.
     return list(dict.fromkeys(mylist))



if __name__ == "__main__":
    PARTS2=[';','a', 'a','a','a', 'b','c','d','e','f',';', 'b', 'b', 'b','c','c','c','f','f','f']
    
#** **********************
    #Remove Duplicates in a list
#** **********************
    for eachItem in PARTS2:
        itemDuplicates = PARTS2.count(eachItem)   #Count the duplicate items
        for i in range(1,itemDuplicates):         #Loop through the duplicate items and .remove them (except for the 0th item)
            PARTS2.remove(eachItem)
            