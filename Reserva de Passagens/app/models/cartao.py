from app.app import db

class Cartao(db.Model):
    id_cartao = db.Column(db.Integer, primary_quey=True)
    no_cartao = db.Column(db.String(16))
    cod_seguranca = db.Column(db.String(3))
    nome_proprietario = db.Column(db.String(50))
    bandeira = db.Column(db.String(50))
    data_vencimento = db.Column(db.Date)

    def __init__(self, no_cartao, cod_seguranca, nome_proprietario, bandeira, data_vencimento):
        self.no_cartao = no_cartao
        self.cod_seguranca = cod_seguranca
        self.nome_proprietario = nome_proprietario
        self.bandeira = bandeira
        self.data_vencimento = data_vencimento