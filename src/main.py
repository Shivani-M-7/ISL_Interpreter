from camera_detect import detect_loop
from peripherals import send_to_lcd, start_lcd

def main():
    start_lcd()
    print("lcd started")
    send_to_lcd(" ")
    print("sent first to LCD")
    detect_loop()

if __name__ == '__main__':
    main()