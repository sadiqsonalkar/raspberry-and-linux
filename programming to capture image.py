from picamera import PiCamera
from time import sleep
try:
    camera=PiCamera()
    camera.start_preview(alpha=150)
    sleep(5)
    camera.capture('storm.jpg')
    camera.stop_preview()
except Exception as e:
    print(e)
    camera.stop_preview()
