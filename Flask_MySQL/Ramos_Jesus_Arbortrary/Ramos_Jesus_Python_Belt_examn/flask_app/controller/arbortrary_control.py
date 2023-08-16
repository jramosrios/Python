from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models import arbortrary_model, user_model


@app.route("/dashboard")
def all_arbortrary():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session["user_id"]
    }
    return render_template('all_arbortrary.html', 
    logged_user = user_model.User.get_userid(data),
    all_arbortrary = arbortrary_model.Arbortrary.get_all_trees_with_users())

@app.route("/new/tree")
def new_tree():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session["user_id"]
    }
    return render_template('add_arbortrary.html', 
    logged_user = user_model.User.get_userid(data))

@app.route("/edit/<int:id>")
def edit_tree(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": id
        }
    return render_template('edit_arbortrary.html',
    this_tree = arbortrary_model.Arbortrary.get_one_tree(data))

@app.route("/show/<int:id>")
def view_tree(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session["user_id"]
    }
    data = {
        "id": id,
    }
    return render_template("view_arbortrary.html", 
    this_tree = arbortrary_model.Arbortrary.get_one_tree(data))

@app.route("/delete/<int:id>", methods=["POST"])
def delete_tree(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    arbortrary_model.Arbortrary.delete_arbortrary(data)
    return redirect('/user/account')

@app.route("/arbortrary/add_to_db", methods=["POST"])
def add_tree_to_db():
    if 'user_id' not in session:
        return redirect('/')
    if not arbortrary_model.Arbortrary.validate_arbortrary(request.form):
        return redirect("/new/tree")
    arbortrary_model.Arbortrary.add_tree(request.form)
    return redirect("/dashboard")

@app.route("/arbortrary/edit_db/<int:id>", methods=["POST"])
def edit_tree_db(id):
    if 'user_id' not in session:
        return redirect('/')
    if not arbortrary_model.Arbortrary.validate_arbortrary(request.form):
        return redirect(f'/edit/{id}')
    arbortrary_model.Arbortrary.edit_tree(request.form)
    return redirect("/dashboard")
