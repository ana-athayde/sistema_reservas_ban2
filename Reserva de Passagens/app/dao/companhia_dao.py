from sqlalchemy.dialects import postgresql

from app.app import db
from app.models import Companhia


def insert(**kwargs):
    ins = postgresql.insert(Companhia).values(kwargs).on_conflict_do_update(index_elements=[Companhia.id_companhia], set_=kwargs)
    db.session.execute(ins)
    db.session.commit()
	