import os

# Configurações
pasta = "./imagensTreino"

alunos_ra = {
    "larissa": "1371392222020",
    "wesley": "1371392222024"
}

# Função para renomear os arquivos
def renomear_fotos_por_ra(pasta, alunos_ra):
    try:
        # Lista todos os arquivos da pasta
        arquivos = os.listdir(pasta)
        print(f"Arquivos encontrados: {arquivos}")
        
        # Filtra apenas os arquivos com extensões de imagem
        extensoes_imagem = (".jpg", ".jpeg", ".png", ".bmp", ".gif")
        imagens = [arq for arq in arquivos if arq.lower().endswith(extensoes_imagem)]

        if not imagens:
            print("Nenhuma imagem encontrada na pasta.")
            return
        
        # Dicionário para acompanhar o número sequencial para cada aluno
        contador = {nome: 1 for nome in alunos_ra.keys()}
        
        # Renomeia as imagens
        for imagem in imagens:
            extensao = os.path.splitext(imagem)[1] 
            partes = imagem.split(".")  

            if len(partes) >= 3 and partes[1].lower() == "aluno": 
                nome = partes[2].lower().strip()
                if nome in alunos_ra:
                    ra = alunos_ra[nome]  # Obtém o RA do dicionário
                    sequencial = contador[nome]  # Obtém o número sequencial atual
                    novo_nome = f"RA.{ra}.{nome.capitalize()}.{sequencial}{extensao}"  # Formata o novo nome
                    contador[nome] += 1 
                    
                    caminho_antigo = os.path.join(pasta, imagem)
                    caminho_novo = os.path.join(pasta, novo_nome)
                    
                    # Renomear o arquivo
                    os.rename(caminho_antigo, caminho_novo)
                    print(f"Renomeado: {imagem} -> {novo_nome}")
                else:
                    print(f"Nome '{nome}' não encontrado no dicionário de RAs. Ignorando: {imagem}")
            else:
                print(f"Formato inválido de arquivo: {imagem}. Ignorando.")
        
        print("Renomeação concluída!")
    except Exception as e:
        print(f"Erro ao renomear arquivos: {e}")

# Chamada da função
renomear_fotos_por_ra(pasta, alunos_ra)
