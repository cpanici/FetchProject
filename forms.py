from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PyramidForm(FlaskForm):
	word = StringField('Input a word to check:', validators=[DataRequired()])
	submit = SubmitField('Submit')