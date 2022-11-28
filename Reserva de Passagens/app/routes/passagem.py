from flask import Blueprint, redirect, render_template
from app.dao import passagem_dao, companhia_dao
from app.forms  import PassagemForm, CompanhiaForms
from app.notebooks.utils import remove_csrf

blue = Blueprint('passagem', __name__, static_folder="static", template_folder="templates")

@blue.route('/passagem', methods=['GET', 'POST'])
def passagem():
    passagem_form = PassagemForm()
    if passagem_form.validate_on_submit():
        passagem_dao.insert(**remove_csrf(passagem_form.data))
        return redirect('/passagem')
    
    companhia_form = CompanhiaForms()
    if companhia_form.validate_on_submit():
        companhia_dao.insert(**remove_csrf(companhia_form.data))
        return redirect('/passagem')

    rows = passagem_dao.get_all()
    table = [dict(row) for row in rows]
    return render_template('page.html', title='Passagem', table=table, forms=[passagem_form, companhia_form])
