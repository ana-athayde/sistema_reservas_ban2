from sqlalchemy.dialects import postgresql

from app.app import db
from app.models import Pagamento, Cartao


def get_all():
    return db.session.query(Pagamento.id_pagamento, Pagamento.forma_pag, Pagamento.total, Pagamento.endereco_cob, \
    Pagamento.parcelamento, Pagamento.nome_responsavel, Pagamento.id_cartao, Cartao.id_cartao, Cartao.no_cartao, \
    Cartao.cod_seguranca, Cartao.nome_proprietario, Cartao.bandeira, Cartao.data_vencimento) \
    .join(Cartao, Pagamento.id_cartao == Cartao.id_cartao, full = True) \
    .order_by(Pagamento.id_cartao, Cartao.id_cartao).all()

def insert(**kwargs):
    ins = postgresql.insert(Pagamento).values(kwargs).on_conflict_do_update(index_elements=[Pagamento.id_pagamento], set_=kwargs)
    db.session.execute(ins)
    db.session.commit()

