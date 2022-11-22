from peripherals import lcd_display
import time

string = ["Hello", "Very", "Good", "Morning", "Not", "Really", "But", "Yes","Anyways", "Hellohello","WHAT","kms"]


for s in string:
    lcd_display.send_to_lcd(s)
    time.sleep(2)