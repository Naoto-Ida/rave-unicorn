import unicornhat as UH
import time
import random

if __name__=='__main__':
  UH.brightness(0.01)
  UH.rotation(90)
  r = range(0,8)
  while True:
    for x in r:
      y = random.choice(r)
      for fill in range(0, y):
        UH.set_pixel(x,fill,255,0,255)

    UH.show()
    time.sleep(0.05)
    UH.clear()
    UH.show()
    time.sleep(0.05)
