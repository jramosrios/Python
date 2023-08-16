from flask import Flask
app = Flask(__name__)

@app.route("/")
def home_route():
    return "Hello World"

@app.route("/dojo")
def dojo_route():
    return "Dojo!"

@app.route("/say/<string:name>")
def say_hi(name):
    return f"Hello {name}"

@app.route("/repeat/<int:num>/<string:word>")
def repeat(num, word):
    return f"Hello {word}" * num


if __name__ =="__main__":
    app.run(debug=True, host="localhost", port=5001)