from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo = 24, trigger = 23)

while True:
    print("\nDistance:", sensor.distance * 100)
    sleep(1)
