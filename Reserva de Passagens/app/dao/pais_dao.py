from sqlalchemy.dialects import postgresql

from app.app import db
from app.models import Pais


def insert(**kwargs):
    ins = postgresql.insert(Pais).values(kwargs).on_conflict_do_update(index_elements=[Pais.id_pais], set_=kwargs)
    db.session.execute(ins)
    db.session.commit()
