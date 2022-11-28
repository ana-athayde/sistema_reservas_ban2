from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired

class OrigemForm(FlaskForm):
    id_origem = IntegerField("Id Origem", validators=[DataRequired()])
    id_aeroporto = IntegerField("Id Aeroporto", validators=[DataRequired()])