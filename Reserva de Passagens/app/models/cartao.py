from app.app import db

class Cartao(db.Model):
    id_cartao = db.Column(db.Integer, primary_key=True)
    no_cartao = db.Column(db.String(16))
    cod_seguranca = db.Column(db.String(3))
    nome_proprietario = db.Column(db.String(50))
    bandeira = db.Column(db.String(50))
    data_vencimento = db.Column(db.Date)
