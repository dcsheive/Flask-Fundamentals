from flask import Flask, render_template, request, redirect, session
from random import randint
import datetime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 
@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['string']=[]
    return render_template("index.html", gold = session['gold'])
@app.route('/process', methods = ['POST'])
def process():
    now = datetime.datetime.now()
    if request.form['action'] == 'farm':
        x= randint(10,20)
        session['gold'] += x
        session['string'].insert(0,['Earned '+str(x)+' gold from the farm!'+now.strftime(" (%Y-%m-%d %H:%M)"),'green'])
    elif request.form['action'] == 'cave':
        x= randint(5,10)
        session['gold'] += x
        session['string'].insert(0,['Earned '+str(x)+' gold from the cave!'+now.strftime(" (%Y-%m-%d %H:%M)"),'green'])
    elif request.form['action'] == 'house':
        x= randint(2,5)
        session['gold'] += x
        session['string'].insert(0,['Earned '+str(x)+' gold from the house!'+now.strftime(" (%Y-%m-%d %H:%M)"),'green'])
    elif request.form['action'] == 'casino':
        x= randint(0,50)
        y= randint(0,2)
        if y == 0:
            session['gold'] += x
            session['string'].insert(0,['Won '+str(x)+' gold at the casino!'+now.strftime(" (%Y-%m-%d %H:%M)"),'green'])
        else:
            session['gold'] -= x
            session['string'].insert(0,['Lost '+str(x)+' gold at the casino!'+now.strftime(" (%Y-%m-%d %H:%M)"),'red'])
    return redirect('/')
@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True) 