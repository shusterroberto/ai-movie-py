from moviepy.editor import *

audio = VideoFileClip("Aula 01 Modulo 01.mp4").audio
audio.write_audiofile("Aula 01 Modulo 01.mp3")