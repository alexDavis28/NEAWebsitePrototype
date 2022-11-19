from flask_wtf import FlaskForm
from wtforms import StringField, FieldList, SelectField, IntegerField, SubmitField
from wtforms.validators import NumberRange


class RecommenderForm(FlaskForm):
    {{ form.hiddent_tag()}}
    ingredients = FieldList(StringField("Ingredient Name"))
    diet = SelectField("Dietary Requirements", choices=[
        ('vgn', 'Vegan'),
        ('veg', 'Vegetarian'),
        ('psc', 'Pescetarian')
    ])
    max_time = IntegerField("Maximum Cooking Time", validators=[NumberRange(min=1)])
    meal_type = StringField("Meal Type")
    submit = SubmitField("Find Recipes")
