from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World Welcome to my first app!"

@app.route('/product/<name>')
def get_product(name):
  return "The product is " + str(name)
