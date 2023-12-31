from googletrans import Translator
import create_script.pytranslate

def english_to_portuguese(text=""):
    try:
        translator = Translator(service_urls=['translate.google.com','translate.google.com.pt','translate.google.com.en'])

        translated = translator.translate(text=text, src='en', dest='pt')
        print(translated.text)
        return translated.text
    except Exception:
        return create_script.pytranslate.english_to_portuguese(text=text)