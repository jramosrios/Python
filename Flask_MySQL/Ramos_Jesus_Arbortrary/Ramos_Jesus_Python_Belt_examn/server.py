from flask_app import app
from flask_app.controller import user_control, arbortrary_control


if __name__=="__main__":
    app.run(debug=True, host="localhost", port=5001)