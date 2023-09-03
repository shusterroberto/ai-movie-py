import os

from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import *

FFMPEG_BINARY = os.getenv('FFMPEG_BINARY', 'ffmpeg-imageio')
#IMAGEMAGICK_BINARY = os.getenv('IMAGEMAGICK_BINARY', 'auto-detect')
IMAGEMAGICK_BINARY = "C:/Program Files/ImageMagick-7.1.1-Q16-HDRI/ffmpeg.exe/magick.exe"


generator = lambda text: TextClip(text, font='Georgia-Regular',
                                  font_size=24, color='white')
sub = SubtitlesClip("subtitles.srt", generator)
sub = SubtitlesClip("subtitles.srt", generator, encoding='utf-8')
myvideo = VideoFileClip("myvideo.avi")
#final = CompositeVideoClip([clip, subtitles])
#final.write_videofile("final.mp4", fps=myvideo.fps)