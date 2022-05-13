import serial
import time
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        ser.write(b"Hello\n")
        time.sleep(1)
