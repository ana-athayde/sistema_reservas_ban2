from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

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

db.create_all()

#singlei cartao
@app.route('/cartoes/<id>', methods='GET')
def get_cartoes(id):
    cartao = Cartao.query.get(id)
    del cartao.__dict__['_sa_instance_state']
    return jsonify(cartao.__dict__)


#get all the cartoes
@app.route('/cartoes', methods='GET')
def get_cartoes():
    cartoes = []
    for cartao in db.session.query(Cartao).all():
        del cartao.__dict__['_sa_instance_state']
        cartoes.append(cartao.__dict__)
    return jsonify(cartoes)

#create a new cartao
@app.route('/cartoes', methods='POST')
def create_cartao():
    body = request.get_json()
    db.session.add(Cartao(body['no_cartao'], body['cod_seguranca'], body['nome_proprietario'], body['bandeira'], body['data_vencimento']))
    db.session.commit()
    return "cartao criado"

#update an existing cartao
@app.route('/cartoes/<id>', methods='PUT')
def update_cartao(id):
    body = request.get_json()
    db.session.query(Cartao).filter_by(id_cartao = id).update(
        dict(no_cartao = body['no_cartao'], cod_seguranca = body['cod_seguranca'], nome_proprietario = body['nome_proprietario'], bandeira = body['bandeira'], data_vencimento = body['data_vencimento'])
    )
    db.session.commit()
    return "cartao atualizado"

#to delete cartao
@app.route('/cartoes/<id>', methods=['DELETE'])
def delete_cartao(id):
    db.session.query(Cartao).filter_by(id_cartao = id).delete()
    db.session.commit()
    return "cartao deletado"



if __name__ == '__main__':
    app.run(debug=True)