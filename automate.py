import os
import process
import compress

def automate_roteiros(diretorio="diretorio",files="gerados",modulo=""):
    conteudo = os.listdir(diretorio)

    for item in conteudo:
        print(item)
        item_caminho = os.path.join(diretorio, item)  # Obtém o caminho completo do item
        if os.path.isfile(item_caminho):  # Verifica se o item é um arquivo
            with open(item_caminho, 'r') as arquivo:            
                process.generate_audio(file=item_caminho, path=files)
                compress.finalize(inputs_dir=files,output=modulo+item.replace(".txt",".mp3"))