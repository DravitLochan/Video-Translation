from pydub import AudioSegment
n = 19
for i in range(n):
	sound = AudioSegment.from_mp3("welcome " + str(i) + ".mp3")
	sound.export("welcome " + str(i) + ".wav", format="wav")
