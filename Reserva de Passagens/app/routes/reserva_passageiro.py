from flask import Blueprint, redirect, render_template
from app.dao import reserva_dao, passageiro_dao, reserva_passageiro_dao
from app.forms import ReservaForm, PassageiroForm
from app.notebooks.utils import remove_csrf

blue = Blueprint('reserva_passageiro', __name__, static_folder="static", template_folder="templates")


@blue.route('/reserva_passageiro', methods=['GET', 'POST'])
def reserva_passageiro():
    reserva_form = ReservaForm()
    if reserva_form.validate_on_submit():
        reserva_dao.insert(**remove_csrf(reserva_form.data))
        return redirect('/reserva_passageiro')

    passageiro_form = PassageiroForm()
    if passageiro_form.validate_on_submit():
        passageiro_dao.insert(**remove_csrf(passageiro_form.data))
        return redirect('/reserva_passageiro')

    rows = reserva_passageiro_dao.get_all()
    table = [dict(row) for row in rows]
    return render_template('page.html', title='ReservaPassageiro', table=table,
                           forms=[reserva_form, passageiro_form])
