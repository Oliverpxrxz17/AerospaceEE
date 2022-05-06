import picamera

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.start_recording('flightTestStabiliseMode2.h264')
camera.wait_recording(120)
camera.stop_recording()
