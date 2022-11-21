from lcd_config import *

def main():

  # Initialise display
  lcd_init()

  # Toggle backlight on
  GPIO.output(LED_ON, True)
  time.sleep(1)
