from sqlalchemy.dialects import postgresql

from app.app import db
from app.models import Reserva_Passageiro, Reserva, Passageiro


def get_all():
    return db.session.query(Reserva_Passageiro.id_reserva, Reserva_Passageiro.id_passageiro, \
    Reserva.id_reserva, Reserva.prazo_validade, Reserva.quantidade, Reserva.emitido, Reserva.bagagem, Reserva.id_pag, Reserva.id_passagem, \
    Passageiro.id_passageiro, Passageiro.nome, Passageiro.assistencia, Passageiro.rg, Passageiro.cpf, \
    Passageiro.crianca, Passageiro.email, Passageiro.endereco, Passageiro.telefone) \
    .join(Reserva, Reserva_Passageiro.id_reserva == Reserva.id_reserva, full = True) \
    .join(Passageiro, Reserva_Passageiro.id_passageiro == Passageiro.id_passageiro, full = True) \
    .order_by(Reserva_Passageiro.id_reserva, Reserva.id_reserva).all()
    # mesma duvida que reserva_dao .. este order by ficou sem Passageiro .. nao sei se e um problema ou nao

def insert(**kwargs):
    ins = postgresql.insert(Reserva_Passageiro).values(kwargs).on_conflict_do_update(index_elements=[Reserva_Passageiro.id_reserva, Reserva_Passageiro.id_passageiro], set_=kwargs)
    db.session.execute(ins)
    db.session.commit()

