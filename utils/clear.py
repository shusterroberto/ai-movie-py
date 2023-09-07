import os
import shutil

def clear_folder(diretorio='./files/', output=''):
    arquivos = os.listdir(diretorio)
    if(os.path.isdir(output)):
        shutil.rmtree(output)
    
    os.mkdir(output)

    for arquivo in arquivos:
        caminho_arquivo = os.path.join(diretorio, arquivo)
        if os.path.isfile(caminho_arquivo):
            shutil.move(caminho_arquivo, output)

    print("Arquivos deletados com sucesso.")

    return True