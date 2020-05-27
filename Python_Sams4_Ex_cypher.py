# Chaptor 4 ; Selfinterest excercise

# An Easter egg in Python is "The Zen of  Python" accessible by using <import this>
import this

myText = "helloHello 27 I LOVE Mary Anne Chen; she is 29 years old."
print "\n", myText,"\n" 

#Cypner ROT-18 example (combo use of ROT-13 and ROT-5)
#Inspired by ZEN manifesto (import this) that uses ROT-13

ROT5 = 5    #for numerics cypher for 0-9 (ASCHII 48-57)
ROT13 = 13  #for alpha cypher for A-Z (ASCHII 65-90), a-z (ASCHII 97-122)

text_length = len(myText)
cyphered_msg = ""
cyphered_ch = ""
for chr_input in myText:
    #Convert the input character to its ASCHII numerical value
    #and check if the charater is a numeric (i.e. 0-9 and not an alpha character)

    #print chr_input
    #print "Execute try]:"

    try:
        ascii_num = ord(chr_input)
#       print "aschii_num= ", ascii_num
        x_value = int(chr_input)
#        print "x_value= ", x_value

        
    except ValueError:
#        print "Execute Exception]:"
        #'-1' denotes the character is an alpha character
        x_value = -1
        

#    print "[Continue main Program Execution]: x_value= ", x_value
    if (x_value > -1):
#        print "Execute numeric cypher]:"
        cyphered_ch = str(x_value%ROT5 + ROT5*abs(x_value/ROT5-1))
#        print cyphered_ch, x_value, ROT5, abs(x_value/ROT5-1)
    else:
        #chr_input is an alpha character
        if ((ascii_num >= 65) and (ascii_num <= 90)):
        #character is A-Z
#            print "Execute A-Z]:"
            x_value=ascii_num-64
            cyphered_ch = chr(x_value%ROT13 + ROT13*abs(x_value/ROT13-1)+64)
#            print "character is A-Z [" + chr_input + "]", + x_value%ROT13 + ROT13*abs(x_value/ROT13-1)+64
        elif ((ascii_num >= 97) and (ascii_num <= 122)):
        #character is a-z
#            print "Execute a-z]:"
            x_value=ascii_num-96
            cyphered_ch = chr(x_value%ROT13 + ROT13*abs(x_value/ROT13-1) + 96)
#            print "character is a-z [" + chr_input + "]", + x_value%ROT13 + ROT13*abs(x_value/ROT13-1)+64
        else:
            cyphered_ch = chr_input

#    print "[Main Program Execution, Build <cyphered_msg>]:"            
    cyphered_msg = cyphered_msg + cyphered_ch
#    print cyphered_ch
#    print cyphered_msg

print("".join([this.d.get(c, c) for c in this.s]))
print "YTC-CYPHERED MSG________:  " + cyphered_msg
print "ROT-13-Python-DeCyphered:  "+ ("".join([this.d.get(c, c) for c in cyphered_msg]))
print "ROT-13-Python-Cyphered__:  " + ("".join([this.d.get(c, c) for c in myText]))
