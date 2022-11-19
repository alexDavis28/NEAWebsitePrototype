from app import app
from app.forms import RecommenderForm
from flask import render_template, redirect, session


@app.route('/', methods=["GET", "POST"])
def index():
    form = RecommenderForm()
    if form.validate_on_submit():
        data = {
            "Ingredient": form.ingredients.data,
            "Diet": form.diet.data,
            "MaxTime": form.max_time.data,
            "MealType": form.meal_type.data
        }
        session["recommenderFormData"] = data
        return redirect("/recommend")
    return render_template("index.html", form=form)


@app.route("/recommend")
def recommend():
    return session["recommenderFormData"]