from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/result', methods=['POST'])
def create_user():
    thename = request.form['thename']
    sel1 = request.form['sel1']
    sel2 = request.form['sel2']
    comment = request.form['comment']
    return render_template('indexresult.html', thename = thename, sel1 = sel1, sel2= sel2, comment = comment)
@app.route('/danger')
def alert():
    print("a user tried to visit /danger.  we have redirected the user to /")
    return redirect('/')
if __name__=="__main__":
    # run our server
    app.run(debug=True) 