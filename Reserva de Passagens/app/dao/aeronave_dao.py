from sqlalchemy.dialects import postgresql

from app.app import db
from app.models import Aeronave, Modelo_Aeronave

def get_all():
    return db.session.query(Aeronave.id_aeronave, Aeronave.total_assentos, Aeronave.id_modelo, \
    Modelo_Aeronave.nome, Modelo_Aeronave.max_assentos, Modelo_Aeronave.empresa, Modelo_Aeronave.capacidade_b) \
    .join(Modelo_Aeronave, Aeronave.id_modelo == Modelo_Aeronave.id_modelo, full = True) \
    .order_by(Aeronave.id_modelo, Modelo_Aeronave.id_modelo).all()

def insert(**kwargs):
    ins = postgresql.insert(Aeronave).values(kwargs).on_conflict_do_update(index_elements=[Aeronave.id_aeronave], set_=kwargs)
    db.session.execute(ins)
    db.session.commit()