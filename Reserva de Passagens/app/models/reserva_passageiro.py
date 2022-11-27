from app.app import db

class Reserva_passageiro(db.Model):
    id_reserva = db.Column(db.Integer, db.ForeignKey('reserva.id_reserva'), primary_key=True)
    id_passageiro = db.Column(db.Integer, db.ForeignKey('passageiro.id_passageiro'), primary_key=True)


