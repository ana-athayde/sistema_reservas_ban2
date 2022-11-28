from flask import Blueprint, redirect, render_template
from app.dao import cidade_dao, pais_dao
from app.forms  import CidadeForm, PaisForm
from app.notebooks.utils import remove_csrf

blue = Blueprint('cidade', __name__, static_folder="static", template_folder="templates")

@blue.route('/cidade', methods=['GET', 'POST'])
def cidade():
    cidade_form = CidadeForm()
    if cidade_form.validate_on_submit():
        cidade_dao.insert(**remove_csrf(cidade_form.data))
        return redirect('/cidade')
    
    pais_form = PaisForm()
    if pais_form.validate_on_submit():
        pais_dao.insert(**remove_csrf(pais_form.data))
        return redirect('/cidade')

    rows = cidade_dao.get_all()
    table = [dict(row) for row in rows]
    return render_template('page.html', title='Cidade', table=table, forms=[cidade_form, pais_form])