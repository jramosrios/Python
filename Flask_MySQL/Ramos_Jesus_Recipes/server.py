from flask_app import app
from flask_app.controller import recipe_controller, users_control

if __name__=="__main__":
    app.run(debug=True, host="localhost", port=5001)