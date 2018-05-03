from flask import Flask, render_template, request, redirect, session
from random import randint
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 
@app.route('/')
def index():
    if 'number' not in session:
        session['wrong'] = ''
        session['box'] = ''
        session['number'] = randint(1,100)
    print(session['number'])
    return render_template("index.html", wrong = session['wrong'], boxClass = session['box'])
@app.route('/guess', methods=['POST'])
def check():
    try:
        int(request.form['guessNum'])
    except ValueError:
        session['wrong'] = 'no'
        return redirect('/')
    num = int(request.form['guessNum'])
    if num < session['number']:
        session['wrong'] = 'low'
        session['box'] = 'red'
    elif num > session['number']:
        session['wrong'] = 'high'
        session['box'] = 'red'
    elif num == session['number']:
        session['wrong'] = 'right'
        session['box'] = 'green'
    return redirect('/')
@app.route('/add', methods=['POST'])
def add():
    session['count'] +=1
    return redirect('/')
@app.route('/again', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')
@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True) 