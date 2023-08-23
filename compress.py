from glob import glob
from pydub import AudioSegment
from pydub.generators import WhiteNoise
from math import *
from random import *
import sys
from gtts import gTTS
from unidecode import unidecode
import os

directory = "C:/github/ai-movie-py/files" 
finalSong = AudioSegment.from_file("C:/Users/shust/Music/bemvindo.mp3")

list = os.listdir(directory)
countFiles = len(list)
i=0
longSound = False

# Percorre os arquivos no diretório
while i<countFiles:
    fullPath = directory + "/" +str(i)+ ".mp3"
    
    if os.path.isfile(fullPath):  # Verifica se é um arquivo (não diretório)
        print("Caminho completo:", fullPath)
        print("Tamanho:", os.path.getsize(fullPath), "bytes")
        print("-" * 40)

        audio1 = AudioSegment.from_mp3(fullPath)
        if(longSound):
            audio2 = AudioSegment.from_file("C:/Users/shust/Music/2seg.m4a")
            longSound = False
        else:
            audio2 = AudioSegment.from_file("C:/Users/shust/Music/1seg.m4a")
            longSound = True

        finalSong = finalSong + audio1 + audio2
        i+=1

# Salve o arquivo final
finalSong.export("C:/Users/shust/Music/aula02modulo1.mp3", format="mp3")
