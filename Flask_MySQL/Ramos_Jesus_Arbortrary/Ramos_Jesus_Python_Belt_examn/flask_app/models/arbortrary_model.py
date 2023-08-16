from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model
from flask import flash

class Arbortrary:
    db_name = "arbortrary_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.species = data["species"]
        self.location = data["location"]
        self.reason = data["reason"]
        self.date_planted = data["date_planted"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user = None

    @classmethod
    def add_tree(cls, data):
        query = """
        INSERT INTO arbortrary
        (species, location, reason, date_planted, user_id)
        VALUES (%(species)s, %(location)s, %(reason)s, %(date_planted)s, %(user_id)s)
        """
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_one_tree(cls, data):
        query = """
        SELECT * FROM arbortrary
        JOIN users
        ON arbortrary.user_id = users.id
        WHERE arbortrary.id = %(id)s;
        """
        results =connectToMySQL(cls.db_name).query_db(query, data)
        tree_dict = results[0]
        new_tree = cls(tree_dict)
        new_user_dic = {
                "id": tree_dict["users.id"],
                "first_name": tree_dict["first_name"],
                "last_name": tree_dict["last_name"],
                "email": tree_dict["email"],
                "password": "",
                "created_at": tree_dict["users.created_at"],
                "updated_at": tree_dict["users.updated_at"]
            }
        user_obj = user_model.User(new_user_dic)
        new_tree.user = user_obj
        return new_tree

    @classmethod
    def get_all_trees_with_users(cls):
        query = """
        SELECT * FROM arbortrary
        JOIN users
        ON arbortrary.user_id = users.id;
        """
        results = connectToMySQL(cls.db_name).query_db(query)
        arbortrary_obj_list = []
        for each_arbortrary_dict in results:
            new_arbortrary_obj = cls(each_arbortrary_dict)
            new_user_dic = {
                "id": each_arbortrary_dict["users.id"],
                "first_name": each_arbortrary_dict["first_name"],
                "last_name": each_arbortrary_dict["last_name"],
                "email": each_arbortrary_dict["email"],
                "password": "",
                "created_at": each_arbortrary_dict["users.created_at"],
                "updated_at": each_arbortrary_dict["users.updated_at"]
            }
            new_user_obj = user_model.User(new_user_dic)
            new_arbortrary_obj.user = new_user_obj
            arbortrary_obj_list.append(new_arbortrary_obj)
        return arbortrary_obj_list

    @classmethod
    def edit_tree(cls, data):
        query = """
        UPDATE arbortrary
        SET
        species = %(species)s,
        location = %(location)s,
        reason = %(reason)s,
        date_planted = %(date_planted)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete_arbortrary(cls, data):
        query = """
        DELETE FROM arbortrary WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_arbortrary(form_data):
        is_valid = True
        if len(form_data["species"]) < 5:
            is_valid = False
            flash("Species min of 5 characters")
        if len(form_data["location"]) < 5:
            is_valid = False
            flash("Location min of 2 characters")
        if len(form_data["reason"]) < 50:
            is_valid = False
            flash("Reason max 50 characters")
        if form_data["date_planted"] == "":
            is_valid = False
            flash("Date Planted must be included")
        return is_valid