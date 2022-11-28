from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, BooleanField
from wtforms.validators import DataRequired

class PassageiroForm(FlaskForm):
	id_passageiro = IntegerField("Id Passageiro", validators=[DataRequired()])
	nome = StringField("Nome", validators=[DataRequired()])
	assistencia = BooleanField("Assistencia", validators=[DataRequired()])
	rg = StringField("RG", validators=[DataRequired()])
	cpf = StringField("CPF", validators=[DataRequired()])
	crianca = BooleanField("Crianca", validators=[DataRequired()])
	email = StringField("Email", validators=[DataRequired()])
	endereco = StringField("Endereco", validators=[DataRequired()])
	telefone = StringField("Telefone", validators=[DataRequired()])
