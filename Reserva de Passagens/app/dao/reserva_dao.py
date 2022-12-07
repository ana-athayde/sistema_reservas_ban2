from sqlalchemy.dialects import postgresql

from app.app import db
from app.models import Reserva, Pagamento, Passagem


def get_all():
    return db.session.query(Reserva.id_reserva, Reserva.prazo_validade, Reserva.quantidade,
                            Reserva.emitido, Reserva.bagagem, Reserva.id_pag, Reserva.id_passagem,
                            Pagamento.id_pagamento, Pagamento.forma_pag, Pagamento.total, Pagamento.endereco_cob,
                            Pagamento.parcelamento, Pagamento.nome_responsavel, Pagamento.id_cartao,
                            Passagem.id_passagem, Passagem.preco, Passagem.no_assentos, Passagem.id_companhia) \
        .join(Pagamento, Reserva.id_pag == Pagamento.id_pagamento, full=True) \
        .join(Passagem, Reserva.id_passagem == Passagem.id_passagem, full=True) \
        .order_by(Reserva.id_pag,
                  Pagamento.id_pagamento).all()  # nao coloquei Passagem no order by nao sei como fazer ??
    # fazer outro order by? ou inlcuir no mesmo Reserva.id_passagem, Passagem.id_passagem


def insert(**kwargs):
    ins = postgresql.insert(Reserva).values(kwargs).on_conflict_do_update(index_elements=[Reserva.id_reserva],
                                                                          set_=kwargs)
    db.session.execute(ins)
    db.session.commit()
