from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired

class DestinoForm(FlaskForm):
    id_destino = IntegerField("Id Destino", validators=[DataRequired()])
    id_aeroporto = IntegerField("Id Aeroporto", validators=[DataRequired()])