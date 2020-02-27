# Third-library imports

from flask_wtf import FlaskForm
from wtforms import DecimalField, RadioField, SubmitField
from wtforms.validators import DataRequired

class SubmissionForm(FlaskForm):
	first = DecimalField('First number:', validators=[DataRequired()])
	second = DecimalField('Second number:', validators=[DataRequired()])

	operations = RadioField('',  choices=[('addition', 'Add'), ('subtraction', 'Subtract'), ('multiplication', 'Multiply'), ('division','Divide')],  validators=[DataRequired()])

	submit = SubmitField('Submit')