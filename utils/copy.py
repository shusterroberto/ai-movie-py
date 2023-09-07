import os
import shutil
import utils.clear as clear

def backup(diretorio='./files/', output=''):
    if(os.path.isdir(output)==False):
        os.mkdir(output)
    else:
        clear.clear_folder()

    shutil.move(diretorio,output)
    print("Arquivos movidos com sucesso.")
    return True

#backup(diretorio="C:/Users/shust/OneDrive/Inglês Conversação/Modulo 01/gerados", output="C:/Users/shust/OneDrive/Inglês Conversação/Modulo 01/aula01modulo01/gerados")