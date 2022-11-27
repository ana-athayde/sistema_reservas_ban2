from app.app import db

class Aeronave(db.Model):
	id_aeronave = db.Column(db.Integer, primary_key=True)
	total_assentos = db.Column(db.Integer)
	id_modelo = db.Column(db.Integer, db.ForeignKey('modelo_aeronave.id_modelo'))

