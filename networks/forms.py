# project/networks/forms.py
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired


class AllocateIP(FlaskForm):

    allocate_ip = SelectField(validators=[DataRequired()], coerce=int)
    submit = SubmitField(
        'Allocate IP'
    )

