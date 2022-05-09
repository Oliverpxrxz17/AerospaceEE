import picamera


RESOLUTION = (1280, 720)
FRAMERATE = 30

camera = picamera.PiCamera()
camera.resolution = RESOLUTION
camera.framerate = FRAMERATE
camera.exposure_mode = 'sports'


camera.resolution = (640, 480)
camera.start_recording('flightTestAutonomous2.h264')
camera.wait_recording(120)
camera.stop_recording()
