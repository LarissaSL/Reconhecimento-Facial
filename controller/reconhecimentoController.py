# Criando o Blueprint para a rota '/reconhecimento' (Basicamente agrupando todas essas funções)
from flask import Blueprint,  render_template

reconhecimentoController = Blueprint('reconhecimentoController', __name__)

# Rota para Registrar uma nova IMG no sistema
@reconhecimentoController.route('/', methods=['GET'])
def reconhecimento():
    return render_template('reconhecimento.html')