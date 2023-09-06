import os
import json
from deep_translator import GoogleTranslator

def english_to_portuguese(text=""):
    try:
        translator = GoogleTranslator(source='en', target='pt')
        results = translator.translate(text=text)
        print(results)
        return results
    except Exception:
        return ""