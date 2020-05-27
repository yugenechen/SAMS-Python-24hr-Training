"""Python_Sams20, p 221, Developing for the Web with Flask \
# Ch 20 Course Training  excercise

print("Open a URL and type in http://127.0.0.1:5000")

"""
import os
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def lucky():
    #    return render_template("C:/Users/Lifygen/projects/python/FlaskTemplates/Lucky.html", message="Hello Flask!")
    return render_template("Lucky.html")

if __name__ == "__main__":
    app.run( debug=True)