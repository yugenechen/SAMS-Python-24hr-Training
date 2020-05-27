class person(object):
    #These are defined objet attributes or properties
    age = 27
    birth = '02/23/1993'
    expire = '?'
    ping = "Hello! :)"

    #This is an object method utilizing the .age property
    def print_a(self):
        print "Hello! I am {} years old".format(self.age)
        

# Ch 12 excercise
class Aperson(object):
    #These are defined objet attributes or properties
    def __init__(self):
        self.age = 27
        self.birth = '02/23/1993'
        self.expire = '?'
        self.ping = "Hello! :)"

    #This is an object method utilizing the .age property
    def showme(self):
        print "Hello! I am {} years old".format(self.age)
    

#**********************
# Pnum() class
# built to explore issues iwth using __gte() and __lte__() as overloads.
# ######################
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
    def __gte__(self, otherObj):
#        print ("CHECKER:  ", self.age, ">=", otherObj.age)
        if self.age >= otherObj.age:
            return True
        else:
            return False
        

#**********************
# Person() class        
#  Rewrote the Person class to replace __gte__() and __lte__() overloades
#  with __ge__() and __le__().
# ######################
class Person(object):
    def __init__(self,
                 name= "Noone",
                 age=27
                 ):
        self.name = name 
        self.age = age
        self.text = "Hello there {:)){-<',"
 
   #Used to compare self with another object        
    def __eq__(self, otherObj):
        if (self.name == otherObj.name and 
            self.age == otherObj.age
            ):
            return True
        else:
            return False

    def __ne__(self, otherObj):
        #Note:  calling the following with <otherObj> works fine because
        #           self is automatically passed.
        a = self.__eq__(otherObj=otherObj)
        if a:
            return False
        else:
            return True

    def showMe(self):
        print "My name: " ,self.name
        print "My age: " ,self.age

    #------------------------------
    # Note:  "__ge__()" is the overload for ">=" operator and NOT  "__gte__()"
    #           as listed in the SAMS Python book example and in Table 12.1.
    def __ge__(self, otherObj):
        print ("CHECKER:  ", self.age, ">=", otherObj.age)
        if (self.age >= otherObj.age):
            return True
        else:
            return False

    # Note:  "__le__()" is the overload for ">=" operator and NOT  "__lte__()"
    #           as listed in the SAMS Python book example and in Table 12.1.
    def __le__(self, otherObj):
        if (self.age <= otherObj.age):
            return True
        else:
            return False

    def __gt__(self, otherObj):
        if (self.age > otherObj.age):
            return True
        else:
            return False

    def __lt__(self, otherObj):
        if (self.age < otherObj.age):
            return True
        else:
            return False

    def __str__(self):
        #This __str__() is used to overload the "print()"
        whoAmI = self.text + "\n------------------------------\n"
        whoAmI += (" <me>.name = " + str(self.name) + "\n <me>.age    = " + str(self.age) +
        '\n <me>.text   =  "' + str(self.text) + '"\n---------------------------\n' + " My methods are:\n---------------------------\n" +
        " .showMe() = shows my name and age.\n" +
        " Arithmetic Operatos: [ =, >, < >=, <= ],  where these compare <me>.age to the external value.\n" +
        " print <me>:  shows this print out detailing my properties and methods :o)~")
                           
        return whoAmI
        
        
        #I would like to go further in coding here than what is in the book.
        #I agree that as in the book, a programmer may want to compare a subset
        #of attributes.  However, I would like to compare ALL attributes with
        #a loop; will have to research this if not covered in this chapter.
    

#**********************
#  2]# The original Person() class
#     ORIGINAL Built-in Extras example using __gte__() and __lte__() that did
#     not work as a ">=" and "<=" overload.
#     Built a simpler class to reduce typing instead of re-using Student and
#     the old person() class.  the following is a new simpler person
#     with __eq__(), __gte__(), __lte__ and other common methods overloaded.
# ######################
class Person_original(object):
    def __init__(self,
                 name= "Noone",
                 age=27
                 ):
        self.name = name 
        self.age = age
        self.text = "Hello there {:)){-<',"
 
   #Used to compare self with another object        
    def __eq__(self, otherObj):
        if (self.name == otherObj.name and 
            self.age == otherObj.age
            ):
            return True
        else:
            return False

    def __ne__(self, otherObj):
        #Note:  calling the following with <otherObj> works fine because
        #           self is automatically passed.
        a = self.__eq__(otherObj=otherObj)
        if a:
            return False
        else:
            return True

    def showMe(self):
        print "My name: " ,self.name
        print "My age: " ,self.age

    #------------------------------
    # Note:  "__ge__()" is the overload for ">=" operator and NOT  "__gte__()"
    #           as listed in the SAMS Python book example and in Table 12.1.
    def __gte__(self, otherObj):
        print ("CHECKER:  ", self.age, ">=", otherObj.age)
        if (self.age >= otherObj.age):
            return True
        else:
            return False

    # Note:  "__le__()" is the overload for ">=" operator and NOT  "__lte__()"
    #           as listed in the SAMS Python book example and in Table 12.1.
    def __lte__(self, otherObj):
        if (self.age <= otherObj.age):
            return True
        else:
            return False

    def __gt__(self, otherObj):
        if (self.age > otherObj.age):
            return True
        else:
            return False

    def __lt__(self, otherObj):
        if (self.age < otherObj.age):
            return True
        else:
            return False

    def __str__(self):
        #This __str__() is used to overload the "print()"
        whoAmI = self.text + "\n------------------------------\n"
        whoAmI += (" <me>.name = " + str(self.name) + "\n <me>.age    = " + str(self.age) +
        '\n <me>.text   =  "' + str(self.text) + '"\n---------------------------\n' + " My methods are:\n---------------------------\n" +
        " .showMe() = shows my name and age.\n" +
        " Arithmetic Operatos: [ =, >, < >=, <= ],  where these compare <me>.age to the external value.\n" +
        " print <me>:  shows this print out detailing my properties and methods :o)~")
                           
        return whoAmI
