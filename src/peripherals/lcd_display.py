from peripherals.lcd_config import *
import time

# Implement an upwards scrolling text for the LCD display.

prev_line = 4
prev_string = ""

def start_lcd():
    # Initialise display
    lcd_init()

    # Toggle backlight on
    GPIO.output(LED_ON, True)
    #time.sleep(1)
    
    #lcd_byte(LCD_LINE_1, LCD_CMD)
    #lcd_string("Hello!!", 1)


def send_to_lcd(string):
    global prev_string
    
    if string == prev_string:
        return
    
    global prev_line
    if prev_line == 1:
        lcd_byte(LCD_LINE_2, LCD_CMD)
        prev_line = 2
    elif prev_line == 2:
        lcd_byte(LCD_LINE_3, LCD_CMD)
        prev_line = 3
    elif prev_line == 3:
        lcd_byte(LCD_LINE_4, LCD_CMD)
        prev_line = 4
    elif prev_line == 4:
        lcd_byte(LCD_LINE_1, LCD_CMD)
        prev_line = 1
    
    print(prev_line)
    lcd_string(string, 2)	#print some left justified word on the LCD
    #time.sleep(1)
