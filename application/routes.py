from application import app, db
from flask import render_template, url_for, redirect, request
from application.forms import AnimalForm
import random

#dictionary of animals

animals = {"cow" : "moo", "sheep" : "baa", "cat" : "meow", "dog" : "woof"}



@app.route('/', methods=['POST', 'GET'])
def index():
    form = AnimalForm()
    if form:
        select = random.choice(list(animals))
    return render_template('index.html', title='Generate animal', form=form)



