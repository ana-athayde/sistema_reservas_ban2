from app.app import db

class Pais(db.Model):
	id_pais = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(50))
	cod_pais = db.Column(db.String(10))

