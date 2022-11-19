from app import app
from app.forms import RecommenderForm
from flask import render_template


@app.route('/')
def index():
    form = RecommenderForm()
    return render_template("index.html", form=form)
