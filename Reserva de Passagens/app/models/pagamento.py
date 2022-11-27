from app.app import db

class Pagamento(db.Model):
	id_pagamento = db.Column(db.Integer, primary_key=True)
	forma_pag = db.Column(db.Boolean)
	total = db.Column(db.Float)
	endereco_cob = db.Column(db.String(50))
	parcelamento = db.Column(db.Integer)
	nome_responsavel = db.Column(db.String(50))
	id_cartao = db.Column(db.Integer, db.ForeignKey('cartao.id_cartao'))
