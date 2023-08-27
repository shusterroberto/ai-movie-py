import os
import process
import compress

diretorio = 'C:/Users/shust/OneDrive/Inglês Conversação/Modulo 01/Roteiro/'
files = 'C:/Users/shust/OneDrive/Inglês Conversação/Modulo 01/gerados'
gerados = 'C:/Users/shust/OneDrive/Inglês Conversação/Modulo 01/'

# Lista todos os arquivos e diretórios no diretório especificado
conteudo = os.listdir(diretorio)

for item in conteudo:
    print(item)
    item_caminho = os.path.join(diretorio, item)  # Obtém o caminho completo do item
    if os.path.isfile(item_caminho):  # Verifica se o item é um arquivo
        with open(item_caminho, 'r') as arquivo:            
            process.generate_audio(file=item_caminho, path=files)
            compress.finalize(inputs_dir=files,output=gerados+item.replace(".txt",".mp3"))