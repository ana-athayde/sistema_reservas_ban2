from flask import Blueprint, redirect, render_template
from app.dao import aeronave_dao, modelo_aeronave_dao
from app.forms import AeronaveForm, ModeloAeronaveForm
from app.notebooks.utils import remove_csrf

blue = Blueprint('aeronave', __name__, static_folder="static", template_folder="templates")

@blue.route('/aeronave', methods=['GET', 'POST'])
def aeronave():
    aeronave_form = AeronaveForm()
    if aeronave_form.validate_on_submit():
        aeronave_dao.insert(**remove_csrf(aeronave_form.data))
        return redirect('/aeronave')

    modelo_aero_form = ModeloAeronaveForm()
    if modelo_aero_form.validate_on_submit():
        modelo_aeronave_dao.insert(**remove_csrf(modelo_aero_form.data))
        return redirect('/aeronave')

    rows = aeronave_dao.get_all()
    table = [dict(row) for row in rows]
    return render_template('page.html', tittle="Aeronave", table=table, forms=[aeronave_form, modelo_aero_form])