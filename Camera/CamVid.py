import picamera
with picamera.PiCamera() as camera:
    for filename in camera.record_sequence([
            'flight_09_05_11.h264',
            'flight_09_05_12.h264',
            'flight_09_05_13.h264',
            'flight_09_05_14.h264',
            'flight_09_05_15.h264',
            'flight_09_05_16.h264',
            'flight_09_05_17.h264',
            'flight_09_05_18.h264',
            'flight_09_05_19.h264',
            'flight_09_05_110.h264']):
        print('Recording to %s' % filename)
        camera.wait_recording(10)
