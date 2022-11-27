from app.app import db

class Reserva(db.Model()):
	id_reserva = db.Column(db.Integer, primary_key=True)
	prazo_validade = db.Column(db.Date)
	quantidade = db.Column(db.Integer)
	emitido = db.Column(db.Boolean)
	bagagem = db.Column(db.Boolean)
	id_pag = db.Column(db.Integer, db.ForeignKey('pagamento.id_pagamento'))
	id_passagem = db.Column(db.Integer, db.ForeignKey('passagem.id_passagem'))

