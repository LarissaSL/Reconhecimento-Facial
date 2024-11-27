from flask import Blueprint, redirect, url_for, render_template, request, flash, Flask
from service.salvarImagemParaTreino import salvar_imagem_de_treino
from service.gerarCodigoUnico import gerar_identificador_unico

# Criando o Blueprint para a rota '/img-treino' (Basicamente agrupando todas essas funções)
imgTreinoController = Blueprint('imgTreinoController', __name__)

# Rota para Registrar uma nova IMG no sistema
@imgTreinoController.route('/guardar', methods=['GET'])
def guardar_nova_imagem():
    id = gerar_identificador_unico()

    # Salvar a imagem
    caminho_imagem = salvar_imagem_de_treino(id)
    print(caminho_imagem)

    # Redireciona para a página com feedback de sucesso
    return redirect(url_for('imgTreinoController.feedback', id=id, caminho_imagem = caminho_imagem, carregando = 'false'))

# Rota para exibir informações sobre novas imagens
@imgTreinoController.route('/feedback', methods=['GET'])
def feedback():
    carregando = request.args.get('carregando')
    id = request.args.get('id')
    caminho_imagem = request.args.get('caminho_imagem')
    return render_template('img-treino.html', id = id, caminho_imagem = caminho_imagem, carregando = carregando)
