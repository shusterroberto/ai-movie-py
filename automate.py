import os
import process
import compress

#def automate_roteiros(diretorio="diretorio",files="gerados",modulo=""):
files = "C:/Users/shust/OneDrive/Inglês Conversação/Modulo 01/gerados/"
diretorio = "C:/Users/shust/OneDrive/Inglês Conversação/Modulo 01/Roteiro/"
modulo = "C:/Users/shust/OneDrive/Inglês Conversação/Modulo 01/"
conteudo = os.listdir(diretorio)

for item in conteudo:
    print(item)
    item_caminho = os.path.join(diretorio, item)
    if os.path.isfile(item_caminho):
        lessonId = item[4:6]
        with open(item_caminho, 'r') as arquivo:            
            process.generate_audio(file=item_caminho, path=files, lessonId=lessonId)
            compress.finalize(inputs_dir=files,output=modulo+item.replace(".txt",".mp3"))