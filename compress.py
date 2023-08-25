from pydub import AudioSegment
import os

def finalize(inputs_dir="./files/", output="file.mp3"):
    print(f"Trabalhando no arquivo: {output}")
    list = os.listdir(inputs_dir)
    countFiles = len(list)
    i=0
    longSound = False
    audios = "C:/audios/"
    finalSong = AudioSegment.from_mp3(audios + "bemvindo.mp3")

    # Percorre os arquivos no diretório
    while i<countFiles:
        fullPath = inputs_dir + "/" +str(i)+ ".mp3"
        
        if os.path.isfile(fullPath):  # Verifica se é um arquivo (não diretório)
            print("Caminho completo:", fullPath)
            print("Tamanho:", os.path.getsize(fullPath), "bytes")
            print("-" * 40)

            audio1 = AudioSegment.from_mp3(fullPath)
            if(longSound):
                audio2 = AudioSegment.from_file(audios + "2seg.m4a")
                longSound = False
            else:
                audio2 = AudioSegment.from_file(audios + "1seg.m4a")
                longSound = True

            finalSong = finalSong + audio1 + audio2
            i+=1

    # Salve o arquivo final
    finalSong.export(output, format="mp3")

    return True