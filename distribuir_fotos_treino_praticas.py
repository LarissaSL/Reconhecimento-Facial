import os
import shutil
import random

# Configurações
pasta_origem = "./imagensTreino"  
pasta_treino = "./Fotos_Treino"
pasta_praticas = "./Fotos_Praticas"
proporcao_treino = 0.7  # 70% para treino
proporcao_praticas = 0.3  # 30% para práticas

# Função para separar fotos
def separar_fotos(pasta_origem, pasta_treino, pasta_praticas, proporcao_treino):
    try:
        # Lista todos os arquivos da pasta
        arquivos = os.listdir(pasta_origem)
        print(f"Arquivos encontrados: {arquivos}")
        
        # Filtra apenas os arquivos com extensões de imagem
        extensoes_imagem = (".jpg", ".jpeg", ".png", ".bmp", ".gif")
        imagens = [arq for arq in arquivos if arq.lower().endswith(extensoes_imagem)]

        if not imagens:
            print("Nenhuma imagem encontrada na pasta.")
            return

        # Embaralha os arquivos para garantir aleatoriedade
        random.shuffle(imagens)

        # Calcula a quantidade de imagens para cada grupo
        total_imagens = len(imagens)
        qtd_treino = int(total_imagens * proporcao_treino)
        qtd_praticas = total_imagens - qtd_treino

        # Separa as imagens
        treino_imagens = imagens[:qtd_treino]
        praticas_imagens = imagens[qtd_treino:]

        # Cria as pastas se não existirem
        os.makedirs(pasta_treino, exist_ok=True)
        os.makedirs(pasta_praticas, exist_ok=True)

        # Move as imagens para as pastas
        for imagem in treino_imagens:
            shutil.move(os.path.join(pasta_origem, imagem), os.path.join(pasta_treino, imagem))
            print(f"Movido para treino: {imagem}")
        
        for imagem in praticas_imagens:
            shutil.move(os.path.join(pasta_origem, imagem), os.path.join(pasta_praticas, imagem))
            print(f"Movido para práticas: {imagem}")

        print(f"Separação concluída! {qtd_treino} imagens em treino e {qtd_praticas} imagens em práticas.")
    except Exception as e:
        print(f"Erro ao separar arquivos: {e}")

# Chamada da função
separar_fotos(pasta_origem, pasta_treino, pasta_praticas, proporcao_treino)
