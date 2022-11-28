from sqlalchemy.dialects import postgresql

from app.app import db
from app.models import Horario


def insert(**kwargs):
    ins = postgresql.insert(Horario).values(kwargs).on_conflict_do_update(index_elements=[Horario.id_horario], set_=kwargs)
    db.session.execute(ins)
    db.session.commit()
