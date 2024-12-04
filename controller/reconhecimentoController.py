from flask import Blueprint, Response, render_template, jsonify
import cv2
import os
from datetime import datetime
import re

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
    global informacoes  
    while True:
        conectado, imagem = camera.read()
        if not conectado:
            break
        
        imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        facesDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(30, 30))
        
        for (x, y, l, a) in facesDetectadas:
            imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
            
            cv2.rectangle(imagem, (x, y), (x + l, y + a), (128, 0, 128), 3)  
            
            id, confianca = reconhecedor.predict(imagemFace)

            # Marcar como "Desconhecido" se a confiança for menor que 10
            if confianca < 10:
                nome = "Desconhecido"
            elif id == 123456:
                nome = 'Larissa'
            elif id == 13713:
                nome = 'Wesley'
            else:
                nome = 'Ninguem'

            # Verifica a posição da face para sugerir instruções
            centro_x = x + l // 2  # Posição horizontal do centro da face
            largura_imagem = imagem.shape[1]  # Largura da imagem da câmera

            if centro_x < largura_imagem * 0.3:
                instrucoes = "Olhe para a direita"
            elif centro_x > largura_imagem * 0.7:
                instrucoes = "Olhe para a esquerda"
            else:
                instrucoes = "Fique firme e olhe para frente"

            cv2.putText(imagem, instrucoes, (x, y - 40), font, 1.5, (128, 0, 128), 3)  # Texto verde com mais espaçamento

            cv2.putText(imagem, nome, (x, y + (a + 60)), font, 2, (128, 0, 128), 3)  # Nome em amarelo, mais distante

            confianca_formatada = f"{confianca:.2f}"  # Formata a confiança com 2 casas decimais
            cv2.putText(imagem, confianca_formatada, (x, y + (a + 100)), font, 1.5, (128, 0, 128), 2)  # Confiança em ciano

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
    
    if informacoes: 
        ultima_informacao = informacoes[-1] 
        
        # Verifica a confiança da última informação
        match = re.search(r"Confiança: (\d+\.?\d*)", ultima_informacao)
        if match:
            confianca = float(match.group(1))
            if confianca < 10:
                confianca_baixa = True
    
    return jsonify({
        'ultima_informacao': ultima_informacao,  
        'confianca_baixa': confianca_baixa
    })

@reconhecimentoController.route('/painel')
def painel():
    return render_template('painel.html', informacoes=informacoes)
