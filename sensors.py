import RPi.GPIO as GP
GP.setmode(GP.BCM)
while True:
      GP.wait_for_edge(9,GP.FALLING)
      print("low water")
