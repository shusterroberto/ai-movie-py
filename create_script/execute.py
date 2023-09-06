import words
import translate_file

def process_translate(path="C:"):
    print(path)
    translate_file.translate_lines(path=path)

def process(st="iniciando processamento"):
    print(st)
    module = "01"
    index = 17
    path = "C:/Users/shust/OneDrive/Inglês Conversação/Modulo 01/bkp/"

    with open('C:\\Users\\shust\\OneDrive\\Inglês Conversação\\phrases.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(linhas)
            file = words.create_scripting(text=linha)
            fullPath = f"{path}aula{index}modulo{module}.txt"
            print(fullPath)
            index += 1

            if(len(file)>0):
                with open(fullPath, 'w', encoding='iso-8859-1') as arquivo: 
                    arquivo.write(file)

index=17
while(index<=54):
    path = f"C:/Users/shust/OneDrive/Inglês Conversação/Modulo 01/bkp/aula{index}modulo01.txt"
    print(path)
    translate_file.translate_lines(path=path)
    index += 1