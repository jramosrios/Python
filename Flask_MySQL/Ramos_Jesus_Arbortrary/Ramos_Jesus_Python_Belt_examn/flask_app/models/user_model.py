from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import arbortrary_model
from flask_app import bcrypt
#import for email specification
import re
#expression obj
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    db_name = "arbortrary_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.arbortrary = []

    @classmethod
    def register_user(cls, data):
        query = """
        INSERT INTO users
        (first_name, last_name, email, password)
        VALUES
        (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_userid(cls, data):
        query = """
        SELECT * FROM users
        WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db_name).query_db(query, data)
        this_user_obj = cls(results[0])
        return this_user_obj
    
    @classmethod
    def get_user_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) == 0:
            return None
        else:
            this_user_obj = cls(results[0])
            return this_user_obj

    @classmethod
    def get_user_trees(cls, data):
        query = """
        SELECT * FROM users
        LEFT JOIN arbortrary
        ON users.id = arbortrary.user_id
        WHERE users.id = %(id)s;
        """
        results = connectToMySQL(cls.db_name).query_db(query, data)
        user_dict = results[0]
        user_obj = cls(user_dict)
        for current_tree_dict in results:
            if current_tree_dict["arbortrary.id"] == None:
                break
            new_tree_dict = {
                "id": current_tree_dict["arbortrary.id"],
                "species": current_tree_dict["species"],
                "location": current_tree_dict["location"],
                "reason": current_tree_dict["reason"],
                "date_planted": current_tree_dict["date_planted"],
                "created_at": current_tree_dict["arbortrary.created_at"],
                "updated_at": current_tree_dict["arbortrary.updated_at"]
            }
            new_arbortrary_obj = arbortrary_model.Arbortrary(new_tree_dict)
            user_obj.arbortrary.append(new_arbortrary_obj)
        return user_obj



    @staticmethod
    def validate_reg(data):
        is_valid = True
        if len(data['first_name']) < 2:
            flash('First Name must be 2 or more characters', 'registration')

        if len(data['last_name']) < 2:
            flash('Last Name must be 2 or more characters', 'registration')

        if not EMAIL_REGEX.match(data['email']): 
            is_valid = False
            flash("Invalid email address!", 'registration')

        found_user_result = User.get_user_email({"email": data["email"]})
        if found_user_result != None:
            is_valid = False
            flash('Email already in use.', 'registration')

        if len(data['password']) < 8:
            flash('Password must be 8 or more characters', 'registration')
            
        if data['password'] != data['confirm_password']:
            is_valid = False
            flash('Password dont match', 'registration')
        return is_valid

    @staticmethod
    def validate_login(form_data):
        is_valid = True
        found_user_result = User.get_user_email({"email": form_data['email']})
        if found_user_result == None:
            is_valid = False
            flash("Incorrect credentials", 'login')
        elif not bcrypt.check_password_hash(found_user_result.password, form_data['password']):
            is_valid = None
            flash("Incorrect credentials", 'login')
        return is_valid