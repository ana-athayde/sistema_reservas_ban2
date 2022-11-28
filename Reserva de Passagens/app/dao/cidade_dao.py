from sqlalchemy.dialects import postgresql

from app.app import db
from app.models import Cidade, Pais


def get_all():
    return db.session.query(Cidade.id_cidade, Cidade.nome, Cidade.cod_cidade, Cidade.id_pais, \
    Pais.id_pais, Pais.nome, Pais.cod_pais) \
    .join(Pais, Cidade.id_pais == Pais.id_pais, full = True) \
    .order_by(Cidade.id_pais, Pais.id_pais).all()

def insert(**kwargs):
    ins = postgresql.insert(Cidade).values(kwargs).on_conflict_do_update(index_elements=[Cidade.id_cidade], set_=kwargs)
    db.session.execute(ins)
    db.session.commit()
