from flask import Flask, render_template, request, redirect, flash, session
import re
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def index():
    if 'first_name' not in session:
        session['first_name'] = ""
    if 'last_name' not in session:
        session['last_name'] = ""
    if 'email' not in session:
        session['email'] = ""
    return render_template("index.html", name1 = session['first_name'], name2 = session['last_name'], email = session['email'])
@app.route('/result', methods=['POST']
)
def create_user():
    email = request.form['email']
    first = request.form['first_name']
    last = request.form['last_name']
    passw = request.form['password']
    passc = request.form['passcom']
    if email or first or last:
        session['email'] = email
        session['first_name'] = first
        session['last_name'] = last
    if len(email) < 1 or len(first) < 1 or len(last) <1 or len(passw)<1 or len(passc)<1:
        flash("Please fill in all fields") 
        return redirect('/')
    elif not EMAIL_REGEX.match(email):
        flash("Invalid Email Address!")
        session['email'] = ''
        return redirect('/')
    elif passw != passc:
        flash("Passwords must match!")
        return redirect('/')
    elif len(passw) < 8:
        flash("Passwords must be 8 or more characters!")
        return redirect('/')
    elif not first.isalpha(): 
        session['first_name'] = ''
        flash("Name must not contain numbers!")
        return redirect('/')
    elif not last.isalpha():
        session['last_name'] = ''
        flash("Name must not contain numbers!")
        return redirect('/')
    else:
        flash("Thanks for submitting your information.")
        session['first_name'] = ''
        session['email'] = ''
        session['last_name'] = ''
        return redirect('/')
@app.route('/danger')
def alert():
    print("a user tried to visit /danger.  we have redirected the user to /")
    return redirect('/')
@app.route('/back')
def back():
    session.clear()
    return redirect('/')
if __name__=="__main__":
    # run our server
    app.run(debug=True) 