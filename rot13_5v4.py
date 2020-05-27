# Chapter 4 ; Selfinterest excercise
def rot13_5(myText):
# An Easter egg in Python is "The Zen of  Python" accessible by using <import this>
    import this
    print "The folloinwg text shall be encoded:  \n",myText,"\n" 

    #Cypner ROT-18 example (combo use of ROT-13 and ROT-5)
    #Inspired by ZEN manifesto (import this) that uses ROT-13
    ROT5 = 5    #for numerics cypher for 0-9 (ASCHII 48-57)
    ROT13 = 13  #for alpha cypher for A-Z (ASCHII 65-90), a-z (ASCHII 97-122)

    cyphered_msg = ""
    cyphered_ch = ""
    for chr_input in myText:
    #Convert the input character to its ASCHII numerical value
    #and check if the charater is a numeric (i.e. 0-9 and not an alpha character)
        try:
            ascii_num = ord(chr_input)
            x_value = int(chr_input)
            #Numeric <chr_input> so process the encoding here otherwise use the exception path for Alphabetic encoding
            #Determines (using "mod" math) how many times the pointer has gone around the code wheel to determine 0-4 set or 5-9 set
            cyphered_ch = str(x_value%ROT5 + ROT5 * abs(x_value/ROT5 - 1))
        except ValueError:
            #Alphabetic <chr_input> causes an Exception so use ASCII number value of the alphabetic chacter
            if ((ascii_num >= 65) and (ascii_num <= 90)) or ((ascii_num >= 97) and (ascii_num <= 122)):
                #subtract the offset to bring the start postion back to 0 for mathematical caluclating the pointer on the code wheel.
                if ((ascii_num >= 65) and (ascii_num <= 90)):
                    #character is A-Z:  the offset is the postion of the first character "A" on the ASCII table
                    ascii_offset = 65
                elif ((ascii_num >= 97) and (ascii_num <= 122)):
                    #character is a-z:  the offset is the position of the first character "a" on the ASCII table
                    ascii_offset = 97
                x_value = ascii_num - ascii_offset
                cyphered_ch = chr(x_value%ROT13 + ROT13 * abs(x_value/ROT13 - 1) + ascii_offset)
            else:
                #character is neither numeric nor alpha but is speical char, space, or punctuation
                #just transfer these characters without translation
                cyphered_ch = chr_input
        cyphered_msg = cyphered_msg + cyphered_ch
        
    return cyphered_msg;
    #myText_encrypted = rot13_5("<type message here")
    #print myText_encrypted
