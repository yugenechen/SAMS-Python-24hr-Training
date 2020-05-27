# Chapter 4 ; Selfinterest excercise
def myROT18(myText):
# An Easter egg in Python is "The Zen of  Python" accessible by using <import this>.
    #Cypher ROT-18 example (combo use of ROT-13 and ROT-5).
    #Inspired by ZEN manifesto (import this) that uses ROT-13.
    alphabetItems = 26  # number of letters in the alphabet.
    base10Items = 10    # number of base numbers and a 10base system.
    #ROT5 = 5            # half numbeRange for numerics rotational cypher
    #                     for 0-9 (ASCHII 48-57).
    #ROT13 = 13          # half alphaRange for alphabet rotational cypher
    #                     for A-Z (ASCHII 65-90), a-z (ASCHII 97-122).
    AlphaOffset = 65    # ASCII start position for uppercase alphabet "A-Z".
    alphaOffset = 97    # ASCII start position for lowercase alphabet "a-z".
    numOffset = 48      # ASCII start position for numerics "0-9".
    cyphered_msg = ""   # encrypted message

   #Create the Cypher translation data set:
   #Create a blank translation encoding data set (or clear the dataset).
    cypher={}
    #Calculate the map to character for each alphabetic character
    #    starting with each Alpha and alpha ASCII start position to
    #    create a circular reference from A-Z and a-z using an offset that is
    #    half the items in the list (or range).  For Alphabet offset =13.
    #    Add a circular reference cypher from 0-9 with an offset that is
    #    half numbers in the set.  Offset = 5 for numbers set 0-9.
    #    Note, using an offset of half the items in a list creates a
    #          symmetrical cypher.  The key is both the encryption cypher
    #          and decryption cypher.
    for asciiStartValue in (numOffset, AlphaOffset, alphaOffset):
        if (asciiStartValue >= 65):        #alphabet uses ROT13
            ListItems = alphabetItems
        else:
            ListItems = base10Items
        ROT = ListItems/2
        
        #Calculate each element of the cypher dataset, which is a alpha map
        for eachItemIndex in range(ListItems):
            cypher[chr(eachItemIndex + asciiStartValue)] = chr((eachItemIndex + ROT) %(ListItems) + asciiStartValue)
            
    #print cypher
    #Encode the message
    cyphered_msg +=  "".join([cypher.get(ch, ch) for ch in myText])
        
    return cyphered_msg;
    #myText="<type message here>"; encryptedMsg = myROT18(myText); print encryptedMsg
