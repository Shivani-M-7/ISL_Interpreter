import os
import speech_recognition as sr
from peripherals.lcd_display import *

recogniser = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        try:
            audio = recogniser.listen(source)
            data = recogniser.recognize_google(audio)
            d = data.split(", ")
            send_to_lcd(d[0], "Mic")
            
        except:
            print('No audio detected')