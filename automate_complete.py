
index=1
while(index<=54):
    path = f"C:/Users/shust/OneDrive/Inglês Conversação/Modulo 01/bkp/aula{index}modulo01.txt"
    print(path)
    translate_file.translate_lines(path=path)
    index += 1