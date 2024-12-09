## Building url dynamicaly
## Variable rule
## Jinja 2 Template engine
## jinja2 template engine
'''
{{}} expresions to print output in html
{%...%} conditions, for loops
{#... #} single line comments
'''



from flask import Flask, render_template, redirect, url_for ## this new render is used to redirect to the html page
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


@app.route('/submit', methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

# Variable rule

@app.route('/success/<int:score>')   # we are restricting the parameter
def sucess(score):
    res = ""
    if score>=50:
        res-"PASSED"
    else:
        res="FAILED"
    return render_template('result.html', results = res)


# Variable rule

@app.route('/successres/<int:score>')   # we are restricting the parameter
def sucessres(score):
    res = ""
    if score>=50:
        res-"PASSED"
    else:
        res="FAILED"

    exp = {'score':score, 'res':res}
    return render_template('result1.html', results = res)

# If condition

@app.route('/successif/<int:score>')   # we are restricting the parameter
def sucessif(score):
    
    return render_template('result.html', results = res)

# Variable rule

@app.route('/fail/<int:score>')   # we are restricting the parameter
def fail(score):
    
    return render_template('result.html', results = score)

@app.route('/sumit', methods = ['POST',"GET"])   # we are restricting the parameter
def submit():

    total_score = 0
    if request.method == 'POST':
            science = float(request.form['science'])
            maths = float(request.form['maths'])

            total_score = (science+maths)/2
    return redirect(url_for('sucessres', score = total_Score))



if __name__ == "__main__":
    app.run(debug = True)
