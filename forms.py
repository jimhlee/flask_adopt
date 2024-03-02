"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, URLField, SelectField
from wtforms.validators import InputRequired, Optional, URL, ValidationError

class AddPetForm(FlaskForm):


    name = StringField(
        'Pet Name',
        validators=[InputRequired()])

    species = StringField(
        'Pet Species',
        validators=[InputRequired()])

    photo_url = URLField(
        'URL of Pet Photo',
        validators=[Optional(), URL()])

    age = SelectField(
        'Pet Age',
        choices=[
            ('baby', 'Baby'),
            ('young', 'Young'),
            ('adult', 'Adult'),
            ('senior', 'Senior')
                 ])

    notes = StringField(
        'Notes',
        validators=[InputRequired()])