from flask import render_template
from app import app


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index2.html')
def about():
    return render_template('index2.html')


@app.route('/blog/fastest-men-in-the-world.html')
def blog1():
    return render_template('blog1.html')


@app.route('/blog/steph.html')
def blog2():
    return render_template('steph.html')

@app.route('/blog/strava.html')
def strava():
    return render_template('strava.html')
