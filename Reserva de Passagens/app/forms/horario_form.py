from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.fields import DateField
from wtforms_components import TimeField
from wtforms.validators import DataRequired

class HorarioForm(FlaskForm):
	id_horario = IntegerField("Id Horario", validators=[DataRequired()])
	data_partida = DateField("Data Partida", validators=[DataRequired()])
	hora_partida = TimeField("Hora Partida", validators=[DataRequired()])
	data_chegada = DateField("Data Chegada", validators=[DataRequired()])
	hora_chegada = TimeField("Hora Chegada", validators=[DataRequired()])