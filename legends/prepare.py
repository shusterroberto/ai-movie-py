def valid_integer(text="123"):
    try:
        int(text)
        return True
    except ValueError:
        return False

conteudo=""

with open('C:\\Users\\shust\\OneDrive\\Inglês Conversação\\legends\\The Simpsons - S34E01.srt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.replace("\n"," ")
        
        if(len(linha.strip())>1):
            posicao = linha.find("00:")            
            if (posicao == -1) and not (valid_integer(linha) and (len(linha.strip())>1)):
                conteudo += linha
                print(linha)

conteudo = conteudo.replace(".","\n")
conteudo = conteudo.replace("?","\n")
conteudo = conteudo.replace("\n\n\n","\n")
conteudo = conteudo.replace("\n\n","\n")
conteudo = conteudo.replace("<i>","")
conteudo = conteudo.replace("</i>","")


with open("C:\\Users\\shust\\OneDrive\\Inglês Conversação\\legends\\legenda.txt", "w") as arquivo:
    arquivo.write(conteudo)