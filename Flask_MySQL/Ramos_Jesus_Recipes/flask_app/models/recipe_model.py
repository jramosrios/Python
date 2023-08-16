from flask_app.config.mysqlconnection import connectToMySQL
from flask_.models import users_model
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.description = db_data['description']
        self.instructions = db_data['instructions']
        self.date_made = db_data['date_made']
        self.under_30 = db_data['under_30']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user_id = db_data['user_id']
        self.creator = None

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM recipes
        JOIN users on recipes.user_id = users.id;
        """
    results = connectToMySQL(cls.db_name).query_db(query, data)
    recipes = []
    for row_recipe in results:
        this_recipe =cls(row_recipe)
        user_data = {
                "id": row_recipe['users.id'],
                "first_name": row_recipe['first_name'],
                "last_name": row_recipe['last_name'],
                "email": row_recipe['email'],
                "password": "",
                "created_at": row_recipe['users.created_at'],
                "updated_at": row_recipe['users.updated_at']            
        }
        this_recipe.creator = user.User(user_data)
        return this_recipe
    


