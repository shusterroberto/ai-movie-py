from pydub import AudioSegment

def export_audio(audioPort, audioEng, output=""):
    print(f"Exportando para: {output}")
    print(f"Arquivo: {audioEng}")
    oneSec = AudioSegment.from_file("C:/audios/1seg.m4a")
    twoSec = AudioSegment.from_file("C:/audios/2seg.m4a")
    Portuguese = AudioSegment.from_mp3(audioPort)
    English = AudioSegment.from_mp3(audioEng)
    finalSong = oneSec + Portuguese + twoSec + English
    
    finalSong.export(output, format="mp3")

    return True