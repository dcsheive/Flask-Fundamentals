from flask import Flask, render_template
app = Flask(__name__) 
@app.route('/')
def hello_world():
    return render_template('index.html', name = 'Jay')
@app.route('/dojo')
def dojo():
    return 'Dojo!'
@app.route('/say/<name>') 
def say(name):
    print(name)
    return "Hi "+name
@app.route('/repeat/<num>/<name>')
def repeat(num,name):
    print(name,num)
    return (name+"\n") * int(num)
    
@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

app.run(debug=True) 