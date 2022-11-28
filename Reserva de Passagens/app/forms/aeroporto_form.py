from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired

class AeroportoForm(FlaskForm):
    id_aeroporto = IntegerField("Id Aeroporto", validators=[DataRequired()])
    nome = StringField("Nome", validators=[DataRequired()])
    id_cidade = IntegerField("Id Cidade", validators=[DataRequired()])
