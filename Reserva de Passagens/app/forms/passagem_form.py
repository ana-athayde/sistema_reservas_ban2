from flask_wtf import FlaskForm
from wtforms import IntegerField, DecimalField
from wtforms.validators import DataRequired

class PassagemForm(FlaskForm):
	id_passagem = IntegerField("Id Passagem", validators=[DataRequired()])
	preco = DecimalField("Preco", validators=[DataRequired()])
	no_assentos = IntegerField("Numero Assentos", validators=[DataRequired()])
	id_companhia = IntegerField("Id Companhia", validators=[DataRequired()])
