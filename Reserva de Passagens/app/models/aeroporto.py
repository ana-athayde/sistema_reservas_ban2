from app.app import db

class Aeroporto(db.Model):
	id_aeroporto = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(50))
	id_cidade = db.Column(db.Integer, db.ForeignKey('cidade.id_cidade'))
	