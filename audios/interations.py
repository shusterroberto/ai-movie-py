
def text_interation(textPortuguese=""):
    textComplete=""
    if(textPortuguese[-1]=='?'):
        textComplete='Pergunte: '+textPortuguese
    else:
        textComplete='Diga: '+textPortuguese

    if(textPortuguese[0]=='-'):
        textComplete=textPortuguese.replace('-','')
    
    print(f"textPortuguese: {textPortuguese} - textComplete: {textComplete}")
    return textComplete

#text_interation("Qual é o plano?")