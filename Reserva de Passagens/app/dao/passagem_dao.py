from sqlalchemy.dialects import postgresql

from app.app import db
from app.models import Passagem, Companhia


def get_all():
    return db.session.query(Passagem.id_passagem, Passagem.preco, Passagem.no_assentos, Passagem.id_companhia, \
    Companhia.id_companhia, Companhia.nome, Companhia.tarifa) \
    .join(Companhia, Passagem.id_companhia == Companhia.id_companhia, full = True) \
    .order_by(Passagem.id_companhia, Companhia.id_companhia).all()

def insert(**kwargs):
    ins = postgresql.insert(Passagem).values(kwargs).on_conflict_do_update(index_elements=[Passagem.id_passagem], set_=kwargs)
    db.session.execute(ins)
    db.session.commit()
