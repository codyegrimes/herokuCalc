from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    startingSR = IntegerField('startingSR', validators=[DataRequired()])
    targetSR = IntegerField('targetSR', validators=[DataRequired()])