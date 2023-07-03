"""Pet Adoption application."""

from flask import Flask, render_template, redirect, flash, url_for, jsonify
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234567@localhost:5433/adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "abc123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)
with app.app_context():
    connect_db(app)
    db.create_all()

#########################################################################################


@app.route('/')
def show_pets():
    """Shows list of pets"""

    pets = Pet.query.all()
    return render_template('list.html', pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_newPet():
    """Add a new pet in a form"""

    form = AddPetForm()


    if form.validate_on_submit():
       data = {k: v for k, v in form.data.items() if k != "csrf_token"}
       new_pet = Pet(**data)
    #    new_pet = Pet(name = form.name.data, species = form.species.data, age = form.age.data,photo_url = form.photo_url.data, notes = form.notes.data, available = form.available.data)
       db.session.add(new_pet)
       db.session.commit()
       flash(f"{new_pet.name} added.")
       return redirect(url_for('list_pets'))

    else:
        return render_template("add_form.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet form."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect(url_for('list_pets'))

    else:
        return render_template("edit_form.html", form=form, pet=pet)


@app.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
    """Return basic info about pet in JSON."""

    pet = Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "age": pet.age, "species": pet.species}

    return jsonify(info)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
