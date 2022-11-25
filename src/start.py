import subprocess
from time import sleep

y=(20)
subprocess.Popen(["python3", 'main.py'])
sleep(y)
subprocess.Popen(["python3", 'speech_rec.py'])
sleep (y)