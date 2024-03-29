"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditForm
from models import connect_db, db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def display_homepage():
    pets = Pet.query.all()

    return render_template('pet_list.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():

    form = AddPetForm()

    if form.validate_on_submit():
        new_pet = Pet(
            name = form.name.data,
            species = form.species.data,
            photo_url = form.photo_url.data,
            age = form.age.data,
            notes = form.notes.data)

        db.session.add(new_pet)
        db.session.commit()

        flash(f'{form.name.data} added to pet list!')
        # This is the get that occurs after the post
        return redirect('/')

    else:
        return render_template('new_pet_form.html', form=form)

@app.route('/<pet_id>', methods=['GET', 'POST'])
def edit_form(pet_id):
    current_pet = Pet.query.get_or_404(pet_id)
    form = EditForm(obj = current_pet)

    if form.validate_on_submit():
        current_pet.photo_url = form.photo_url.data
        current_pet.notes = form.notes.data
        current_pet.available = form.available.data
        db.session.commit()

        flash(f'{form.name.data} successfully edited!')
        # This is the get that occurs after the post
        return redirect('/')
    else:
        return render_template('edit_pet_form.html', pet_id=pet_id, form=form)
