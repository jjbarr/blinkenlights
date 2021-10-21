import board
import neopixel
import time
PIXEN = 10
RED = (0x10, 0, 0)
pix = [neopixel.NeoPixel(board.A0, PIXEN, pixel_order=neopixel.GRB)]

while True:
    statline = map(int, input().split())
    bars_on = list(map(lambda n: round((n/100)*PIXEN), statline))
    for i in range(0, len(pix)):
        for j in range(0, PIXEN):
            pix[i][j] = RED if j < bars_on[i] else 0
        pix[i].show()
