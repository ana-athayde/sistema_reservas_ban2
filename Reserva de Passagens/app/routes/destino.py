from flask import Blueprint, redirect, render_template
from app.dao import destino_dao, aeroporto_dao
from app.forms import DestinoForm, AeroportoForm
from app.notebooks.utils import remove_csrf

blue = Blueprint('destino', __name__, static_folder="static", template_folder="templates")

@blue.route('/destino', methods=['GET', 'POST'])
def destino():
    destino_form = DestinoForm()
    if destino_form.validate_on_submit():
        destino_dao.insert(**remove_csrf(destino_form.data))
        return redirect('/destino')

    aeroporto_form = AeroportoForm()
    if aeroporto_form.validate_on_submit():
        aeroporto_dao.insert(**remove_csrf(aeroporto_form.data))
        return redirect('/destino')

    rows = destino_dao.get_all()
    table = [dict(row) for row in rows]
    return render_template('page.html', title='Destino', table=table, forms=[destino_form, aeroporto_form])
