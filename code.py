import board
import busio
import digitalio
import math
import time
BARS = 8
spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI)
spi.try_lock()
send = digitalio.DigitalInOut(board.A0)
send.direction = digitalio.Direction.OUTPUT
send.value = False


while True:
    statline = map(int, input().split())
    bars_on = map(lambda n: math.floor((n/100)*BARS), statline)
    bytevals = list(map(lambda b: (2**b)-1, bars_on))
    spi.write(bytearray(bytevals)[0:1])
    send.value = True
    time.sleep(0.01)
    send.value = False
