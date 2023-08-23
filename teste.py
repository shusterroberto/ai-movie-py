from glob import glob
from pydub import AudioSegment
from pydub.generators import WhiteNoise
from math import *
from random import *
import sys
from gtts import gTTS
from unidecode import unidecode
import os

identy=0
characters = ".'!?Ã;¡ê"
arquivos = {"1seg.mp3"}

def text_to_speech(textPort, textEng, filename='output.mp3'):
    global identy

    if(textPort[-1]=='?'):
        textPortComplete='Pergunte: '+textPort
    else:
        textPortComplete='Diga: '+textPort

    bSlow=(textPort[0]=='-')

    if(bSlow):
        textPortComplete=textPort.replace('-','')

    tts = gTTS(text=textPortComplete, lang='pt', slow=False)
    tts.save(filename+str(identy)+'.mp3')
    arquivos.add(str(identy)+'.mp3')
    identy+=1

    tts = gTTS(text=textEng, lang='en', slow=bSlow)
    tts.save(filename+str(identy)+'.mp3')
    arquivos.add(str(identy)+'.mp3')
    identy+=1
    print(f"{textPort} : {textEng}")

#text_to_speech(textPort="Eu estou feliz", textEng="I am happy", filename=path, id=id+1)
modulo="modulo01"
path="C:/github/ai-movie-py/files/" 
texto=""
bra=""
eng=""

# Abre o arquivo em modo de leitura
with open('C:/github/ai-movie-py/aula02modulo01.txt', 'r') as arquivo:
    for linha in arquivo:
        for i in linha:
            if(i=="|"): 
                eng=texto
                texto=""

            if(i=="@"): 
                bra=texto
                texto=""

            if(i!="|" and i!="@" and i!="\n"): 
                texto=texto+i

        text_to_speech(textPort=bra, textEng=eng, filename=path)