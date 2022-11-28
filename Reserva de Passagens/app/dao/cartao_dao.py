from sqlalchemy.dialects import postgresql

from app.app import db
from app.models import Cartao


def insert(**kwargs):
    ins = postgresql.insert(Cartao).values(kwargs).on_conflict_do_update(index_elements=[Cartao.id_cartao], set_=kwargs)
    db.session.execute(ins)
    db.session.commit()
