import numpy as np
from pydub import AudioSegment
import wave

CHANNELS = 1
swidth = 2

def getSampleRate(file_interval, dialogue_interval):
	print (file_interval / dialogue_interval)
	return (file_interval / dialogue_interval)

def samplingFunction(sample_rate, file_path):
	CHANGE_RATE = sample_rate
	spf = wave.open(file_path, 'rb')
	RATE=spf.getframerate()
	signal = spf.readframes(-1)
	wf = wave.open('gen_file.wav', 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(swidth)
	wf.setframerate(RATE*CHANGE_RATE)
	wf.writeframes(signal)
	wf.close()


# interval_file = open('new_srt.srt', 'r')
# print interval_file.read()
intervals = np.loadtxt('new_srt.srt')
# print intervals

prev_end = 0
wav = ".wav"
result = AudioSegment.silent(duration=0)
sound0 = AudioSegment.from_file("audio.wav", format = "wav")

n = 19

for i in range(n):
	d_start = intervals[i][0]
	d_end = intervals[i][1]
	path = "welcome "
	path = path + str(i) + wav
	sound = AudioSegment.from_file(str(path))
	s = str(d_end - d_start)
	print str(len(sound)) + " " + s + "\n"
	sample_rate = getSampleRate(len(sound), d_end - d_start)
	# print sample_rate
	samplingFunction(sample_rate, path)
	seg_file = AudioSegment.from_file('gen_file.wav', format = "wav")
	print len(seg_file)
	result = result + sound0[prev_end : d_start] + seg_file
	prev_end = d_end + 1

result = result + sound0[prev_end:]
result.export("final.wav", format = "wav")