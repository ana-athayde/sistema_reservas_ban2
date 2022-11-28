from flask import Blueprint, redirect, render_template
from app.dao import origem_dao, aeroporto_dao
from app.forms  import OrigemForm, AeroportoForm
from app.notebooks.utils import remove_csrf

blue = Blueprint('origem', __name__, static_folder="static", template_folder="templates")

@blue.route('/origem', methods=['GET', 'POST'])
def origem():
    origem_form = OrigemForm()
    if origem_form.validate_on_submit():
        origem_dao.insert(**remove_csrf(origem_form.data))
        return redirect('/origem')
    
    aeroporto_form = AeroportoForm()
    if aeroporto_form.validate_on_submit():
        aeroporto_dao.insert(**remove_csrf(aeroporto_form.data))
        return redirect('/origem')

    rows = origem_dao.get_all()
    table = [dict(row) for row in rows]
    return render_template('page.html', title='Origem', table=table, forms=[origem_form, aeroporto_form])
