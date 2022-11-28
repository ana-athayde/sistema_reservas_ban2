from sqlalchemy.dialects import postgresql

from app.app import db
from app.models import Aeroporto, Cidade


def get_all():
    return db.session.query(Aeroporto.id_aeroporto, Aeroporto.nome, Aeroporto.id_cidade, \
    Cidade.id_cidade, Cidade.nome, Cidade.cod_cidade, Cidade.id_pais) \
    .join(Cidade, Aeroporto.id_cidade == Cidade.id_cidade, full = True) \
    .order_by(Aeroporto.id_cidade, Cidade.id_cidade).all()

def insert(**kwargs):
    ins = postgresql.insert(Aeroporto).values(kwargs).on_conflict_do_update(index_elements=[Aeroporto.id_aeroporto], set_=kwargs)
    db.session.execute(ins)
    db.session.commit()
