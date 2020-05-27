class Pnum(object):
    def __init__(self,
                 age=27
                 ):
        self.age = age
 
   #Used to compare self with another object        
    def __eq__(self, otherObj):
        if self.age == otherObj.age:
            return True
        else:
            return False

    def __ne__(self, otherObj):
        a = self.__eq__(otherObj=otherObj)
        if a:
            return False
        else:
            return True

    def showMe(self):
        print "My age: " ,self.age

    #------------------------------    
    def __ge__(self, otherObj):
#    def __gte__(self, otherObj):        
#        print ("CHECKER:  ", self.age, ">=", otherObj.age)
        if self.age >= otherObj.age:
            return True
        else:
            return False

def Test():
    a = Pnum()
    b = Pnum()
    c = Pnum(age=0)

    print "---------" + "\t" + "---------" + "\t" + "---------"
    print "Person: a" + "\t" + "Person: b" + "\t" + "Person: c"
    print "---------" + "\t" + "---------" + "\t" + "---------"

    print "Age: " + str(a.age) + "\t" + "\tAge: " + str(b.age) + "\t" + "\tAge: " + str(c.age)

    print "---------"
    print "Printing a.showMe: "
    a.showMe()
    print "---------"

   

    print ("a = Person()\n" +
           "b = Person()\n" +
           "c = Person(age=0)"+
           "\n"
           )
 
    print("[" + str(a.age) + "]a==c[" + str(c.age) + "]:  " + str(a==c) + "\n" +
          "[" + str(b.age) + "]b!=c[" + str(c.age) + "]:  " + str(a!=c) + "\n" +
          "[" + str(a.age) + "]a==b[" + str(b.age) + "]:  " + str(a==b) + "\n")
    print(
          "[" + str(a.age) + "]a>=c[" + str(c.age) + "]:  "+ str(a>=c), gtCheck(a.age, c.age, (a>=c)))

    if ((a>=c) != (a.age>=c.age)):
          print("[" + str(a.age) + "]a.age>=c.age[" + str(c.age) + "]:  "+ str(a.age>=c.age) + "\n" +
                "[" + str(a.age) + "]a.__ge__(c)" + str(c.age) + "=:  "+ str(a.__ge__(otherObj=c)) + "\n" +
                "[" + str(c.age) + "]c.age>=a.age[" + str(a.age) + "]:  "+ str(c.age>=a.age) + "\n" )

#                "[" + str(a.age) + "]a.__gte__(c)" + str(c.age) + "=:  "+ str(a.__gte__(otherObj=c)) + "\n" +
        
    print ("[" + str(b.age) + "]b>=c[" + str(c.age) + "]:  "+ str(b>=c), gtCheck(b.age, c.age, (b>=c)))

    print ("[" + str(a.age) + "]a>=b[" + str(b.age) + "]:  "+ str(a>=b), gtCheck(a.age, b.age, (a>=b)))
                

def gtCheck(a,b,c):
    if ((a>=b) != c):
        return " ?!What!? How can this be?  " + str(a>=b) + str(c) + "\n"
    else:
        return "It Checks out!:)  " + str(a>=b) + str(c)


# This must be the last line of the file (other than whitespace) so that the
# the file can run as a script.  
if __name__ == "__main__":
                       Test()
