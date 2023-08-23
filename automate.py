import os

diretorio = './roteiros/'

# Lista todos os arquivos e diretórios no diretório especificado
conteudo = os.listdir(diretorio)

for item in conteudo:
    item_caminho = os.path.join(diretorio, item)  # Obtém o caminho completo do item
    if os.path.isfile(item_caminho):  # Verifica se o item é um arquivo
        with open(item_caminho, 'r') as arquivo:
            print(f"Conteúdo do arquivo {item}:")
            print(arquivo.read())
            print('-' * 30)
