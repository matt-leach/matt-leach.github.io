from flask import render_template
from app import app


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/blog/fastest-men-in-the-world.html')
def about():
    return render_template('blog1.html')
