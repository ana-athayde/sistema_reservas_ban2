from app.app import db	
	
class Cidade(db.Model):
	id_cidade = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(50))
	cod_cidade = db.Column(db.String(10))
	id_pais = db.Column(db.Integer, db.ForeignKey('pais.id_pais'))

