from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.fields import DateField
from wtforms.validators import DataRequired

class CartaoForm(FlaskForm):
    id_cartao = IntegerField("Id Cartao", validators=[DataRequired()])
    no_cartao = StringField("Numero Cartao", validators=[DataRequired()])
    cod_seguranca = StringField("Codigo Seguranca", validators=[DataRequired()])
    nome_proprietario = StringField("Nome Proprietario", validators=[DataRequired()])
    bandeira = StringField("Bandeira", validators=[DataRequired()])
    data_vencimento = DateField("Data de Vencimento", validators=[DataRequired()])