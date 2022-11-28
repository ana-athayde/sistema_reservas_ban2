from flask import Blueprint, redirect, render_template
from app.dao import aeroporto_dao, cidade_dao
from app.forms  import AeroportoForm, CidadeForm
from app.notebooks.utils import remove_csrf

blue = Blueprint('aeroporto', __name__, static_folder="static", template_folder="templates")

@blue.route('/aeroporto', methods=['GET', 'POST'])
def aeroporto():
    aeroporto_form = AeroportoForm()
    if aeroporto_form.validate_on_submit():
        aeroporto_dao.insert(**remove_csrf(aeroporto_form.data))
        return redirect('/aeroporto')
    
    cidade_form = CidadeForm()
    if cidade_form.validate_on_submit():
        cidade_dao.insert(**remove_csrf(cidade_form.data))
        return redirect('/aeroporto')

    rows = aeroporto_dao.get_all()
    table = [dict(row) for row in rows]
    return render_template('page.html', title='Aeroporto', table=table, forms=[aeroporto_form, cidade_form])