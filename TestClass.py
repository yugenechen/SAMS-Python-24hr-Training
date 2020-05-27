#This was built to exlpore passing a list of objects (custom class instances)
#due to issues with implementing SAMS-Python-Ch14-Excercise #2.

#*** New class: song ***
class song(object):
      def __init__(self, name="", artist="", path="", file=""):
          while (not name):
               name = raw_input("what is the song's name? :")
            
          while not artist:
               artist = raw_input("what is the artist's name? :")

          while not path:
               path = raw_input("what is the full filepath to the song directory? :")
          
          while not file:
               file = raw_input("what is the song filename? :")
          self.name = name
          self.artist = artist
          self.path = path
          self.file = file
          
      def zPlay(self):
          import webbrowser
          print "Playing {}...".format(self.name)  
          #webbrowser.open("C:\Users\Lifygen\Music\Panda1\Phil Collins - She's an Easy Lover.mp3")
          webbrowser.open(self.path + self.file)

      def zShowme(self):
            print ("name: {}\nartist: {}\npath: {}\nfile: {}".format(
                    self.name, self.artist, self.path, self.file))
      

#*** New class: album ***
class album(object):
      def __init__(self, name="", band="", songList=[]):
          while (not name):
               name = raw_input("what is the Album name? : ")
          
          while (not band):
               artist = raw_input("what is the band's name? : ")
          
          while (not songList):
              try:
                    songList = input("Input a list of songs objects: ")
                    if not songList[0].name:
                       songList=[]      
                    continue
              except KeyboardInterrupt:
                    break
              except:
                    songList=[]
                    continue
          
          self.name = name
          self.artist = artist
          self.songList = songList
          
      def zShowme(self):
            print ("name: {}\nartist: {}\n\n".format(self.name, self.band))
            for song in songList:
                print song.name
      

#*** New class: person ***
class person(object):
    def __init__(self, name="", age="", family=""):
        from random import choice
        from random import randint
        vowel = ["a", "e", "i", "o", "u"]
        conso = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        #Generate a randomly constructed name for the person
        randLen = randint(1,7)
        if not name:
          fN = choice(conso)
          fN = fN.upper()
          if fN == "Q":
             fN += "u"
             chooseVowel = True
             while len(fN) < randLen:
                if chooseVowel:
                   fN+=choice(vowel)
                   chooseVowel = False
                else:
                   fN+=choice(conso)
                   chooseVowel = True
          name = fN
        if not age:
           age = randint(0,1000)
        
        self.name = name
        self.age = age
        self.family = family
    
    def zShowme(self):
        #print(" My info: (name, age, family)\n"+
        #      " -------------")
        print self.name, str(self.age).rjust(4," "), self.family
    

#*** New class: aTestList ***
class aTestList(object):
    def __init__(self, myList=[]):
        while not myList:
            try:
                  myList = input("Enter list of instances: ")
                  if not myList[0].name:
                     myList=[]      
                  continue
            except KeyboardInterrupt:
                  break
            except:      
                  myList=[]
                  continue
            
        self.myList = myList
    
    def fixFamily(self):
        ancestory = ["Elven", "Dwarven", "Human", "Orcen", "Floresiensian"] 
        from random import choice
        for person in self.myList:
            if not person.family:
                person.family = choice(ancestory)
    
    def zShowme(self):
        print(" --------------------\n" +
                      " List of items: \n" +
                      "|Class(aTestList)|\n"+
              " --------------------\n" +
                      " Manually constructed:  \n" +
                      " --------------------"
                      )
        i = 0
        for item in self.myList:
            name = self.myList[i].name
            age = self.myList[i].age
            family = self.myList[i].family
            print ("[" + str(i) + "]" + "  " +
                               name  + "    \t" +
                               str(age).rjust(4," ")  + "    \t" +
                               family
                               )
            i += 1
        
    def zShowme2(self):
        print(" --------------------\n" +
                      " List of items: \n" +
                      "|Class(aTestList)|\n"+
              " --------------------\n" +
                      " Auto-constructed:  \n" +
                      " --------------------"
                      )
        i = 0
        for item in self.myList:
        #    name = self.myList[i].name
        #    age = self.myList[i].age
        #    family = self.myList[i].family
            print ("[" + str(i) + "]" + "  " +
                               item.name + "    \t" +
                               str(item.age).rjust(4," ") + "    \t" +
                               item.family
                              )
            i += 1


#*** New Function: TestList ***
def TestList(heroList=[]):
    while not heroList:
        try:
              heroList = input(" Invalid list input. Try again using the following list format:\n" +
                               "\t[hero1,hero2,...,heroN],\n" +
                               " where 'hero#' = is a person() classs object.\n" +
                               " Enter hero list: ")
              if not heroList[0].name:
                     heroList=[]
              continue
        except KeyboardInterrupt:
              break
        except:
              heroList=[]
              continue
                
    print("\n List of items: \n"+
            " -------------")
    i = 0
    for item in heroList:
        i+=1
        print(" " + str(i) + ")  " + item.name + "      \t" +
                      str(item.age).rjust(4," ")+ "    " + str(item.family)
                      )
    print ""
    
    

    
#*** MAIN ***
def main():
      # Test to exlpore passing a list of objects (custom class instances) to a funciton
      # and have the function display the object.parameters from each object in the list.

      print ("Programmatically creating person instances that exists within main().\n"+
             "These vaiables do not exist within Python Shell environment (out of scope),\n"+
             "ie. not accessible from the Python Shell command line.")

      print ""

      # Create some instances of the custom person() class
      print ("Creating some instances of person() class with fixed names:\n"+
             'p1 = person("Mary Anne")\n' +
             'p2 = person("cindy")\n' +
             'p3 = person("Michel")\n')
      p1 = person("Mary Anne")
      p2 = person("Cindy")
      p3 = person("Michel")

      # Create a list of person objects and store it as the variable 'hList'
      print ("Creating list of persons from p1-p3, new fixed name person() instances:\n"+
             'hList = [p1, p2, p3]\n')
      hList = [p1, p2, p3]
      for item in hList:
            item.zShowme()
      
      # [main() Test #1]: Call a function and feeding it a list of person
      #                   objects, where the function can access person objects.
      print "TestList(hList)\n"
      TestList(hList)
      #The result of the above call should be that it prints out the name, age, family of each person in the list

      # [main() Test #2]: Receive a list of person objects as a User Input and
      #                   show the attributes of each person.
      #         Note:  This test goes a step further and does not just access
      #                the attributes but also uses a person method!!!
      inputList=[]
      while not inputList:
          try:
              inputList = input('[From main()]:  Enter < hList > variable: ')
              if not inputList[0].name:
                     inputList=[]
              continue
          except KeyboardInterrupt:
              break
          except:      
              inputList=[]
              continue
      print "********************"
      print "Showing [inputList]:"
      print "-------------------"
      for item in inputList:
            item.zShowme()
      print "*End of [inputList]*"
      print "********************"
      print ""
      

if __name__ == "__main__":
      #This can be used to override main() defaults when executing as a script 
      #using [F5] or using the menu [Run]->[Run Module] :
      #    changing to "main(1)" would run scenario 1
      #    changing to "main(2)" would run scenario 2
      #User entered values override this input and command line main() would 
      #run the default (without using this override).
      #Oh, to override main() then call a different function than <main() 
      #(in plade of where it is called below):

      #BEGIN Red Herring   
      #myList not used in this test, (not yet anyway)
      print ("\n************************\n" +
             "[Begin Red Herring test]" +
             "\n************************")
      print "myList = ['Mary Anne', 'Cindy', 'Michel', 'Max', 'Paul', 'Yu-Gene', 'Susan', 'Barbara']"
      myList = ['Mary Anne', 'Cindy', 'Michel', 'Max', 'Paul', 'Yu-Gene', 'Susan', 'Barbara']
      print myList
      print "*** End Red Herring test ***"
      #END of Red Gerring      
      
      print '# -----------------------------------------------------'
      print '# Begin test of passing a list of object instances'
      print '# -----------------------------------------------------'

      #[Test #1 and Setup]:  Programmaticaly generate person objects, put them in a list,
      #                      print out the attributes of each object in the list. 
      #
      #               Create some instances of a custom object (used custom person() class).
      #               Mimics main() as a script to create local variables in the Shell 
      #               environment because I am too lazy to keep creating the list manually 
      #               every time I run the test.
      #
      print ("\n*********" +
             "\n[Test #1]:  Create Local vars & run Local Script showing persons from the list:" +
             "\n*********")  
      #(1) Create some instances of a custom object (used custom person() class).
      print "Create Python Shell variables, instances of the person() class:"
      p1 = person("Cindy")
      p2 = person("Max")
      p3 = person("Susan")
      #    for p4 I let the class auto-generate the attributes (i.e. notice I do not feed any values into the attributes)
      p4 = person()

      print "==========="
      print "p1 info: ";p1.zShowme()
      print "==========="
      print "p2 info: ";p2.zShowme()
      print "==========="
      print "p3 info: ";p3.zShowme()
      print "==========="
      print "p4 info: ";p4.zShowme()
      print "==========="
      print ""
      
      #(2) Create the hero list [of person object instances]
      print "Create Python Shell list of person() instances, store as 'hList':"
      print "hList = [p1, p2, p3]"
      hList = [p1, p2, p3]
      #Display info from person intances that comprise the person list      
      i=0
      for item in hList:
          i+=1
          print " p" + str(i) + ": " + item.name + "    \t", str(item.age).rjust(4," "), item.family
      print ""
      
      print "Test apppend method of the <list> type:"
      print "hList.append(p4)"
      hList.append(p4)

      print "\nShow new hList with p4 appended:"
      #(3) Print info from the hero list [of person object instances], to prove info is there.
      i=0
      for item in hList:
          i+=1
          print " p" + str(i) + ": " + item.name + "    \t", str(item.age).rjust(4," "), item.family


      #[Test #2]  Run main() , where the program in main tests passing a list of     
      #                custom objects to a function() and the function effectively        
      #                uses the objects contained in the list. 
      print ("\n*********" +
             "\n[Test #2]:  Run main() that tests passing [<...person list...>] to a function."+
             "\n*********")
      main()
      
            
      #[Test #3]  Make use of User Input object list within a local memory environment
      #           Obtain User Input (from keyboard) of a hero list and
      #           Print info from the User Input hero list [of person object instances],
      #           to prove info made it in as an INPUT.
      print ("\n*********" +
             "\n[Test #3]:  Solicit User Input of person list and then use the list:" +
             "\n*********")
      inputList=[]
      while not inputList:
          try:
                inputList = input('\n[From Script]:  Enter < hList > variable: ')
                if not inputlist[0].name:
                      inputList=[]      
                continue
          except KeyboardInterrupt:
                break
          except:
                inputList=[]
                continue
          
      for item in inputList:
            item.zShowme()

      #[Test #4]  From within a Class, accept a User Input list of custom objects,
      #           then from the Class, display info from the objects within the list.
    
      #aTestList(object):
      # is bakcup working?
      import sys
      print(Sys.version)