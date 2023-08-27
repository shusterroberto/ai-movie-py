import os

def diretory_exists(path="", create=True):
    exists = os.path.exists(path) 
    
    if(create and not exists):
        os.mkdir(path)
        exists=True

    return exists

#testeok = diretory_exists(path="C:/Users/shust/OneDrive/Inglês Conversação/Modulo 01/gerados",create=True) 