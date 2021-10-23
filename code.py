import board
import neopixel
import time
PIXEN = 10
RED = (0x10, 0, 0)

pix = list(map(lambda p: neopixel.NeoPixel(p, PIXEN, pixel_order=neopixel.GRB),
               [board.A0, board.A1, board.A2, board.A3, board.A4, board.A5,
                board.D5, board.D6, board.D9, board.D10, board.D11, board.D12]))

while True:
    statline = map(int, input().split())
    bars_on = list(map(lambda n: round((n/100)*PIXEN), statline))
    for i in range(0, len(pix)):
        for j in range(0, PIXEN):
            color = (round((j/PIXEN)*16), round((PIXEN-j)/PIXEN)*16, 0)
            pix[i][j] = color if j < (bars_on[i] if i < len(bars_on) else 0) \
                else 0
        pix[i].show()
