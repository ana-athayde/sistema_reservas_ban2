from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DecimalField
from wtforms.validators import DataRequired

class ModeloAeronaveForm(FlaskForm):
    id_modelo = IntegerField("Id Modelo", validators=[DataRequired()])
	nome = StringField("Nome", validators=[DataRequired()])
	max_assentos = IntegerField("Maximo Assentos", validators=[DataRequired()])
	empresa = StringField("Empresa", validators=[DataRequired()])
	capacidade_b = DecimalField("Capacidade Bagageiro", validators=[DataRequired()])