class MusicMachine(object):
    # A custom music player application
    # NOT USED in the answer excercise - just a concept
    # the following code frame is just a framework for
    # converting this into a MusicMachine class that manages a list of
    # both albums and songs.
    #import testclasses.MusicLibrary
    def __init__(self, songList=""):
    #
       self.me = "Music Machine"
       self.songList = songList
    
    def PlayRndSong(self, song="", songLibrary=""):
        if not songLibrary:
           #Note:  <Default_Home_Song_Lib> has to be setup as
           #       an <album> class object containing a group of songs 
           #       (or even better to get all songs on the hard drive)
           #songLibrary = Default_Home_Song_Lib 
           songLibrary=self.songList
           songLibrary.zPlayRandom()
        if not song:
           print "Playing a random song from the Song Library"
           songLibrary.zPlayRandom()
        else:
           songLibrary.zPlay           
    
    def playRndSongFromAlbum(self,album):
        # <album> = album object that contains a list of songs(<song ojbects>)
        print "play a random song"
        album.zPlayRandom()
    

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

def main():
    print "Hello World"
    
    
    
if __name__ == "__main__":
    
    main()

    # ***    
    #[Test #3] Chapter Excercise #2 test - Music Library / Song & Album classes 
    # ***    
    #playTime = "3:00"    #Use pTime[] instead of this line (see below)
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

    pTime=["4:24","5:12","5:25",'06:18',"2:06","4:11","4:17","4:51","7:34"]

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
    
    