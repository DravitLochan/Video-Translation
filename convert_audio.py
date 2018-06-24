from pydub import AudioSegment
sound = AudioSegment.from_mp3("audio.mp3")
sound.export("audio.wav", format="wav")