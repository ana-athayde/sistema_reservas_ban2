from sqlalchemy.dialects import postgresql

from app.app import db
from app.models import Aeronave, Modelo_Aeronave

def get_all():
    # aeronaves = []
    # for aeronaves in db.session.query(Aeronave).all():
    #     del aeronaves.__dict__['_sa_instance_state']
    #     aeronaves.append(aeronaves.__dict__)
    # return aeronaves
    return db.session.query(Aeronave.id_aeronave, Aeronave.total_assentos, Aeronave.id_modelo, \
    Modelo_Aeronave.nome, Modelo_Aeronave.max_assentos, Modelo_Aeronave.empresa, Modelo_Aeronave.capacidade_b) \
    .join(Modelo_Aeronave, Aeronave.id_modelo == Modelo_Aeronave.id_modelo, full = True) \
    .order_by(Aeronave.id_modelo, Modelo_Aeronave.id_modelo).all()


# def get_cartoes():
#     cartoes = []
#     for cartao in db.session.query(Cartao).all():
#         del cartao.__dict__['_sa_instance_state']
#         cartoes.append(cartao.__dict__)
#     return jsonify(cartoes)


def insert(**kwargs):
    ins = postgresql.insert(Aeronave).values(kwargs).on_conflict_do_update(index_elements=[Aeronave.id_aeronave], set_=kwargs)
    db.session.execute(ins)
    db.session.commit()
