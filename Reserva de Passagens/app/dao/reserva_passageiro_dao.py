from sqlalchemy.dialects import postgresql

from app.app import db
from app.models import ReservaPassageiro, Reserva, Passageiro


def get_all():
    return db.session.query(ReservaPassageiro.id_reserva, ReservaPassageiro.id_passageiro,
                            Reserva.id_reserva, Reserva.prazo_validade, Reserva.quantidade, Reserva.emitido,
                            Reserva.bagagem, Reserva.id_pag, Reserva.id_passagem,
                            Passageiro.id_passageiro, Passageiro.nome, Passageiro.assistencia, Passageiro.rg,
                            Passageiro.cpf,
                            Passageiro.crianca, Passageiro.email, Passageiro.endereco, Passageiro.telefone) \
        .join(Reserva, ReservaPassageiro.id_reserva == Reserva.id_reserva, full=True) \
        .join(Passageiro, ReservaPassageiro.id_passageiro == Passageiro.id_passageiro, full=True) \
        .order_by(ReservaPassageiro.id_reserva, Reserva.id_reserva).all()
    # mesma duvida que reserva_dao .. este order by ficou sem Passageiro .. nao sei se e um problema ou nao


def insert(**kwargs):
    ins = postgresql.insert(ReservaPassageiro).values(kwargs).on_conflict_do_update(
        index_elements=[ReservaPassageiro.id_reserva, ReservaPassageiro.id_passageiro], set_=kwargs)
    db.session.execute(ins)
    db.session.commit()
