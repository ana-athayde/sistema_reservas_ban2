from flask_wtf import FlaskForm
from wtforms import IntegerField, BooleanField
from wtforms.fields import DateField
from wtforms.validators import DataRequired


class ReservaForm(FlaskForm):
    id_reserva = IntegerField("Id Reserva", validators=[DataRequired()])
    prazo_validade = DateField("Prazo Validade", validators=[DataRequired()])
    quantidade = IntegerField("Quantidade", validators=[DataRequired()])
    emitido = BooleanField("Emitido", validators=[DataRequired()])
    bagagem = BooleanField("Bagagem", validators=[DataRequired()])
    id_pag = IntegerField("Id Pagamento", validators=[DataRequired()])
    id_passagem = IntegerField("Id Passagem", validators=[DataRequired()])
