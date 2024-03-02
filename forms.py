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

    age = SelectField(
        'Pet Age',
        choices=[
            ('baby', 'Baby'),
            ('young', 'Young'),
            ('adult', 'Adult'),
            ('senior', 'Senior')
                 ])

    photo_url = URLField(
        'URL of Pet Photo',
        validators=[Optional(), URL()])

    notes = StringField(
        'Notes',
        validators=[InputRequired()])


class EditForm(FlaskForm):

    name = StringField(
        'Pet Name',
        validators=[InputRequired()])

    species = StringField(
        'Pet Species',
        validators=[InputRequired()])

    age = SelectField(
        'Pet Age',
        choices=[
            ('baby', 'Baby'),
            ('young', 'Young'),
            ('adult', 'Adult'),
            ('senior', 'Senior')
                 ])

    photo_url = URLField(
        'URL of Pet Photo',
        validators=[Optional(), URL()])

    notes = StringField(
        'Notes',
        validators=[InputRequired()])

    available = SelectField(
        'Is Pet Available?',
        validators=[InputRequired()],
        choices=[(True, 'Available'),
                 (False, 'Not Available')],
        coerce=bool
    )