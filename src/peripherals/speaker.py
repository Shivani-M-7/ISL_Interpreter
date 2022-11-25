import os

def tts(word):
    print("sent to tts")
    os.system('espeak "{}"'.format(word)) 