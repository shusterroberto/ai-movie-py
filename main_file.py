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

def filter(str = ""):
    for x in range(len(characters)):
        str = str.replace(characters[x],"")

    str = str.replace("cAa","ce")
    str = str.replace("E aA","E ai")
    str = str.replace("APSo","ao")
    str = str.replace("ASS","ç")
    str = str.replace("A(c)","e")
    str = str.replace("tA","ta")
    str = str.replace("A(c)","e")
    str = str.replace("APS","a")
    str = str.replace("hA","ha")

    return str

def text_to_speech(textPort, textEng, filename='output.mp3', play=False):
    global identy
    tts = gTTS(text='Diga: '+textPort, lang='pt', slow=False)
    tts.save(filename+str(identy)+filter(textPort)+'.mp3')
    arquivos.add(filter(textPort)+'.mp3')

    tts = gTTS(text=textEng, lang='en', slow=False)
    tts.save(filename+str(identy)+filter(textEng)+'.mp3')
    arquivos.add(filter(textEng)+'.mp3')

    identy=identy+1

    if(play):
        os.system(f"start {filename}")  # Reproduzir o áudio gerado

#text_to_speech(textPort="Eu estou feliz", textEng="I am happy", filename=path, id=id+1)
modulo="modulo01"
path="C:/Users/shust/Music/" + modulo + "/" 
texto=""
bra=""
eng=""
id=0

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

        text_to_speech(textPort=unidecode(bra), textEng=unidecode(eng), filename=path)


print(arquivos)