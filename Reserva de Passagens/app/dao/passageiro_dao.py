from sqlalchemy.dialects import postgresql

from app.app import db
from app.models import Passageiro


def insert(**kwargs):
    ins = postgresql.insert(Passageiro).values(kwargs).on_conflict_do_update(index_elements=[Passageiro.id_passageiro], set_=kwargs)
    db.session.execute(ins)
    db.session.commit()
