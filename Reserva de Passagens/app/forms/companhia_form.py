from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DecimalField
from wtforms.validators import DataRequired

class CompanhiaForms(FlaskForm):
    id_companhia = IntegerField("Id Companhia", validators=[DataRequired()])
	nome = StringField("Nome", validators=[DataRequired()])
	tarifa = DecimalField("Tarifa", validators=[DataRequired()])