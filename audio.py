from gtts import gTTS
import os

def text_to_speech(text, lang='en', filename='output.mp3', play=False):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(filename)
    if(play):
        os.system(f"start {filename}")  # Reproduzir o áudio gerado

# Módulo 1 do ingles conversacao
modulo="modulo01"
path="C:/Users/shust/Music/" + modulo + "/" 

texto = "Olá! Seja bem vindo ao módulo 1 do curso de inglês conversação."
text_to_speech(texto, lang='pt', filename=path+'bemvindo.mp3')

texto = "Repita comigo em inglês o que vem a seguir."
text_to_speech(texto, lang='pt', filename=path+'repitacomigo.mp3')

texto = "Diga: Eu estou feliz."
text_to_speech(texto, lang='pt', filename=path+'EstouFeliz.mp3')

texto = "I am happy."
text_to_speech(texto, lang='en', filename=path+'IamHappy.mp3', play=True)