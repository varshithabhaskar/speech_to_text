from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
recognizer=sr.Recognizer()
with sr.Microphone() as mic:
    print("speak now")
    listening=recognizer.listen(mic)
    print("processing")
    op=recognizer.recognize_google(listening,language="en")
    msg=op
    print("output:",op)
