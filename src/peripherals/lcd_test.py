from lcd_display import *

def test():
    strings = ["Hello!!", "Yes", "Money", "No", "What?", "Where", "Document", "Feasible", "Every", "Monring", "I", "Wake", "up", "And", "Have", "To", "go", "to", "college", ":pensive:"]
    start_lcd()
    for s in strings:
        send_to_lcd(s)
        time.sleep(0.500)