from RPLCD import CharLCD
import time

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33,31,29,23])

def output(message):
    lcd.write_string(message)
    print(message)
