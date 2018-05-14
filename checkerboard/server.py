from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def welcome():
    return "Welcome!"
@app.route('/<rows>/<cols>')
def play2(rows, cols):
    return render_template("index.html", rows = int(rows), cols = int(cols))
if __name__=="__main__":
    app.run(debug=True) 