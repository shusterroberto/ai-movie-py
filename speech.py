import audios.interations
import utils.text
import utils.export
import utils.folder
import crud.words
import crud.Lines
import crud.lessons
from gtts import gTTS

def text_to_speech(textPort, textEng, filename='C:/Audios/', identy=0, lessonId=0):
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
    output = f"{filename}/words/{textEng}.mp3"
    utils.export.export_audio(audioPort=pathPt, audioEng=pathEn, output=output)
    identy+=1

    wordId = crud.words.force_word(english=textEng, portuguese=textPort, path=output)
    crud.lessons.create_lesson(module=1,lessonId=lessonId,name="Modulo 01",path=pathEn)
    crud.Lines.create_line(lineId=(identy-1),lessonId=lessonId,wordId=wordId,tag="")

    print(f"{textPort} : {textEng}")
    return identy