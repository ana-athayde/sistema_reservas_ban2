from sqlalchemy.dialects import postgresql

from app.app import db
from app.models import Trecho, Horario, Passagem, Aeronave, Origem, Destino


def get_all():
    return db.session.query(Trecho.id_trecho, Trecho.classe, Trecho.assento, Trecho.id_horario, Trecho.id_passagem, \
    Trecho.id_aeronave, Trecho.id_origem, Trecho.id_destino, Horario.id_horario, Horario.data_partida, Horario.hora_partida, \
    Horario.data_chegada, Horario.hora_chegada, Passagem.id_passagem, Passagem.preco, Passagem.no_assentos, Passagem.id_companhia, \
    Aeronave.id_aeronave, Aeronave.total_assentos, Aeronave.id_modelo, Origem.id_origem, Origem.id_aeroporto, \
    Destino.id_destino, Destino.id_aeroporto) \
    .join(Horario, Trecho.id_horario == Horario.id_horario, full = True) \
    .join(Passagem, Trecho.id_passagem == Passagem.id_passagem, full = True) \
    .join(Aeronave, Trecho.id_aeronave == Aeronave.id_aeronave, full = True) \
    .join(Origem, Trecho.id_origem == Origem.id_origem, full = True) \
    .join(Destino, Trecho.id_destino == Destino.id_destino, full = True) \
    .order_by(Trecho.id_horario, Horario.id_horario).all()
    # mesma situ q reserva_dao e reserva_passageiro_dao

def insert(**kwargs):
    ins = postgresql.insert(Trecho).values(kwargs).on_conflict_do_update(index_elements=[Trecho.id_trecho], set_=kwargs)
    db.session.execute(ins)
    db.session.commit()
