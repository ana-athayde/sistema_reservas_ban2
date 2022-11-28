from sqlalchemy.dialects import postgresql

from app.app import db
from app.models import Origem, Aeroporto


def get_all():
    return db.session.query(Origem.id_origem, Origem.id_aeroporto, \
    Aeroporto.id_aeroporto, Aeroporto.nome, Aeroporto.id_cidade) \
    .join(Aeroporto, Origem.id_aeroporto == Aeroporto.id_aeroporto, full = True) \
    .order_by(Origem.id_aeroporto, Aeroporto.id_aeroporto).all()

def insert(**kwargs):
    ins = postgresql.insert(Origem).values(kwargs).on_conflict_do_update(index_elements=[Origem.id_origem], set_=kwargs)
    db.session.execute(ins)
    db.session.commit()
