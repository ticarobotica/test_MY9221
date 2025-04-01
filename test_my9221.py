# Senzorul MY9221

from machine import Pin
from time import sleep_ms
from random import randint
from my9221 import MY9221

led_bar=MY9221(di=Pin(22), dcki=Pin(21))

nivel=0
led_bar.level(nivel)

while True:
    nivel=randint(0,10)
    led_bar.level(nivel)
    sleep_ms(200)
    