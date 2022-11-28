from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired

class ReservaPassageiroForm(FlaskForm):
    id_reserva = IntegerField("Id Reserva", validators=[DataRequired()])
    id_passageiro = IntegerField("Id Passageiro", validators=[DataRequired()])
