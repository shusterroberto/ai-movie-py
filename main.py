from gtts import gTTS
import os

identy=0

def text_to_speech(textPort, textEng, filename='output.mp3', id=0, play=False):
    global identy
    tts = gTTS(text='Diga: '+textPort, lang='pt', slow=False)
    tts.save(filename+str(identy)+textPort+'.mp3')

    tts = gTTS(text=textEng, lang='en', slow=False)
    tts.save(filename+str(identy)+textEng+'.mp3')

    identy=identy+1

    if(play):
        os.system(f"start {filename}")  # Reproduzir o áudio gerado

# Módulo 1 do ingles conversacao
modulo="modulo01"
path="C:/Users/shust/Music/" + modulo + "/" 

#I am happy to join with you today in what will go down in history as the greatest demonstration 
#for freedom in the history of our nation.
id=0

text_to_speech(textPort="Eu estou feliz", textEng="I am happy", filename=path, id=id+1)
text_to_speech(textPort="Eu estou feliz com você", textEng="I am happy for you", filename=path, id=id+1)
text_to_speech(textPort="Juntar-se", textEng="To join", filename=path, id=id+1)
text_to_speech(textPort="Juntar-se a você", textEng="Join you", filename=path, id=id+1)
text_to_speech(textPort="Para se juntar a você agora", textEng="To join you now", filename=path, id=id+1)
text_to_speech(textPort="Para se juntar aos vencedores", textEng="To join the winners", filename=path, id=id+1)
text_to_speech(textPort="Para se juntar a você hoje", textEng="To join with you today", filename=path, id=id+1)
text_to_speech(textPort="O que", textEng="What", filename=path, id=id+1)
text_to_speech(textPort="Vai", textEng="Will", filename=path, id=id+1)
text_to_speech(textPort="História", textEng="History", filename=path, id=id+1)
text_to_speech(textPort="Na história", textEng="In history", filename=path, id=id+1)
text_to_speech(textPort="Vai ficar na história", textEng="Will go down in history", filename=path, id=id+1)
text_to_speech(textPort="Demonstração", textEng="Demonstration", filename=path, id=id+1)
text_to_speech(textPort="O melhor", textEng="The greatest", filename=path, id=id+1)
text_to_speech(textPort="A maior demonstração", textEng="The greatest demonstration", filename=path, id=id+1)
text_to_speech(textPort="Liberdade", textEng="Freedom", filename=path, id=id+1)
text_to_speech(textPort="Pela liberdade", textEng="For freedom", filename=path, id=id+1)
text_to_speech(textPort="Na história", textEng="In the history", filename=path, id=id+1)
text_to_speech(textPort="Pela liberdade na história", textEng="For freedom in the history", filename=path, id=id+1)
text_to_speech(textPort="Nação", textEng="Nation", filename=path, id=id+1)
text_to_speech(textPort="Nossa", textEng="Our", filename=path, id=id+1)
text_to_speech(textPort="Nossa nação", textEng="Our nation", filename=path, id=id+1)
text_to_speech(textPort="A história da nossa nação", textEng="The history of our nation", filename=path, id=id+1)

text_to_speech(textPort="Estou feliz por me juntar a vocês hoje no que ficará na história como a maior manifestação pela liberdade na história de nossa nação", 
               textEng="I am happy to join with you today in what will go down in history as the greatest demonstration for freedom in the history of our nation", 
               filename=path, id=id+1)
