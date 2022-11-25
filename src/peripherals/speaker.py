import os

def tts(word):
   os.system('espeak "{}"'.format(word)) 