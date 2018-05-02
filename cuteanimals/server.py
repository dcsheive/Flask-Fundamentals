from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    y = []
    for i in range(0,10):
        y.append(str(i+1))
    return render_template("index.html", num = y)
# @app.route('/<x>')
# def numOfImages(x):
#     y = []
#     for i in range(0,int(x)):
#         y.append(str(i+1))
#     return render_template("index.html", num = y)
@app.route('/danger')
def alert():
    print("user accessed danger page")
    return redirect('/')
@app.route('/<x>')
def random(x):
    from random import shuffle
    y = []
    for i in range(0,int(x)):
        y.append(str(i+1))
    shuffle(y)
    return render_template("index.html", num = y)
if __name__=="__main__":
    app.run(debug=True)