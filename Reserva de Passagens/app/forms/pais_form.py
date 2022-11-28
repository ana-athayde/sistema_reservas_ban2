from flask_wtf import FlaskForm	
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired
    
class PaisForm(FlaskForm): 
	id_pais = IntegerField("Id Pais", validators=[DataRequired()])
	nome = StringField("Nome", validators=[DataRequired()])
	cod_pais = StringField("Codigo Pais", validators=[DataRequired()])