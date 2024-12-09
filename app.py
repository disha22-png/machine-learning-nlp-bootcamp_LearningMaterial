from flask import Flask
'''It creates an instance of the flask class, which will be your WSGI'''
## WSGI Application
app = Flask(__name__)

@app.route("/") ## Route of home page
def welcome():
    return "Welcome to this best flask course. This is amazing course"  ## if you change this message then to get it modify you need to restart the server.

@app.route("/index") ## Route of home page
def index():
    return "Welcome to index page"



if __name__ == "__main__":
    app.run(debug = True)