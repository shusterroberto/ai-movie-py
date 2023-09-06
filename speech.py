import audios.interations
import utils.text
import utils.export
import utils.folder
from gtts import gTTS

def text_to_speech(textPort, textEng, filename='C:/Audios/', identy=0):
    textPortComplete = audios.interations.text_interation(textPortuguese=textPort)
    utils.folder.diretory_exists(path=filename+"/words",create=True)
    
    tts = gTTS(text=textPortComplete, lang='pt', slow=False)
    pathPt = f"{filename}/{str(identy)}.mp3"
    tts.save(pathPt)
    identy+=1

    tts = gTTS(text=textEng, lang='en', slow=True)
    textEng = utils.text.clear_text(textEng)
    pathEn = f"{filename}/{str(identy)}.mp3"
    tts.save(f"{filename}/{str(identy)}.mp3")
    utils.export.export_audio(pathPt,pathEn,f"{filename}/words/{textEng}.mp3")
    identy+=1

    print(f"{textPort} : {textEng}")
    return identy