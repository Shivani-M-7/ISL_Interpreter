from peripherals.lcd_display import send_to_lcd, start_lcd
import time

string = ["Hello", "Very", "Good", "Morning", "Not", "Really", "But", "Yes","Anyways", "Hellohello","WHAT","kms"]

start_lcd()
for s in string:
    send_to_lcd(s)
    time.sleep(2)