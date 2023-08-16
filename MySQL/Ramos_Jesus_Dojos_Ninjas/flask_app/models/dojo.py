from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    db_name = "dojo_and_ninjas_schema" #schema name

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        #link all ninjas
        self.ninjas =[]


    #Adding a dojo
    @classmethod
    def add_dojo(cls, data):
        query = """ 
        INSERT INTO dojos
        (name)
        VALUES (%(name)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        return connectToMySQL(cls.db_name).query_db(query)
        #list dojos objects
        all_dojo_objects =[]
        for each_dojo in results:
            print(each_dojo)
            #create dojo obj
            new_dojo_obj =cls()
            #adding dojo to the list
            all_dojo_objects.append(new_dojo_obj)
        return all_dojo_objects

    @classmethod
    def get_one_dojo(cls, data):
        query = """
        SELECT * from dojos
        LEFT JOIN ninjas
        ON dojos.id = ninjas.dojo_id
        WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL(cls.db_name).query_db(query, data)
        dojo_dict = results[0]
        dojo_obj = cls(dojo_dict)
        for each_ninja_dict in results:
            #create dojo obj
            ninja_info = {
                "id": each_ninja_dict['ninjas.id'], #dup column name so specify table name
                "first_name": each_ninja_dict['first_name'],
                "last_name": each_ninja_dict['last_name'],
                "age": each_ninja_dict['age'],
                "created_at": each_ninja_dict['ninjas.created_at'],
                "updated_at": each_ninja_dict['ninjas.updated_at'],
            }
            ninja_obj = ninja.Ninja(ninja_info)
            dojo_obj.ninjas.append(ninja_obj)
        return dojo_obj
        