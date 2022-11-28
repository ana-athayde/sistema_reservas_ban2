from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired

class CidadeForm(FlaskForm):
    id_cidade = IntegerField("Id Cidade", validators=[DataRequired()])
	nome = StringField("Noma", validators=[DataRequired()])
	cod_cidade = StringField("Codigo Cidade", validators=[DataRequired()])
	id_pais = IntegerField("Id Pais", validators=[DataRequired()])
