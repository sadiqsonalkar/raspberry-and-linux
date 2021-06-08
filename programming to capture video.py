from picamera import PiCamera
from time import sleep
try:
    camera=PiCamera()
    camera.start_preview(alpha=150)
    camera.start_recording('thor.h264')
    sleep(5)
    camera.stop_recording()
    camera.stop_preview()
except Exception as e:
    print(e)
    camera.stop_preview()
