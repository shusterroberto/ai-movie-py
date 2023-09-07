import create_script.words
import create_script.translate_file

def process_translate(path="C:"):
    print(path)
    create_script.translate_file.translate_lines(path=path)

def process(path="phrases",bkp="path/", increment=False, module="01",index=17):
    print(path)

    with open(path, 'r', encoding='ASCII') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(linhas)
            file = create_script.words.create_scripting(text=linha)
            fullPath = f"{bkp}aula{index}modulo{module}.txt"
            print(fullPath)

            if(increment):
                index += 1

            if(len(file)>0):
                with open(fullPath, 'w') as archive: 
                    archive.write(file)