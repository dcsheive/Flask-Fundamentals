from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    import datetime
    now = datetime.datetime.now()
    straw = request.form['strawberry']
    rasp = request.form['raspberry']
    apple = request.form['apple']
    first = request.form['first_name']
    last = request.form['last_name']
    stud = request.form['student_id']
    items = int(straw) + int(rasp) + int(apple)
    return render_template("checkout.html",straw = straw, rasp = rasp, apple = apple, first = first, last = last, stud = stud, items = items, now = now)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    