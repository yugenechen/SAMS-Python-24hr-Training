"""Python_Sams20, p 221-240, Developing for the Web with Flask \
1. What is delivered in the Flask framework.
2. Installing Flask
3. Creat a Flask app
4. Add templates to Flask app
5. When to use frameworks in the real world\

'Thu, May 21, 2020    07:41:13'

@author: Lifygen

#**********************
Course Training:
--------------
http://flask.pocoo.org/docs
1. Flask - what is it?
Flask is a framework (libraries with a defined structure for working wihtin a devlopment envronment) for building web applications with Python.  Flask enables the following:
    a. Generating web pages
    b. figuring out URLs
    c. Running a web server
    d. Getting info from the user
    e. Dealing with uploading files
    f. Managing errors
    g. Saving erros and other status info about your website
    h. Working with other server applications

2. - install usng Windows command prompt commands and path update

3. - Create "Hello World" app

from flask import flask
app = Flask)__name__)

    @app.route('/')
    def hello:
        return "Hello World!"

if __name__ == '__main__':
    app.run()


# ****************
# Questions, p 240
# ****************
  1] What is the difference between a framework and an appliation?
     [Answer]:  A framework is an [general] environment with tools used to \
                create applications.  Applications are tied together in a \
                larger program.

  2] What is a view, How do you define one?
     [Answer]:  A view is a function in a Flask app that renders a web page. \
                You create one by creating a function and then adding the \
                @app.route() decorator just before the function definition.

  3] What is the function used to create HTML from a template?
     [Answer]:  Flask.render_template()

# *****************************************************************
Excercise:  Ch 20 Ex #1, p240 Revise cook's Inventory() from ch 18.
# *****************************************************************
  This Ch 20 Ex #1 excercise description:
      We have the beginning of a resturant website!  Let's add a bio page. \
      Create three biographies:  one for our ownder, the cook and the waiter. \
      Save them in a json file, where the path to the file is in /bios/.  This\
      page should display all three bios.
"""

# Ch 20 Course Training  excercise
import sqlite3
from Python_Sams19_Ex_InventorySQL3 import showInv
from flask import Flask
from flask import Flask, render_template

import sys
import os
import sqlite3
from datetime import datetime

"""
Notes:
    flask expects the html template that is fed into render_template() to be \
    in a subfolder called "template".  This folder is expected to be a \
    subfolder of the folder where your main module is located.  However, it \
    can be renamed to something else by naming the location ni the Flask() \
    call (see below):

app = Flask(__name__, template_folder='template')  # still relative to module

You can back up a level from the working directory by using "../newSubfolder"

https://stackoverflow.com/questions/23327293/flask-raises-templatenotfound-error-even-though-template-file-exists
"""
print("Open a URL and type in http://127.0.0.1:5000")

#app = Flask(__name__)
# Open flask and redirect templates from default "tempaltes" to a new
# subfolder called "FlaseTemplates"
app = Flask(__name__, template_folder='FlaskTemplates')

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/test/')
def TestPage():
    return "This is a Test Page:  http://127.0.0.1:5000/test"

@app.route('/Inventory/')
def ShowInventory():
    dbName = 'Inventory.db'
    path = "C:\\Users\\Lifygen\\projects\\python\\data\\"

    fullPathFileName = path + dbName
    conn = sqlite3.connect(fullPathFileName)

    showInventory = showInv(conn, toScreen=True, sendRet=True)
    return (showInventory)

@app.route('/<name>/')
def name_page(name):
    response = "Hello, {name}.  \n".format(name=name)
    if 'Mary Anne' in name:
        response += "You look marvelous!!!"
    return (response)
# http://127.0.0.1:5000/Mary Anne

# See Lucky.py
@app.route('/luckyNo./')
def lucky():
    # https://jinja.palletsprojects.com/en/2.11.x/
    localNbr = 3
    return render_template('Lucky.html', luckyNbr = localNbr)

# See Lucky.py
@app.route('/getLucky/')
def rnd_lucky():
    import random
    getLucky = random.randint(1, 10)
    return render_template('Lucky.html', luckyNbr = getLucky)


""" Lesson Training - Paradiase Diner
"""
from flask import Flask
from flask import Flask, render_template
import json
from datetime import datetime

#DinerApp = Flask(__name__, template_folder='FlaskTemplates')
@app.route('/diner/')
def main_page():
    #return render_template('ParadiseCafe.html', TheSpecial="Hamburger")
    #  <br />
    dailySpecial=get_special()
    Breakfast = "Breakfast:  " + dailySpecial["Breakfast"]
    Lunch = "Lunch:  " + dailySpecial["Lunch"]
    Dinner = "Dinner:  " + dailySpecial["Dinner"]

    todaysSpecial = "\\n" + Breakfast + '<br />' + Lunch + '<br \>' + Dinner

    return render_template('ParadiseCafe.html',
                           breakfast=Breakfast, lunch=Lunch, dinner=Dinner)


def get_specials(filename):
    f = open(filename)
    specials = json.load(f)
    f.close()
    return specials


def get_special():
    path = "C:\\Users\\Lifygen\\projects\\python\\data\\"
    file ="specials.json"
    fullfilepath =path + file
    specials = get_specials(fullfilepath)
    today = datetime.now()
    DAYS_OF_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                    'Saturday', 'Sunday')
    weekday = DAYS_OF_WEEK[today.weekday()]
    return specials[weekday]


"""
# *****************************************************************
Excercise:  Ch 20 Ex #1, p240 Revise cook's Inventory() from ch 18.
# *****************************************************************
  This Ch 20 Ex #1 excercise description:
      We have the beginning of a restaurant website!  Let's add a bio page. \
      Create three biographies:  one for our owner, the cook and the waiter. \
      Save them in a json file, where the path to the file is in /bios/.  This\
      page should display all three bios.
"""
# Modified such that the bios are contained in "~/FlaskTemplates/bios/".  The
# app = Flask() already assigned "FlaskTemplates" as the subfolder for templates.
# So, just add "/bios/" to the path string before adding filename when passing
# to render_template().
@app.route('/bios/')
def diner_bios():
    path = "C:\\Users\\Lifygen\\projects\\python\\FlaskTemplates\\bios\\"
    file ="DinerBios.json"
    fullFilepath = path + file

    f = open(fullFilepath)
    DinerBios = json.load(f)
    f.close()

    ownerBio = DinerBios["Owner"]["background"]
    cookBio = DinerBios["Cook"]["background"]
    waiterBio = DinerBios["Waiter"]["background"]
    bios = ownerBio + "<br />" + cookBio + "<br />" + waiterBio

    return render_template('/DinerBios.html',
                           ownerName=DinerBios["Owner"]["name"],
                           ownerBio = ownerBio,
                           cookName=DinerBios["Cook"]["name"],
                           cookBio = cookBio,
                           waiterName=DinerBios["Waiter"]["name"],
                           waiterBio = waiterBio,

                           )
    #render_template("DinerBios.html")
    #return render_template("Lucky.html", luckyNbr = 3)
    #return render_template('Lucky.html', luckyNbr = localNbr)



if __name__ == "__main__":
    # [Test #1] app "Hello" using the Flask Framework

    #DinerApp.run(debug = True)
    app.run(debug = True)

