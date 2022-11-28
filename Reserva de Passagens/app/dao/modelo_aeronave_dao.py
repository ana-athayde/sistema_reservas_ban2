from sqlalchemy.dialects import postgresql

from app.app import db
from app.models import Modelo_Aeronave


def insert(**kwargs):
    ins = postgresql.insert(Modelo_Aeronave).values(kwargs).on_conflict_do_update(index_elements=[Modelo_Aeronave.id_modelo], set_=kwargs)
    db.session.execute(ins)
    db.session.commit()
