import speech
import utils.folder

def generate_audio(file="", path="C:/github", lessonId=0):
    identy=0    
    texto=""
    bra=""
    eng=""
    
    with open(file, 'r') as arquivo:
        for linha in arquivo:
            for i in linha:
                if(i=="|"): 
                    eng=texto
                    texto=""

                if(i=="@"): 
                    bra=texto
                    texto=""

                if(i!="|" and i!="@" and i!="\n"): 
                    texto=texto+str(i)

            if(utils.folder.diretory_exists(path=path,create=True)):
                identy = speech.text_to_speech(textPort=bra, textEng=eng, filename=path, identy=identy, lessonId=lessonId)
    
    return True