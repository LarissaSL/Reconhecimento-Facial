from flask import Blueprint, Response, render_template, jsonify
import cv2
import os
from datetime import datetime
import re  # Importa o módulo 're' para expressões regulares

# Criando o Blueprint para a rota '/reconhecimento'
reconhecimentoController = Blueprint('reconhecimentoController', __name__)

# Inicializando o classificador e reconhecedor
classificadorFace = "classificadorLBPHYale.yml"
detectorFace = cv2.CascadeClassifier("./cascades/haarcascade_frontalface_default.xml")
reconhecedor = cv2.face.LBPHFaceRecognizer.create()
reconhecedor.read(classificadorFace)
largura, altura = 220, 220
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
camera = cv2.VideoCapture(0)

# Armazenar informações em uma lista
informacoes = []

def gerar_frames():
    global informacoes  # Usar a lista global para armazenar informações
    while True:
        conectado, imagem = camera.read()
        if not conectado:
            break
        imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        facesDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(30, 30))
        
        for (x, y, l, a) in facesDetectadas:
            imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
            cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
            id, confianca = reconhecedor.predict(imagemFace)
            nome = "Desconhecido"
            if id == 123456:
                nome = 'Larissa'
            elif id == 13713:
                nome = 'Wesley'
            else:
                nome = 'Ninguem'

            cv2.putText(imagem, nome, (x, y + (a + 30)), font, 2, (0, 0, 255))
            cv2.putText(imagem, str(confianca), (x, y + (a + 50)), font, 1, (0, 0, 255))

            # Adiciona informações à lista se a confiança for menor que 90%
            if confianca < 90:
                informacoes.append(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - Nome: {nome}, Confiança: {confianca}')

        # Codifica a imagem para o formato JPEG
        _, jpeg = cv2.imencode('.jpg', imagem)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

@reconhecimentoController.route('/', methods=['GET'])
def reconhecimento():
    return render_template('reconhecimento.html')

@reconhecimentoController.route('/video_feed')
def video_feed():
    return Response(gerar_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@reconhecimentoController.route('/get_informacoes')
def get_informacoes():
    confianca_baixa = False
    ultima_informacao = None
    
    if informacoes:  # Verifica se há informações registradas
        ultima_informacao = informacoes[-1]  # Pega o último item da lista
        
        # Verifica a confiança da última informação
        match = re.search(r"Confiança: (\d+\.?\d*)", ultima_informacao)
        if match:
            confianca = float(match.group(1))  # Converte o valor de confiança para float
            if confianca < 90:
                confianca_baixa = True
    
    return jsonify({
        'ultima_informacao': ultima_informacao,  # Retorna apenas a última informação
        'confianca_baixa': confianca_baixa
    })


@reconhecimentoController.route('/painel')
def painel():
    return render_template('painel.html', informacoes=informacoes)
