import os
import create_script.translating

def translate_lines(path = ""):
    conteudo = os.listdir(path)
    for item in conteudo:
        print(item)
        item_caminho = os.path.join(path, item)
        if os.path.isfile(item_caminho):
            filelocal = ""
            with open(item_caminho, 'r', encoding='ASCII') as archive:
                lines = archive.readlines()
    
                for line in lines:
                    if(line.find("@")<=0):
                        text=line.replace("|\n","").replace("|","").replace("\n","")
                        translated = create_script.translating.english_to_portuguese(text)
                        #finish = False

                    if(len(translated)>0):
                        line = f"{text}|{translated}@\n"

                    filelocal += line
                    print(line)

            with open(path, 'w') as newFile:
                newFile.write(filelocal)

    return True