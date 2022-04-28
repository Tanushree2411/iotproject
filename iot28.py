import speech_recognition as sr
r = sr.Recognizer()



hello = sr.AudioFile('Recording.wav')
with hello as source:
	audio = r.record(source)
try:
	s = r.recognize_google(audio)
	print(s)
	with open("binary.txt", "w") as f:
		f.write(s)
except Exception as e:
	print("Exception: "+str(e))
