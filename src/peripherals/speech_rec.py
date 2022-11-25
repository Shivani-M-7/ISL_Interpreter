import os
import speech_recognition as sr

recogniser = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        try:
            audio = recogniser.listen(source)
            data = recogniser.recognize_google(audio)
        except:
            print('No audio detected')