def clear_text(text="",characters = ".!?;¡"):
    new_text=text
    for letter in characters:
        new_text=new_text.replace(letter,'')
    
    print(f"text_orig: {text} - new_text: {new_text}")
    return new_text

#texto = clear_text(text="Qual é o melhor?")