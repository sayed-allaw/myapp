from flask import Flask
import os
app = Flask(__name__)
@app.route("/")
def home():
  return "Hello from Docker"
@app.route("/hello")
def hello():
  return "hello sayed"
@app.route("/about")
def about():
  name = os.getenv("NAME", "sayed")
  return f" hello {name}, i am learning docker and flask "
app.run(host="0.0.0.0", port=5000, debug=True)
