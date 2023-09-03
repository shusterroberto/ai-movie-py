from googletrans import Translator

def english_to_portuguese(text=""):
    translator = Translator(service_urls=['translate.google.com','translate.google.com.br'])
    translated = translator.translate(text=text, src='en', dest='pt')
    print(translated.text)
    return translated.text