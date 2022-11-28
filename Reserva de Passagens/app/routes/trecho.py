from flask import Blueprint, redirect, render_template
from app.dao import trecho_dao, horario_dao, passagem_dao, aeronave_dao, origem_dao, destino_dao
from app.forms  import TrechoForm, HorarioForm, PassagemForm, AeronaveForm, OrigemForm, DestinoForm
from app.notebooks.utils import remove_csrf

blue = Blueprint('trecho', __name__, static_folder="static", template_folder="templates")

@blue.route('/trecho', methods=['GET', 'POST'])
def trecho():
    trecho_form = TrechoForm()
    if trecho_form.validate_on_submit():
        trecho_dao.insert(**remove_csrf(trecho_form.data))
        return redirect('/trecho')
    
    horario_form = HorarioForm()
    if horario_form.validate_on_submit():
        horario_dao.insert(**remove_csrf(horario_form.data))
        return redirect('/trecho')

    passagem_form = PassagemForm()
    if passagem_form.validate_on_submit():
        passagem_dao.insert(**remove_csrf(passagem_form.data))
        return redirect('/trecho')

    aeronave_form = AeronaveForm()
    if aeronave_form.validate_on_submit():
        aeronave_dao.insert(**remove_csrf(aeronave_form.data))
        return redirect('/trecho')

    origem_form = OrigemForm()
    if origem_form.validate_on_submit():
        origem_dao.insert(**remove_csrf(origem_form.data))
        return redirect('/trecho')

    destino_form = DestinoForm()
    if destino_form.validate_on_submit():
        destino_dao.insert(**remove_csrf(destino_form.data))
        return redirect('/trecho')

    rows = passagem_dao.get_all()
    table = [dict(row) for row in rows]
    return render_template('page.html', title='Trecho', table=table, forms=[trecho_form, horario_form, passagem_form, aeronave_form, origem_form, destino_form])