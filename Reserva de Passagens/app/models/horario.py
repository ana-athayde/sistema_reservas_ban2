from app.app import db

class Horario(db.Model):
	id_horario = db.Column(db.Integer, primary_key=True)
	data_partida = db.Column(db.Date)
	hora_partida = db.Column(db.Time)
	data_chegada = db.Column(db.Date)
	hora_chegada = db.Column(db.Time)

