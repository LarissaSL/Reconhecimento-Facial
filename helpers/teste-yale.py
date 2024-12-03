import cv2
import os
import numpy as np
from PIL import Image

detectorFace = cv2.CascadeClassifier("./cascades/haarcascade_frontalface_default.xml")
reconhecedor = cv2.face.LBPHFaceRecognizer.create()
reconhecedor.read("classificadorLBPHYale.yml")

totalAcertos = 0
percentualAcerto = 0.0
totalConfianca = 0.0

# Caminhos das imagens
caminhos = [os.path.join('./Fotos_Praticas', f) for f in os.listdir('./Fotos_Praticas')]

for caminhoImagem in caminhos:
    imagemFace = Image.open(caminhoImagem).convert('L')
    imagemFaceNP = np.array(imagemFace, 'uint8')
    facesDetectadas = detectorFace.detectMultiScale(imagemFaceNP)
    for (x, y, l, a) in facesDetectadas:
        idprevisto, confianca = reconhecedor.predict(imagemFaceNP)
        
        # Extrai o ID atual do nome do arquivo
        nome_arquivo = os.path.split(caminhoImagem)[1] 
        partes = nome_arquivo.split(".")  # Divide o nome pelo "."
        
        if len(partes) >= 4 and partes[0] == "RA":
            idatual = int(partes[1])  # O RA está na segunda parte
            
            print(f"{idatual} foi classificado como {idprevisto} - {confianca}")
            
            if idprevisto == idatual:
                totalAcertos += 1
                totalConfianca += confianca

# Calcular o percentual de acertos com base no número de arquivos na pasta
percentualAcerto = (totalAcertos / len(caminhos)) * 100 if len(caminhos) > 0 else 0
totalConfianca = totalConfianca / totalAcertos if totalAcertos > 0 else 0

print(f"Percentual de acerto: {percentualAcerto:.2f}%")
print(f"Total confiança: {totalConfianca:.2f}")
