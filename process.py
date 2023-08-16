from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

input_text = "I am happy to join with you today in what will go down in history as the greatest demonstration for freedom in the history of our nation."
target_language = "pt"  # Código do idioma de destino (por exemplo, "pt" para português)

#translated_text = translate_text(input_text, target_language)
#print(f"Original: {input_text} \n")
#print(f"Translated: {translated_text}")

input_text = input_text.replace("will go down","will stay")

palavra=""
frase=""
for i in input_text:
    palavra = palavra + i
    if(i==" " or i==","):        
        translated_text = translate_text(palavra, target_language)
        print(f"Diga: {translated_text} \n {palavra} \n")
        frase=frase + palavra
        palavra=""
        
    if(i==","):
        print(f"{frase} \n")
        translated_text = translate_text(frase, target_language)
        print(f"Diga: {translated_text}")
        frase=""
        palavra=""