from flask import Flask, render_template

class Person:
  def __init__(self, name, email):
    self.name = name
    self.email = email

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    username = 'Peto Velky'
    array = [1,4,5,8]
    userObject = Person(username, "peto.velky@gmail.com")
    return render_template('welcome.html', username = username, array = array, userObject = userObject)

if __name__ == "__main__":
    app.run(debug=True)


