from flask import Flask, render_template
from controller.imagemController import imgTreinoController
from controller.reconhecimentoController import reconhecimentoController

app = Flask(__name__)

# Registrando o Controller com as rotas
app.register_blueprint(imgTreinoController, url_prefix='/img-treino')

# Registrando o Controller com as rotas
app.register_blueprint(reconhecimentoController, url_prefix='/reconhecimento')

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota Painel Estudante
@app.route('/painel')
def exibir_painel():
    return render_template('painel.html')

# Rota Painel Estudante
@app.route('/reconhecimento')
def reconhecimento():
    return render_template('reconhecimento.html')

# Rota pra Cadastrar novas Imagens
@app.route('/img-treino')
def guardar_nova_imagem():
    return render_template('img-treino.html', carregando = True)

if __name__ == "__main__":
    app.run(debug=True)
