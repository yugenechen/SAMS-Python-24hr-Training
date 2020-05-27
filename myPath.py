# -*- coding: utf-8 -*-
"""
Created on Mon May 04 10:56:41 2020

@author: Lifygen

This program - shows the current Python path,
               adds the "classes" folder to the Python path, and
               redisplays the path after "classes" has been added.


    Run the following every time:
    >>>import site
    >>>site.addsitedir(".")
"""
class myPath(object):
    me = "Add local project path and 'classes' to the Python Path."
        
    def run(self):
        print("Show existing folders that make up python path:\n" +
              "----------------------------------------------")
        import sys
        for each in sys.path:
            print each

        print '\nAlways start by adding the "classes" folder to the python path:'
        if not ("C:\Users\Lifygen\projects\python\classes" in sys.path):
            sys.path.append("C:\Users\Lifygen\projects\python\classes")
        if not ("C:\Users\Lifygen\projects\python" in sys.path):
            sys.path.append("C:\Users\Lifygen\projects\python")
        for each in sys.path:
            print each
            
    def __str__(self):
        return self.me






if __name__ == "__main__":
    '''This should always be the last line or last code group of any file.
       It enables the file to run as a script and can be used to run any
       program or just type in the code to run as a sript.
    '''
    print "Hello World/n"  #this is a script line
    m=myPath()      #Change this line to a different program call to run something
                #other than main(), Or put script here (or after here).
    m.run()
    print "You can also use the [PYTHONPATH manager] tool in Acaconda-Spyder."