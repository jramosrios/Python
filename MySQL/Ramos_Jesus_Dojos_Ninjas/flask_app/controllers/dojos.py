from flask_app import app
from flask import render_template, redirect, request, session
#import models
from flask_app.models import dojo, ninja

@app.route('/')
def root():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template('dojos.html', all_dojos = dojo.Dojo.get_all_dojos())

@app.route('/add/new', methods=['POST'])
def add_dojo():
    dojo.Dojo.add_dojo(request.form) #Dojo with upper case refers to the class method in the model file
    return redirect("/")

@app.route('/dojo/<int:id>')
def view_dojo(id):
    data = {
        "id": id,
    }
    return render_template("view_dojo.html", one_dojo = dojo.Dojo.get_one_dojo(data))


