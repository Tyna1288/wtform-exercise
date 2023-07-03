
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, URL, Optional, Length, NumberRange


class AddPetForm(FlaskForm):
    """Form to add pets."""

    name = StringField(
        "Pet Name",
        validators=[InputRequired()],
    )

    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],
    )

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    age = IntegerField(
        "Age",
        validators=[Optional(), NumberRange(min=0, max=30)],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )


class EditPetForm(FlaskForm):
    """Form to edit a pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[InputRequired(), URL()],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available?")
