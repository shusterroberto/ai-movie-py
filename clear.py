import os

def clear_folder(diretorio='./files/'):
    arquivos = os.listdir(diretorio)

    # Percorre a lista de arquivos e deleta cada um
    for arquivo in arquivos:
        caminho_arquivo = os.path.join(diretorio, arquivo)  # Gera o caminho completo do arquivo
        if os.path.isfile(caminho_arquivo):  # Verifica se é um arquivo (não uma pasta)
            os.remove(caminho_arquivo)  # Deleta o arquivo

    print("Arquivos deletados com sucesso.")

    return True