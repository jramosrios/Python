from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def person():
    return render_template('user.html')

@app.route('/submit', methods=['POST'])
def submit():
    session['name'] = request.form['name']
    session['location'] = request.form.get('location')
    session['language'] = request.form.get('language')
    session['comment'] = request.form.get('comment')
    print(request.form)
    return redirect('/result')

@app.route('/goback', methods=['POST'])
def goback():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True, host='localhost', port = 5001)