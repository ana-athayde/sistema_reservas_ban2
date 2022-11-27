from app.app import db

class Passagem(db.Model):
	id_passagem = db.Column(db.Integer, primary_key=True)
	preco = db.Column(db.Float)
	no_assentos = db.Column(db.Integer)
	id_companhia = db.Column(db.Integer, db.ForeignKey('companhia.id_companhia'))
	
