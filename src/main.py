from camera_detect import detect_loop
import time
from peripherals import send_to_lcd, start_lcd

def start():
    start_lcd()
    time.sleep(2)
    print("lcd started")
    time.sleep(4)
    send_to_lcd(" ")
    print("Starting the ISL Interpreter.", "")
    send_to_lcd("B1G2", "")
    send_to_lcd("ISL Interpreter.", "")
    time.sleep(4)
    send_to_lcd("Starting...", "")
    
    return True



if __name__ == '__main__':
    if start():
        detect_loop()