from flask import Flask,render_template
import random
x=Flask(__name__)

@x.route("/")
def hello():
    return render_template('index.html')
@x.route("/about")
def shiv():
    name=["Shivam Tandon","kopal Tandon","Sanjay Tandon","Jyoti Tandon"]
    return render_template('about.html',name=random.choice(name))
x.run()