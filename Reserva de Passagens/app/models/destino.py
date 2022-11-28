from app.app import db

class Destino(db.Model):
	id_destino = db.Column(db.Integer, primary_key=True)
	id_aeroporto = db.Column(db.Integer, db.ForeignKey('aeroporto.id_aeroporto'))