"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, URLField

class AddPetForm(FlaskForm):

    name = StringField('Pet Name')
    species = StringField('Pet Species')
    photo_url = URLField('URL of Pet Photo')
    age = StringField('Pet Age')
    notes = StringField('Notes')