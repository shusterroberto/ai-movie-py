import words

def process():
    module = "01"
    index = 17
    path = "C:/Users/shust/OneDrive/Inglês Conversação/Modulo 01/bkp/"

    with open('C:/Users/shust/OneDrive/Inglês Conversação/phrases.txt', 'r') as arquivo:
        for linha in arquivo:
            file = words.create_scripting(text=linha)
            fullPath = f"{path}aula{index}modulo{module}.txt"
            print(fullPath)
            index += 1

            with open(fullPath, "w") as arquivo: 
                arquivo.write(file)

process()