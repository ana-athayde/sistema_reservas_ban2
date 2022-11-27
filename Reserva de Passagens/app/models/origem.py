from app.app import db

class Origem(db.Model):
	id_origem = db.Column(db.Integer, primary_key=True)
	id_aeroporto = db.Column(db.Integer, db.ForeignKey('aeroporto.id_aeroporto'))


