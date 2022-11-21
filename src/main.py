from detection.camera_detect import *
import peripherals.lcd_display as lcd

def main():
    start_lcd()
    print("lcd started")
    send_to_lcd(" ")
    print("sent first to LCD")
    #detect()

if __name__ == '__main__':
    main()