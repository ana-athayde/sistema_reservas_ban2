from app.app import db

class Companhia(db.Model):
	id_companhia = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(50))
	tarifa = db.Column(db.Float)
	