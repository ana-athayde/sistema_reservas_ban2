from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired

class AeronaveForm(FlaskForm):
    id_aeronave = IntegerField("Id Aeronave", validators=[DataRequired()])
    total_assentos = IntegerField("Total de Assentos", validators=[DataRequired()])
    id_modelo = IntegerFiels("Id Modelo", validators=[DataRequired()])
