from sqlalchemy.dialects import postgresql

from app.app import db
from app.models import Destino, Aeroporto


def get_all():
    return db.session.query(Destino.id_destino, Destino.id_aeroporto, \
    Aeroporto.id_aeroporto, Aeroporto.nome, Aeroporto.id_cidade) \
    .join(Aeroporto, Destino.id_aeroporto == Aeroporto.id_aeroporto, full = True) \
    .order_by(Destino.id_aeroporto, Aeroporto.id_aeroporto).all()

def insert(**kwargs):
    ins = postgresql.insert(Destino).values(kwargs).on_conflict_do_update(index_elements=[Destino.id_destino], set_=kwargs)
    db.session.execute(ins)
    db.session.commit()
