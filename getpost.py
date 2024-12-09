## Integrating HTML files in framework

from flask import Flask, render_template  ## this new render is used to redirect to the html page
'''It creates an instance of the flask class, which will be your WSGI'''
## WSGI Application
app = Flask(__name__, root_path = 'c:/Users/admin/OneDrive/Desktop/machine-learning-nlp-bootcamp_LearningMaterial/Flask')

@app.route("/") ## Route of home page
def welcome():
    return "<html><H1>welcome to the flask course</H1></html>" 
     ## if you change this message then to get it modify you need to restart the server.

@app.route("/index", methods = ['GET']) ## Route of home page
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods = ['GET','POST'])
def form_page():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route('/submit', methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug = True)
