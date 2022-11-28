from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DecimalField, BooleanField
from wtforms.validators import DataRequired

class PagamentoForm(FlaskForm):
    id_pagamento = IntegerField("Id Pagamento", validators=[DataRequired()])
	forma_pag = BooleanField("Forma Pagamento", validators=[DataRequired()])
	total = DecimalField("Total", validators=[DataRequired()])
	endereco_cob = StringField("Endereco Cobranca", validators=[DataRequired()])
	parcelamento = IntegerField("Parcelamento", validators=[DataRequired()])
	nome_responsavel = StringField("Nome Responsavel", validators=[DataRequired()])
	id_cartao = IntegerField("Id Cartao", validators=[DataRequired()])