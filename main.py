from detection.camera_detect import *
from peripherals.lcd_display import *

def main():
    start_lcd()
    print("lcd started")
    send_to_lcd(" ")
    print("sent first to LCD")
    detect()

if __name__ == '__main__':
    main()