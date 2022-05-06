from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Navio2/LocalRepo/AerospaceEE/Camera/TestPic2.jpg')
camera.stop_preview()






