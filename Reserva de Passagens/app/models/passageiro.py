from app.app import db

class Passageiro(db.Model):
	id_passageiro = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(50))
	assistencia = db.Column(db.Boolean)
	rg = db.Column(db.String(7))
	cpf = db.Column(db.String(11))
	crianca = db.Column(db.Boolean)
	email = db.Column(db.String(50))
	endereco = db.Column(db.String(50))
	telefone = db.Column(db.String(50))
