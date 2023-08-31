import teste.pyttsx3 as pyttsx3

engine = pyttsx3.init()
engine.say("Olá, isso é um exemplo de texto convertido em áudio.")
engine.save_to_file("Isso é um exemplo de texto convertido em áudio.", "output.mp3")
engine.runAndWait()
