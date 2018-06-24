from moviepy.editor import *

movie = VideoFileClip("splice.mp4").\
        set_audio( AudioFileClip("final.mp3") )

movie.write_videofile("output.mp4", codec="mpeg4")
