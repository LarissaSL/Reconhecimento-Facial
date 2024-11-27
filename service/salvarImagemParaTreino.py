import cv2
import os
import time
from datetime import datetime


# Função para salvar imagem de treino
def salvar_imagem_de_treino(id, amostra='aluno'):
    l, a = 220, 220
    # Carregar o classificador de rosto Haar
    classificadorFace = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

    # Inicializar a captura de vídeo
    cap = cv2.VideoCapture(0)

    # Adicione um delay para garantir que a câmera esteja pronta
    time.sleep(2)

    # Diretório para salvar as imagens capturadas
    diretorio = "imagensTreino/"
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    caminho_imagem = None

    while True:
        conectado, frame = cap.read()
        frameCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar rostos na imagem usando o classificador Haar
        facesDetectadas = classificadorFace.detectMultiScale(frameCinza, scaleFactor=1.1, minNeighbors=5,
                                                             minSize=(30, 30))

        for (x, y, w, h) in facesDetectadas:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Exibir o frame com as faces detectadas
        cv2.imshow("frame", frame)

        # Captura do pressionamento da tecla
        key = cv2.waitKey(1)

        if key == 27:  # Pressionar ESC para capturar a foto
            if len(facesDetectadas) == 1:  # Certifique-se de que uma face foi detectada
                x, y, w, h = facesDetectadas[0]
                imagemFace = cv2.resize(frameCinza[y:y + h, x:x + w], (l, a))

                caminho_imagem = os.path.join(diretorio, f"codigo{id}.{amostra}.jpg")

                # Salvar a imagem no diretório
                cv2.imwrite(caminho_imagem, imagemFace)
                print("[ foto capturada com sucesso ]")
                print(imagemFace.shape)

                break

    cap.release()
    cv2.destroyAllWindows()

    return caminho_imagem
