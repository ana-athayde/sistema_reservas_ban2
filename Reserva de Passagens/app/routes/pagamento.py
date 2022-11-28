from flask import Blueprint, redirect, render_template
from app.dao import pagamento_dao, cartao_dao
from app.forms import PagamentoForm, CartaoForm
from app.notebooks.utils import remove_csrf

blue = Blueprint('pagamento', __name__, static_folder="static", template_folder="templates")

@blue.route('/pagamento', methods=['GET', 'POST'])
def pagamento():
    pagamento_form = PagamentoForm()
    if pagamento_form.validate_on_submit():
        pagamento_dao.insert(**remove_csrf(pagamento_form.data))
        return redirect('/pagamento')
    
    cartao_form = CartaoForm()
    if cartao_form.validate_on_submit():
        cartao_dao.insert(**remove_csrf(cartao_form.data))
        return redirect('/pagamento')

    rows = pagamento_dao.get_all()
    table = [dict(row) for row in rows]
    return render_template('page.html', title='Pagamento', table=table, forms=[pagamento_form, cartao_form])