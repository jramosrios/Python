from flask import render_template, redirect, session, request
from flask_app import app, bcrypt
from flask_app.models import users_model, users_model

@app.route('/')
def reg_page():
    return render_template('index.html')

@app.route('/recipes')
def recipes():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    return render_template('recipes.html', this_user = users_model.User.get_userid(data))

@app.route('/register', methods=['POST'])
def register_user():
    if not users_model.User.validate_reg(request.form):
        return redirect('/')
    new_user_data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    session['user_id'] = users_model.User.register_user(new_user_data)
    return redirect('/recipes')
    


@app.route('/login', methods=['POST'])
def login_user():
    if not users_model.User.validate_login(request.form):
        return redirect('/')
    email_data = {
        "email": request.form["email"]
    }
    found_user = users_model.User.get_user_email(email_data)
    session["user_id"] = found_user.id
    return redirect('/recipes')

@app.route('/logout')
def logout_user():
    session.clear()
    return redirect('/')