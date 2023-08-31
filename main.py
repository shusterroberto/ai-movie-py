import os
from moviepy.editor import *

FFMPEG_BINARY = os.getenv('FFMPEG_BINARY', 'ffmpeg-imageio')
#IMAGEMAGICK_BINARY = os.getenv('IMAGEMAGICK_BINARY', 'auto-detect')
IMAGEMAGICK_BINARY = "C:/Program Files/ImageMagick-7.1.1-Q16-HDRI/ffmpeg.exe/magick.exe"

# VIDEO CLIPS
clip = VideoClip(make_frame, duration=4) # for custom animations (see below)
clip = VideoFileClip("my_video_file.mp4") # or .avi, .webm, .gif ...
clip = ImageSequenceClip(['image_file1.jpeg', ...], fps=24)
clip = ImageClip("my_picture.png") # or .jpeg, .tiff, ...
clip = TextClip("Hello!", font="Amiri-Bold", fontsize=70, color="black")
clip = ColorClip(size=(460,380), color=[R,G,B])

# AUDIO CLIPS
clip = AudioFileClip("my_audiofile.mp3") # or .ogg, .wav... or a video!
clip = AudioArrayClip(numpy_array, fps=44100) # from a numerical array
clip = AudioClip(make_frame, duration=3) # uses a function make_frame(t)

# Criar um objeto VideoClip com um texto
txt_clip = TextClip(txt="Olá, mundo!", fontsize=70, color='white')

# Carregar um arquivo de áudio
audio_clip = AudioFileClip("C:/Users/shust/OneDrive/Inglês Conversação/Modulo 01/aula01modulo01.mp3")

video_with_audio = VideoFileClip("C:\audios\video.mp4")
video_with_audio = txt_clip.set_audio(audio_clip)
video_with_audio.duration = '100.000000'
video_with_audio.fps=24
video_with_audio.write_videofile("video.mp4")
