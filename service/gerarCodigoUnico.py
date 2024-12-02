import os
import re

def gerar_identificador_unico(diretorio='imagensTreino'):
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    # Arquivos do diretorio
    arquivos = os.listdir(diretorio)

    # Regex para extrair os IDs dos arquivos
    padrao = re.compile(r'^codigo(\d+)\.aluno\.[^"]*\.jpg$')

    ids_existentes = []
    for arquivo in arquivos:
        match = padrao.match(arquivo)
        if match:
            # Tenta extrair o ID de dentro das aspas, se houver
            id_str = match.group(1).strip('"')
            if id_str.isdigit():
                ids_existentes.append(int(id_str))

    # Obter o próximo identificador
    if ids_existentes:
        novo_id = max(ids_existentes) + 1
    else:
        novo_id = 1

    return str(novo_id)
