from detection.camera_detect import *
from peripherals.lcd_display import *

def main():
    start_lcd()
    send_to_lcd(" ", 1)
    detect()

if __name__ == '__main__':
    main()