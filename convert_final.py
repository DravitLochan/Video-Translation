from pydub import AudioSegment
sound = AudioSegment.from_file("final.wav")
sound.export("final.mp3", format="mp3")