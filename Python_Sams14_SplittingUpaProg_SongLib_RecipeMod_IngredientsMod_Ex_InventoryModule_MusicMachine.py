#  SAMS Python Chapter 14 (pp147 - 158) Training snippets, Quiz and Excercise
#  "Splitting up a Program (separating classes and funcitons)
# Course Training -
#**********************
# 1]  Include Modules (custom made modules) - see pp 152 -154
#     a.  import sys :  provides directory manipulation
#                       sys.path : provides a list of folders in the directory
#                                  (i.e. parent folder)
#     b.  use __init__.py :  usualy an empty file that indicats to Python to
#                            search for [packages] in the diretory where this is
#                            located.  putthing this empty file in the folder
#                            teslls Python that the folder is a [package] folder.
#                     Note:  Python will not let you load a class, say Student()
#                            even if you have Student() class in the local folder (or local path)
#                            unless "__init__.py" existing in the folder where
#                            Student.py resides.
#     c. RULE:  DO NOT USE "-" dashes in filenames (use udnerscore "_" instead).
#                              Python reserves dashes for special meaning.
#**********************
#  2]  Code Practice:
#       Restaurant Cook planned Classes:
#           Ingredient
#           Recipe (contains ingredients)
#           Inventory (contains indredients)
# ------------------------------------------------------
#  see "~/projects/python/classes/"
#  It contains the CLASS objects:
#           * Ingredient()
# ------------------------------------------------------
# Terms and definitions:
#  ( ) : a Tuple, a list of items that cannot be changed.
#  [ ] : a List,  a list of items that can be changed (added/remove
#                   items, re-order items) 
#                   my_List[x] is an index subscript list. so my_List[0] returns the 1st item
#                   (the 0th item is the 1st item) in the list.
#  { } : a Dict,  a list of paired items.  the first item of the pair is the
#                   name of "index" and the second item of the pair is the value.
#                   The value is referenced by using the index name.
#                   example, my_dict = {"fruit1":"Bannana", "one": 1}
#                            my_dict['one'] will return a 1
#                            my_dict['Fruit1'] will return a bannana





#**********************
# Questions:

# 1) Where does Python look for modules to import? 
#   [Answer]:  directories in the Python path that contain the
#              "__init__.py" file.
#
#     Note: a. The __init__.py files are required to make Python treat
#              directories containing the file as packages. This prevents
#              directories with a common name, such as string, unintentionally
#              hiding valid modules that occur later on the module search path.
#
#           b. The packages and/or modules within a package can be Imported
#              by ensuring that the package path is in the Python System path
#              and called via the dot naming convention
#              (files are case sensitive):
#
#              >>>import classes.recipes
#              >>>from recipes import recipe
#
#              # Change the path via the the following:
#              # 1st] Inspect the path
#              >>>import sys
#              >>>for item in sys.path:
#                     print item
#              # 2nd] Look at the path to determine the path text then construct
#              #      a valid path to your "classes" directory and add it to
#                     path:
#              >>>sys.path.append("C:\users\<username>\projects\pyton\classes")
#
#              # 3rd] (As a best practice) Add an empty file named "__init__.py" to <classes>
#              # to <classes> dirctory using a text editor or the IDLE editor.
#              
#              # 4th] Now you can use either of the following techniques to add
#              #      a module or package (on the command line or in a script):
#              >>>import classes.recipes      #add whole 'recipes' package
#              >>>from recipes import recipe  #add just a module called 'recipe'
#              

# 2) Why would you bother to split your code into more than one file?
#   [Answer]:  Make it easier to manage AND re-use [by another developer].
#               
# 3)  What does os.getcwd() return?
#   [Answer]:  Get Current Working Directory - it returns the operating system
#              directory where your current code is running from.
#       (NOTE: Not necessarily the directory where the script is stored!!!)

#***********
# EXCERCISE: P. 157-158
#***********
  
# 1) The cook has already written the ingredient module for you.  Now,
#   a.  write the inventory module in the same directoy as ingredients.py.
#   b.  create a new file called inventroy.py
#   c.  Inventory class should include the following:
#       1. A list of ingredients
#       2. How many of each ingredient is on-hand
#       3. A way to search the ingredients
#       4. A way to add items to the inventory
#       5. A way to remove items from the inventory
#
#   Hint:  Think what data type would work best for the ingredients;
#          it is not a list!

#  [Answer]:  See the inventory.py in the "classes" folder.





# 2) This chapter discussed a planned music library.  Write some fake classes
#    and functions, split them up as planned, and write the main file to use
#    them.  Do not worry about actual functionality (it does not need to play
#    songs).  Just make sure the attributes can actually be called as expected.
#    See pp 150 - 152
#    Functions:
#      a. Play a song 
#      b. Play a random song from the playlist (note, can treat an album as a playlist)
#      c. Play a random song off an album
#      d. Play a random album <not implemented but would be similar to how songs on albums are handled>
#      e. Play whole album in squential order (of number songs)
#
#    Test the class from a program:

class music(object):
    def __init__(self, name="", artist=""):
        while (not name):
             name = raw_input("what is the Title? :")
          
        while not artist:
            artist = raw_input("what is the artist/band's name? :")
        
        self.name = name
        self.artist = artist
        
    def chgName(self, Name):
        self.name = Name
        
    def chgArtist(self, Artist):
        self.artist = Artist
    

class Song(music):
    def __init__(self, name="", artist="", playTime="", genre="", musicFile=""):
        super(Song, self).__init__(name=name, artist=artist)
        while not musicFile:
           musicFile = raw_input("what is the full path musicFile? :")
           if not playTime:
               playTime = raw_input("what is the song's playTime? [MM:SS]: ")
               if not playTime:
                   playTime = "00:00"
           
        if not genre:
           genre = raw_input("what is the song's genre? :")
        
        self.playTime = playTime  
        self.genre = genre  
        self.musicFile = musicFile
        
    def chgMusicFile(self, musicFile):
        self.musicFile = musicFile
        
    def chgPlaytime(self, playTime):
        self.playTime = playTime
        
    def chgGenre(self, genre):
            self.genre = genre
                                
    def zPlay(self):
        #from playsound import playsound
        import webbrowser
        print "Playing {}...".format(self.name)  
        #webbrowser.open("C:\Users\Lifygen\Music\Panda1\Phil Collins - She's an Easy Lover.mp3")
        webbrowser.open(self.musicFile)
    
    def display(self):
        print self.name, self.artist
        print self.musicfile, self.playTime, "minutes    Genre=", self.genre
      

class Album(music):
    def __init__(self, name="", artist="", playTime="", genre="", songList=[], pubYear=""):
#        from datetime import time
        from datetime import datetime
        #datetime manipulation examples.  Following converts a string to a datetime object
        #str = '09/19/18 13:55:26'
        #datetime_object = datetime.strptime(str, '%m/%d/%y %H:%M:%S')
        T0 = datetime.strptime('00:00:00', '%H:%M:%S')
        
        super(Album, self).__init__(name=name, artist=artist)
        if not playTime:
           playTime = raw_input("what is the Album's playTime? [MM:SS]: ")
           if not playTime:
               playTime = "00:00"
        albumTime_TD = datetime.strptime(playTime, "%M:%S")-T0
        if not genre:
           genre = raw_input("what is the Album's genre? :")

        while not songList:
           try:
               songList = input("what is the Album song list? [song1, song2, ... songN]:")
               continue
           except KeyboardInterrupt:
               break
           except:
               songList=[]
               continue
           
        if not pubYear:
           pubYear = raw_input("what is the album publication year? :")
                       
        for song in songList:
            #print song.name
            if song.playTime:
               songTime_obj = datetime.strptime(str(song.playTime), "%M:%S")
               albumTime_obj = (songTime_obj + albumTime_TD)
               albumTime_TD = (albumTime_obj - T0)
            playTime = str(albumTime_TD)

            if genre:
               song.genre = genre
            elif song.genre:
               genre = song.genre
               
        self.playTime = playTime
        self.genre = genre
        self.songList = songList
        self.pubYear = pubYear


    def zShowSongs(self):
        maxSongName = max([len(song.name) for song in self.songList])
        i=0
        for song in self.songList:
            i+=1
            print (" " + str(i) + ") " + song.name + " "*(maxSongName-len(song.name)) + "\t [" + str(song.playTime) + "]")
        
    def zSongExists(self, songName):
        songExists = False
        for song in self.songList:
            if song.name == songName:
               songExists = song
               break
        return songExists
                
    def zPlay(self, songName):
        if type(songName) is int:
            if (songName-1) in range(len(self.songList)):
                songExists = True
                self.songList[songName-1].zPlay()
            else:
                songExists = False
        else:
            songExists = self.zSongExists(songName)
            if songExists:
               songExists.zPlay()
            else:
               songExists = False
        if not songExists:       
           print ("Try another song, the one you provided is not on the album.\n" +
                  "Choose one from the songs on this album:\n")
           self.zShowSongs()                        
      
    def zPlayAll(self):
        import time
        for song in self.songList:
            songTime_sec = (time.strptime(song.playTime,"%M:%S").tm_sec
                           +time.strptime(song.playTime,"%M:%S").tm_min * 60
                            )
            #self.zPlay(song.name)
            song.zPlay()
            time.sleep(songTime_sec+3)
    
    def zPlayRandom(self):
        from random import choice
        randomSong = choice(self.songList).name
        self.zPlay(songName=randomSong)
      
    def zShowMe(self):
        print " name:", self.name
        print " artist:", self.artist
        print " playTime:", self.playTime
        print " genre:", self.genre
        print " pubYear:", self.pubYear
        header = ("{band} - {title} Album Song List:".format(band=self.artist, title=self.name))
        print ("\n {header}\n".format(header = header) +
                " "+len(header)*"-")
        self.zShowSongs()

        
# ****************
# Class:  myTest
# ****************
class myTest(object):
    def __init__(self,
                 name="",
                 songList=[Song(name="name",
                               artist="Noone",
                               playTime=0,
                               genre=" ",
                               musicFile=" "
                               )]
                 ):
        if not name:
            name=raw_input("enter name: ")
        if not songList:
            songList=input("enter song list object: ")
          
        self.name =name
        self.songList = songList
    
    def Showme(self):
        print "Name: ", self.name
        for song in self.songList:
            print song.name
      



# ===================================================

# *** MAIN Program
def main():
    #Test the kitchen classes:  Ingredient(), Recipe(), Inventory()
    i = Ingredient(name = "egg")
    r = Recipe(name = "Scrambled eggs",
               ingredients = [i],
               directions = ['Break egg', 'Beat egg', 'Cook egg']
               )
    
    r.print_recipe()



if __name__ == "__main__":
    #[Test #1] Test the kitchen classes:  Ingredient(), Recipe(), Inventory()
    from classes.ingredients import Ingredient
    from classes.recipes import Recipe
    
    main()

    
    #[Test #2] Chapter Excercise #1 test - new Kitchen inventory
    import classes.inventory
    from classes.inventory import Inventory
    #import inventory
    print "Hello World\n"

    print "*** Testing sending a (Tuple) object into an Inventory object ***"
    aTuple=('apple', 'orange','bannana')
    print aTuple
    tI=Inventory(aTuple)
    tI.print_inventory()
    print '\n'

    print "*** Testing sending a {Dictionary} object into an Inventory object ***"
    aDict={'apple':1, 'orange':3,'bannana':5}
    print aDict
    dI=Inventory(aDict)
    dI.print_inventory()
    print '\n'

    print "*** Testing sending a [List] object into an Inventory object ***"
    aList=['Mary Anne', 'Cindy', 'Stan']
    print aList
    lI=Inventory(aList)
    lI.print_inventory()
    print '\n'

    print '*** Testing sending a "text" item into an Inventory object ***'
    aStr = "Gene"
    print aStr
    sI=Inventory("Gene")    
    sI.print_inventory()
    print '\n'

    print "Inventory.remove():  dI.remove('bannana')"
    dI.remove('bannana')
    dI.print_inventory()
    print '\n'

    print "Inventory.add():  dI.add('apple')"
    dI.add('apple')
    dI.print_inventory()
    print '\n'

    print "Hello World END"
    print '***************\n'


    # ***    
    #[Test #3] Chapter Excercise #2 test - Music Library / Song & Album classes 
    # ***    
    #playTime = "3:00"    #Use pTime[] instead of this line (see below)
    import classes.MusicMachine
    genre = "pop"
    albumTitle = "90125"
    band = "YES"
    songPath = "C:\\Users\\Lifygen\\Music\\"

    sFile = []
    sFile.append("YES - 90125 - 1 - Owner of a Lonely Heart.mp3")
    sFile.append("YES - 90125 - 2 - Hold On.mp3")
    sFile.append("YES - 90125 - 3 - It Can Happen.mp3")
    sFile.append("YES - 90125 - 4 - Changes.mp3")
    sFile.append("YES - 90125 - 5 - Cinema.mp3")
    sFile.append("YES - 90125 - 6 - Leave It.mp3")
    sFile.append("YES - 90125 - 7 - Our Song.mp3")
    sFile.append("YES - 90125 - 8 - City of Love.mp3")
    sFile.append("YES - 90125 - 9 - Hearts.mp3")

    name =[]
    name.append("Owner of a Lonely Heart")
    name.append("Hold On")
    name.append("It Can Happen")
    name.append("Changes")
    name.append("Cinema")
    name.append("Leave It")
    name.append("Our Song")
    name.append("City of Love")
    name.append("Hearts")

    pTime=["4:24","5:12","5:25",'6:18',"2:06","4:11","4:17","4:51","7:34"]

    sList = []
    for i in range(9):
        aSong = (Song(name = name[i],
                      artist = band,
                      playTime = pTime[i],
                      genre = genre,
                      musicFile = songPath + sFile[i]
                      )
                 )
                 
        sList.append(aSong)
        
    Album90125 = Album(name = albumTitle,
                       artist = band,
                       playTime = "00:00",
                       genre = genre,
                       songList = sList,
                       pubYear = "1981"
                       )

    Album90125.zShowMe()
    #Album90125.zPlayRandom()
    #Album90125.zPlayAll()
    
























