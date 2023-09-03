def create_scripting(text="I"):
    words = text.split(" ")
    scripting = ""
    phrases = {" "}

    for word in words:
        scripting += word + "|\n"
        scripting += word + "|\n"
        scripting += word + "|\n"

    temp = ""
    for word in words:
        temp = temp + word + " "
        scripting += temp + "|\n"

    scripting += temp + "|\n"
    scripting += temp + "|\n"
    scripting += temp + "|\n"
    print(scripting)
    return scripting