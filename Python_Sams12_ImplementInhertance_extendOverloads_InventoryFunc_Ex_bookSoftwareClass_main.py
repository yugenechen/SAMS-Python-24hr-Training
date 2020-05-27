#  SAMS Python Chapter 12 (pp125 - 130) Training snippets, Quiz and Excercise
#  Classes and SubClasses (aka "inheritance")
# Course Training -
'''
  Note:  'object' is passsed into a custom class.  This is becuase it is the
         basis of ALL objects (if you declare it that way).  It is a built-in
         object class provided within Python so your new Class can inherit the
         properties and methods of Python's object().
         
         If you wanted <Student> to inherit <person> then you could pass 
         'person' into Student upon class declaration:  
                 def Student(person)
         Student would then inherit both person() and object() properties and 
         methods because person was built upon object and then Student was built
         upon person.
'''
#**********************
#  1] Built-in Extras
#     Comparing classes and printing out classes, creating basic
#     Note:
#      instead of using ch12 reading examples. just use student class built in
#      last chapter to create new student instances.  Try printing an comparing
#      them and note results on command line.

# ######################
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


# >>> person1 = person()
# >>> person2 = person()

# check to see if person1 and person2 are equivalent:
# >>> person1 == person2
# >>> False
# >>> print person1
  #How bizarre, cannot print the person object (person1 nor person2) and they
  #do not show as being equivalent even though the are identically instantiated.
  #(i.e. they are twins at birth)

#**********************
#  2] Built-in Extras - __eq__() - build an equality function
#     OK, I give in.  I will build a simple class to reduce typing instead of
#     re-using Student and the old person() class.  Build a new simpler person
#     and add an __eq__() method
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


# ######################
#  Series of functions to check the anomally seen in using
#  __gte__() and __lte__() as overloads for [>=] and [<=]
# ######################
def isGTError(a, b, methodResult):
    #Return TRUE if there is a mismatch in the result
    TrueResult =  (a>=b)
    if (TrueResult == methodResult):
        return False
    else:
        return True
# ------------------------------------------------
def isLTError(a, b, methodResult):
    TrueResult =  (a<=b)
    if (TrueResult == methodResult):
        return False
    else:
        return True
    
# ######################
# Test function to explore inconsistent results using __gte__() and __lte__()
# as overloads for [>=] and [<=]
# ######################
def Test():
    a = Pnum()
    b = Pnum()
    c = Pnum(age=0)

    print "---------" + "\t" + "---------" + "\t" + "---------"
    print "Person: a" + "\t" + "Person: b" + "\t" + "Person: c"
    print "---------" + "\t" + "---------" + "\t" + "---------"

    print "Age: " + str(a.age) + "\t" + "\tAge: " + str(b.age) + "\t" + "\tAge: " + str(c.age)

    print a.showMe()

    print "---------"
    print "---------"

    print ("a = Person()\n" +
           "b = Person()\n" +
           "c = Person(age=0)"+
           "\n"
           )
 
    print("[" + str(a.age) + "]a==c[" + str(c.age) + "]:  " + str(a==c) + "\n" +
          "[" + str(b.age) + "]b!=c[" + str(c.age) + "]:  " + str(a!=c) + "\n" +
          "[" + str(a.age) + "]a==b[" + str(b.age) + "]:  " + str(a==b) + "\n")

    print("[" + str(a.age) + "]a>=c[" + str(c.age) + "]:  "+ str(a>=c), gtCheck(a.age, c.age, (a>=c)))
    
    if ((a>=c) != (a.age>=c.age)):
          print("[" + str(a.age) + "]a.age>=c.age[" + str(c.age) + "]:  "+ str(a.age>=c.age) + "\n" +
                  "[" + str(a.age) + "]a.__gte__(c)" + str(c.age) + "=:  "+ str(a.__gte__(otherObj=c)) + "\n" +
                  "[" + str(c.age) + "]c.age>=a.age[" + str(a.age) + "]:  "+ str(c.age>=a.age) + "\n"
                 )
        
    print ("[" + str(b.age) + "]b>=c[" + str(c.age) + "]:  "+ str(b>=c), gtCheck(b.age, c.age, (b>=c)))

    print ("[" + str(a.age) + "]a>=b[" + str(b.age) + "]:  "+ str(a>=b), gtCheck(a.age, b.age, (a>=b)))
                

# ######################
def gtCheck(a,b,c):
    if ((a>=b) != c):
        return " ?!What!? How can this be?  " + str(a>=b) + str(c) + "\n"
    else:
        return "It Checks out!:)  " + str(a>=b) + str(c)
    


# ######################
# SAMS Python chapter 12:  Test Class Objects from pp 124 - 129
#  Note there is a major error in the SAMS book for >= and <= overload.
# ######################

# ######################
def main():
    #test the classes
    a = Person()
    b = Person()
    c = Person(age=0)

    print "---------" + "\t" + "---------" + "\t" + "---------"
    print "Person: a" + "\t" + "Person: b" + "\t" + "Person: c"
    print "---------" + "\t" + "---------" + "\t" + "---------"
    print "Name: " + a.name + "\t" + "Name: " + b.name + "\t" + "Name: " + c.name
    print "Age: " + str(a.age) + "\t" + "\tAge: " + str(b.age) + "\t" + "\tAge: " + str(c.age)

    print a.showMe()

    print "---------"
    print "---------"

   

    print ("a = Person()\n" +
           "b = Person()\n" +
           "c = Person(age=0)"+
           "\n"
           )
 
    print("[" + str(a.age) + "]a==c[" + str(c.age) + "]:  " + str(a==c) + "\n" +
          "[" + str(b.age) + "]b!=c[" + str(c.age) + "]:  " + str(a!=c) + "\n" +
          "[" + str(a.age) + "]a==b[" + str(b.age) + "]:  " + str(a==b) + "\n"
          )

    # errorCheck  [>=] and [<=]
    if (isGTError(a.age,c.age,(a>=c))):
        aGTEcResult = " ?!What!? How can this be?"
    else:
        aGTEcResult = ""

    if (isLTError(a.age,c.age,(a<=c))):
        aLTEcResult = " ?!What!? How can this be?"
    else:
        aLTEcResult = ""

    if (isGTError(b.age,c.age,(b>=c))):
        bGTEcResult = " ?!What!? How can this be?"
    else:
        bGTEcResult = ""

    if (isLTError(b.age,c.age,(b<=c))):
        bLTEcResult = " ?!What!? How can this be?"
    else:
        bLTEcResult = ""

    if (isGTError(a.age,b.age,(a>=b))):
        aGTEbResult = " ?!What!? How can this be?"
    else:
        aGTEbResult = ""

    if (isLTError(a.age,b.age,(a<=b))):
        aLTEbResult = " ?!What!? How can this be?"
    else:
        aLTEbResult = ""

     #Note:  Changed Person Class to use __ge__ () and __le__() methods.
     #           So, errors or logic mismatches should no longer occur.
    print(
          "[" + str(a.age) + "]a> c[" + str(c.age) + "]:  " + str(a>c) + "\n" +
          "[" + str(a.age) + "]a< c[" + str(c.age) + "]:  " + str(a<c) + "\n" +
           "\n" +
          "[" + str(a.age) + "]a>=c[" + str(c.age) + "]:  "+ str(a>=c) + aGTEcResult + "\n" +
          "[" + str(a.age) + "]a.age>=c.age[" + str(c.age) + "]:  "+ str(a.age>=c.age) + "\n" +
          "[" + str(a.age) + "]a.__gte__(c)" + str(c.age) + "=:  "+ str(a.__ge__(otherObj=c)) + "\n" +
           "\n" +
          "[" + str(a.age) + "]a<=c[" + str(c.age) + "]:  "+ str(a<=c) + aLTEcResult + "\n" +
           "\n" +
          "[" + str(b.age) + "]b> c[" + str(c.age) + "]:  " + str(b>c) + "\n" +
          "[" + str(b.age) + "]b< c[" + str(c.age) + "]:  " + str(b<c) + "\n" +
          "[" + str(b.age) + "]b>=c[" + str(c.age) + "]:  "+ str(b>=c) + "\n" + bGTEcResult + "\n" +
          "[" + str(b.age) + "]b<=c[" + str(c.age) + "]:  "+ str(b<=c) + "\n" + bLTEcResult + "\n" +
           "\n" +
          "[" + str(a.age) + "]a> b[" + str(b.age) + "]:  " + str(a>b) + "\n" +
          "[" + str(a.age) + "]a< b[" + str(b.age) + "]:  " + str(a<b) + "\n" +
          "[" + str(a.age) + "]a>=b[" + str(b.age) + "]:  "+ str(a>=b) + "\n" + aGTEbResult  + "\n"  +
          "[" + str(a.age) + "]a<=b[" + str(b.age) + "]:  "+ str(a<=b) + aLTEbResult + "\n"       
           )

    print "---------"
    print "Person: a"
    print "---------"
    a.showMe()
    print "---------\n"
    print "---------"
    print "Person: b"
    print "---------"
    b.showMe()
    print "---------\n"
    print "---------"
    print "Person: c"
    print "---------"
    c.showMe()
    print "---------\n"


# ######################
# Chapter 12 part 2:  Class Inheritance
# ######################
class InvItem(object):
    def __init__(self, title, description, price, store_id):
        self.title = title
        self.description = description
        self.price = price
        self.store_id = store_id

    def __str__(self):
        return self.title

    def __eq__(self, otherObj):
        if self.store_id == otherObj.title:
            return True
        else:
            return False

    def change_description(self, description=""):
        if not description:
            description = raw_input("Please enter a description: ")
        self.description = description

    def change_price(self, price=-1):
        while price < 0:
            price = raw_input("Please enter the new price [X.XX]:  ")
            try:
                price = float(price)
                break
            except:
                print "I'm sorry, but {} isn't valid".format(price)
        self.price = price

    def change_title(self, title=""):
        if not title:
            title = raw_input("Please give me a new TITLE:  ")
        self.title = title

#Define a book() class based on the InvItem() class
# Note:  instead of declaring with <object>; declare with teh <InvItem> as the object
class Book(InvItem):
    def __init__(self, title, description, price, format, author, store_id):
        super(Book, self).__init__(
                                    title = title,
                                    description = description,
                                    price = price,
                                    store_id = store_id
                                    )
        self.format = format
        self.author = author

    def __str__(self):
        book_line = "{title} by {author}".format(
            title = self.title,
            author=self.author)
        return book_line

    def __eq__(self, otherObj):
        if self.title == otherObj.title and self.author == otherObj.author:
            return True
        else:
            return False

    def change_format(self, format):
        if not format:
            format = raw_input("Please give me the new format:  ")
        self.format = format

        def change_author(self, author):
            if not author:
                author = raw_input("Please give me the new author:  ")
            self.author = author


# Books to create from the Book class [saves a bunch of re-typing]
hamlet = Book(title="Hamlet", description="A Dane has a bad time.", price = 5.99, format="paperback", store_id="29382918", author = "William Shakespeare")
hamlet_hb = Book("Hamlet", "A Dane has a bad time.", 10.99, "hardback", "William Shakespeare", "3894083920")
macbeth = Book("Macbeth", "Don't listen to strange ladies on the side of the road.", 4.99, "paperback", "William Shakespear","23928932")


#**********************
# Questions:

# 1) How do you customize what is returned when you print an instance of a class?
#   [Answer]:  Write an overload method for print() by defining a <__str__()> method.
#                    Note:  The overload function must return <a string> or an error will occur.

# 2) When  you override a comparison function, what is stored into self, and what is
#     sent as an argument?
#   [Answer]:  The local instance of the  object is stored into "self.  The object with
#                    its associated parameters and methods are passed into the function.
#                    Variables defined after <self> are passed into the function.
#                    Oh, the question is a==b; among <a> and <b>, which is passed into
#                    <self> and whichi is passed as an argument into  <otherObj>?
#                   [Answer]: <self> = a , <otherObj> = b
#


#***********
# EXCERCISE:
#***********
  
#1) Now that the Book() class is written, write a class for any software the
#    bookstore might sell.  Here is a list of requirements:
#    a) An operationg system
#    b) An ERSB rating(E, T, M, and so on...)
#    c) A function to change the OS
#    d) A function to change the rating
#    e) Don't forget to override the comparison and string functions too!

class SW(InvItem):
    def __init__(self, title, description, price, store_id, producer, OS, ERSB):
        super(SW, self).__init__(
                                    title = title,
                                    description = description,
                                    price = price,
                                    store_id = store_id
                                    )
        self.producer = producer
        self.OS = OS
        self.ERSB = ERSB
        
    def __str__(self):
        sw_overview = "{title} by {producer} rated {ersb}".format(
                                title = self.title,
                                producer = self.producer,
                                ERSB = self.ERSB
                                )
        return sw_overview

    def __eq__(self, otherObj):
        if ((self.title == otherObj.title) and (self.producer == otherObj.producer)):
            return True
        else:
            return False

    def change_OS(self, OS=""):
        # Note:  must but the "" as default otherwise <not OS> will not catch null pass-ins
        if not OS:
            OS = raw_input("Current OS = {}, please provide the new required OS:  ".format(self.OS))
        self.OS = OS

    def change_producer(self, producer=""):
        if not producer:
            producer = raw_input("Current producer = {}, please give me the new producer:  ".format(self.producer))
        self.producer = producer

    def change_ERSB(self, ERSB=""):
        while not ERSB or not ERSB in ("E", "T", "M"):
            ERSB = raw_input("Current rating = {}, please provide the new ERSB rating [E, T, M]:  ".format(self.ERSB))
        self.ERSB = ERSB

#Test the SW Class        
aSW = SW(title="Lemmings", description="try to escape; avoid falling off cliffs!", price=59.98, store_id="ISBN9281-562879", producer="SSI", OS="Longhorn", ERSB="T")


if __name__ == "__main__":
                       main()
                       #This can be used to override main() defaults when
                       # executing as a script using [F5] or
                       # using the menu [Run]->[Run Module]
                       #    changing to "main(1)" would run scenario 1
                       #    changing to "main(2)" would run scenario 2
                       #User entered values override this input and
                       #command line main() would run the default (without using this override)
                       

                       
        

        
    




























