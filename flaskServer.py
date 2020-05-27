# -*- coding: utf-8 -*-
"""
HTML web page server example.
Utilizes index.html as a template file.

Created on Sun May 24 12:53:26 2020

@author: Lifygen

Notes:
    flask expects the html template that is fed into render_template() to be in a subfolder called "template".  This folder is expected to be a subfolder of
the folder where your main module is located.  However, it can be renamed to
something else by naming the location ni the Flask() call (see below):

app = Flask(__name__, template_folder='template')  # still relative to module

You can back up a level from the working directory by using "../"

https://stackoverflow.com/questions/23327293/flask-raises-templatenotfound-error-even-though-template-file-exists
"""

import os
from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='FlaskTemplates')

@app.route("/hello/")
def Hello():
    message="Hello Flask!"
    return (message);
    #return render_template("index.html", message="Hello Flask!");

@app.route("/")
def index():
    message="Hello Flask!"
    # myHtml ="C:\\Users\\Lifygen\\projects\\python\\index.html"
    myHtml ="index.html"
    return render_template(myHtml, message=message);

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)