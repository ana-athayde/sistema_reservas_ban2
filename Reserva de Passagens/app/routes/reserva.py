from flask import Blueprint, redirect, render_template
from app.dao import reserva_dao, pagamento_dao, passagem_dao
from app.forms import ReservaForm, PagamentoForm, PassagemForm
from app.notebooks.utils import remove_csrf

blue = Blueprint('reserva', __name__, static_folder="static", template_folder="templates")


@blue.route('/reserva', methods=['GET', 'POST'])
def reserva():
    reserva_form = ReservaForm()
    if reserva_form.validate_on_submit():
        reserva_dao.insert(**remove_csrf(reserva_form.data))
        return redirect('/reserva')

    pagamento_form = PagamentoForm()
    if pagamento_form.validate_on_submit():
        pagamento_dao.insert(**remove_csrf(pagamento_form.data))
        return redirect('/reserva')

    passagem_form = PassagemForm()
    if passagem_form.validate_on_submit():
        passagem_dao.insert(**remove_csrf(passagem_form.data))
        return redirect('/reserva')

    rows = passagem_dao.get_all()
    table = [dict(row) for row in rows]
    return render_template('page.html', title='Reserva', table=table,
                           forms=[reserva_form, pagamento_form, passagem_form])
