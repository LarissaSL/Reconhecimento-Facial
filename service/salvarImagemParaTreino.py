import cv2
import os
import time

# Função para salvar imagem de treino
def salvar_imagem_de_treino(id, amostra='aluno'):
    l, a = 220, 220
    # Carregar o classificador de rosto Haar
    classificadorFace = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

    # Inicializar a captura de vídeo
    cap = cv2.VideoCapture(0)

    # Adicione um delay para abrir a câmera
    time.sleep(2)

    # Diretório para salvar as imagens capturadas
    diretorio = "imagensTreino/"
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    caminho_imagem = None

    while True:
        conectado, frame = cap.read()
        if not conectado:
            print("Erro ao capturar o vídeo.")
            break

        # Converter o frame para escala de cinza
        frameCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar rostos na imagem usando o classificador Haar
        facesDetectadas = classificadorFace.detectMultiScale(frameCinza, scaleFactor=1.2, minNeighbors=8,
                                                            minSize=(30, 30))

        # Desenhar retângulos ao redor das faces detectadas
        for (x, y, w, h) in facesDetectadas:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Verificar se algum rosto foi detectado e exibir a mensagem se não houver
        if len(facesDetectadas) == 0:
            cv2.putText(frame, "Nenhum rosto detectado! Mexa a camera.", (100, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Exibir o frame com a detecção de rostos
        cv2.imshow("frame", frame)

        # Captura do pressionamento da tecla
        key = cv2.waitKey(1)

        if key == 13 or key == 32:  # Esc ou Espaço para capturar
            if len(facesDetectadas) == 0: 
                # Se não houver rostos detectados, exibir a mensagem
                print("Nenhum rosto detectado")
            elif len(facesDetectadas) == 1:  # Se detectar exatamente 1 rosto
                x, y, w, h = facesDetectadas[0]
                imagemFace = cv2.resize(frameCinza[y:y + h, x:x + w], (l, a))

                # Definir o caminho da imagem a ser salva
                caminho_imagem = os.path.join(diretorio, f"codigo{id}.{amostra}.jpg")

                # Salvar a imagem no diretório
                cv2.imwrite(caminho_imagem, imagemFace)
                print("[foto capturada com sucesso]")
                print(imagemFace.shape)

                break

        elif key == 27:  # Tecla 'R' para cancelar qualquer coisa alteramos isso 
            print("Captura cancelada!")
            caminho_imagem = None
            break

    # Finaliza a captura e fecha a janela
    cap.release()
    cv2.destroyAllWindows()

    return caminho_imagem