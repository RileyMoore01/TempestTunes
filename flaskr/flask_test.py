from cgitb import html
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home(): 
    testData = request.args
    return "<h1>Hello World this is a test to fetch values on this webpage</h1>"

@app.route('/login')
def about():


    return render_template("views/index.html")

if __name__ == "__main__":
    app.run(debug=True)