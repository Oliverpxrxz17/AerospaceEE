import picamera
with picamera.PiCamera() as camera:
    for filename in camera.record_sequence([
            'clip01.h264',
            'clip02.h264',
            'clip03.h264']):
        print('Recording to %s' % filename)
        camera.wait_recording(10)
