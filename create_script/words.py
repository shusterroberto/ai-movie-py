import pyphen

def create_scripting(text="I"):
    words = text.split(" ")
    scripting = ""
    phrases = {" "}
    a = pyphen.Pyphen(lang='en')

    for word in words:        
        scripting += a.inserted(word) + "|\n"
        scripting += word + "|\n"
        scripting += word + "|\n"

    temp = ""
    for word in words:
        temp = temp + word + " "
        scripting += temp + "|\n"

    scripting += temp + "|\n"
    scripting += temp + "|\n"
    scripting += temp + "|\n"
    scripting = scripting.replace(" |","|")
    scripting = scripting.replace("\n|","|")
    print(scripting)
    return scripting