from app.app import db

class Trecho(db.Model):
	id_trecho = db.Column(db.Integer, primary_key=True)
	classe = db.Column(db.String(50))
	assento = db.Column(db.String(3))
	id_horario = db.Column(db.Integer, db.ForeignKey('horario.id_horario'))
	id_passagem = db.Column(db.Integer, db.ForeignKey('passagem.id_passagem'))
	id_aeronave = db.Column(db.Integer, db.ForeignKey('aeronave.id_aeronave'))
	id_origem = db.Column(db.Integer, db.ForeignKey('origem.id_origem'))
	id_destino = db.Column(db.Integer, db.ForeignKey('destino.id_destino'))