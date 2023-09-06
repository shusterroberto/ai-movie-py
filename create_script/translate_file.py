import translate
import os
import translate

file = ""
finish = False
def translate_lines(path = ""):
    global finish
    filelocal = ""
    with open(path, 'r') as archive:
        lines = archive.readlines()
        
        for line in lines:
            if(line.find("@")<=0):
                text=line.replace("|\n","").replace("|","").replace("\n","")
                translated = translate.english_to_portuguese(text)
                #finish = False

            if(len(translated)>0):
                line = f"{text}|{translated}@\n"

            filelocal += line
            print(line)

    with open(path, 'w') as newFile:
        newFile.write(filelocal)

    return True