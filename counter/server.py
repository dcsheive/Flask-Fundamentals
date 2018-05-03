from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 
@app.route('/')
def index():
    if 'count'not in session:
        session['count'] = 0
    session['count'] += 1
    return render_template("index.html", count = session['count'])
@app.route('/destroy', methods=['POST'])
def destroy():
    session.clear()
    return redirect('/')
@app.route('/add', methods=['POST'])
def add():
    session['count'] +=1
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True) 