from flask_app import app
from flask import render_template, redirect, request, session
#import models
from flask_app.models import ninja, dojo

@app.route('/ninjas')
def ninja_page():
    return render_template('ninjas.html', all_dojos = dojo.Dojo.get_all_dojos())

@app.route('/ninja/add', methods=["POST"])
def add_ninja():
    ninja.Ninja.add_ninja(request.form)
    return redirect("/dojos")
