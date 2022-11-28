from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired

class TrechoForm(FlaskForm):
	id_trecho = IntegerField("Id Trecho", validators=[DataRequired()])
	classe = StringField("Classe", validators=[DataRequired()])
	assento = StringField("Assento", validators=[DataRequired()])
	id_horario = IntegerField("Id Horario", validators=[DataRequired()])
	id_passagem = IntegerField("Id Passagem", validators=[DataRequired()])
	id_aeronave = IntegerField("Id Aeronave", validators=[DataRequired()])
	id_origem = IntegerField("Id Origem", validators=[DataRequired()])
	id_destino = IntegerField("Id Destino", validators=[DataRequired()])