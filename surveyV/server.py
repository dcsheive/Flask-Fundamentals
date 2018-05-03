from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    if 'comment' not in session:
        session['comment'] = ""
    if 'thename' not in session:
        session['thename'] = ""
    return render_template("index.html", comm = session['comment'], nom = session['thename'])
@app.route('/result', methods=['POST'])
def create_user():
    if len(request.form['thename']) < 1:
        flash("Name cannot be empty!") 
        session['comment'] = request.form['comment']
        return redirect('/')
    if len(request.form['comment']) < 1:
        flash("Comment cannot be empty!") 
        session['thename'] = request.form['thename']
        return redirect('/')        
    if len(request.form['comment']) >120:
        session['comment'] = request.form['comment']
        session['thename'] = request.form['thename']        
        flash("Comment cannot be longer than 120 characters")
        return redirect('/')
    session['thename'] = request.form['thename']
    session['sel1'] = request.form['sel1']
    session['sel2'] = request.form['sel2']
    session['comment'] = request.form['comment']
    return render_template('indexresult.html', thename = session['thename'], sel1 = session['sel1'], sel2= session['sel2'], comment = session['comment'])
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