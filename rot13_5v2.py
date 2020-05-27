# Chapter 4 ; Selfinterest excercise
def rot13_5(myText):
# An Easter egg in Python is "The Zen of  Python" accessible by using <import this>
    import this
    #myText=""
    if (len(myText) == 0):

        myText = "Shannon:\nOk, I had an error in my code but I finally figured it out.\n"
        myText += "This is encrypted using symectric encryption keys:  \n"
        myText += "    + ROT-13 for alpha\n"
        myText += "    + ROT-5 for numeric\n"
        myText += '    + No translation for "space", punctuation, \n'
        myText += "      and special characters\n"
        myText += "\nNotepadd++ works great (i.e. better) for Python coding) because it is easier to see and maintain the code blocks."
        myText += "\nRegards,\n\nYu-Gene Chen\n623-680-9816"

    print "\n", myText,"\n" 

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
        except ValueError:
            #'-1' denotes the character is an alpha character
            x_value = -1
            
        if (x_value > -1):
            cyphered_ch = str(x_value%ROT5 + ROT5*abs(x_value/ROT5-1))
        else:
            #chr_input is an alpha character
            if ((ascii_num >= 65) and (ascii_num <= 90)):
                #character is A-Z
                x_value=ascii_num-65
                cyphered_ch = chr(x_value%ROT13 + ROT13*abs(x_value/ROT13-1)+65)
            elif ((ascii_num >= 97) and (ascii_num <= 122)):
                #character is a-z
                x_value=ascii_num-97
                cyphered_ch = chr(x_value%ROT13 + ROT13*abs(x_value/ROT13-1) + 97)
            else:
                #character is neither numeric nor alpha but is speical char, space, or punctuation
                #just transfer these characters without translation
                cyphered_ch = chr_input
        
        cyphered_msg = cyphered_msg + cyphered_ch

    # #print("".join([this.d.get(c, c) for c in this.s]))
    print "\nYTC_rot13_5-CYPHERED MSG:          \n" + cyphered_msg + "\n"
    #print "DeCyphered using ROT-13-Python:      \n" + ("".join([this.d.get(c, c) for c in cyphered_msg])) + "\n"
    # #ROT-13-Python cypher:  this.d = the stored Cypher table, gets each character in <myText> and replaces it with the cyphermap
    #print "Encrypted with ROT-13-Python-Cypher:_\n:  " + ("".join([this.d.get(c, c) for c in myText]))
    return cyphered_msg;
    
