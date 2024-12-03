import cv2
import os
import numpy as np
from PIL import Image

# Inicializando os reconhecedores
eigenface = cv2.face.EigenFaceRecognizer_create(40, 8000)
fisherface = cv2.face.FisherFaceRecognizer_create(3, 2000)
lbph = cv2.face.LBPHFaceRecognizer_create(2, 2, 7, 7, 50)

def getImagemComId():
    # Caminhos das imagens
    caminhos = [os.path.join('./Fotos_Treino', f) for f in os.listdir('./Fotos_Treino') if os.path.isfile(os.path.join('./Fotos_Treino', f))]
    faces = []
    ids = []

    for caminhoImagem in caminhos:
        try:
            # Abre a imagem e a converte para escala de cinza
            imagemFace = Image.open(caminhoImagem).convert('L')
            imagemNP = np.array(imagemFace, 'uint8')
            
            # Extrai informações do nome do arquivo
            nome_arquivo = os.path.split(caminhoImagem)[1]  # Ex.: RA_12345_Larissa_2.jpg
            partes = nome_arquivo.split(".")  # Divide por "." -> ["RA", "12345", "Larissa", "2.jpg"]
            
            if len(partes) >= 4 and partes[0] == "RA":
                ra = int(partes[1])  
                print(f"Processando imagem: {nome_arquivo} com RA: {ra}")  # Exibe o RA no terminal
                ids.append(ra)
                faces.append(imagemNP)
            else:
                print(f"Formato de arquivo inválido ignorado: {nome_arquivo}")
        except Exception as e:
            print(f"Erro ao processar arquivo {caminhoImagem}: {e}")
    
    return np.array(ids), faces


# Chama a função para pegar os IDs e as faces
ids, faces = getImagemComId()

# Inicia o treinamento
print("Treinando...")
eigenface.train(faces, ids)
eigenface.write('classificadorEigenYale.yml')

fisherface.train(faces, ids)
fisherface.write('classificadorFisherYale.yml')

lbph.train(faces, ids)
lbph.write('classificadorLBPHYale.yml')

print("Treinamento realizado")
