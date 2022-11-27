from app.app import db

class Modelo_aeronave(db.Model):
	id_modelo = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(50))
	max_assentos = db.Column(db.Integer)
	empresa = db.Column(db.String(50))
	capacidade_b = db.Column(db.Float)