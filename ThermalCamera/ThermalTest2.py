
##################################
# MLX90640 Test with Raspberry Pi
##################################

#Code used from:
#https://makersportal.com/blog/2020/6/8/high-resolution-thermal-camera-with-raspberry-pi-and-mlx90640
import time,board,busio
import numpy as np
import adafruit_mlx90640
import sys

i2c = busio.I2C(board.SCL, board.SDA, frequency=400000) # setup I2C
mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ # set refresh rate


frame = np.zeros((24*32,)) # setup array for storing all 768 temperatures and initialising to 0
while True:
    try: #try and except is used to try something and if there's an error it will do something else
        mlx.getFrame(frame) # read MLX temperatures into frame var

        break
    except ValueError:
        continue # if error, just read again

#calculate the size in bytes of the data array for one frame 
packet_length = len(frame)

# print out the average temperature from the MLX90640
#print('Average MLX90640 Temperature: {0:2.1f}C ({1:2.1f}F)'.\
#      format(np.mean(frame),(((9.0/5.0)*np.mean(frame))+32.0)))
print(frame)
frame2 = [int(i) for i in frame]

print(frame2)
print (f'Length of the 24x36 datastring in bytes is: {packet_length}.')
print('Byte size: ', sys.getsizeof(frame), 'bits size: ', 8*sys.getsizeof(frame))

print('byte size: ', sys.getsizeof(frame2), 'bit size: ', 8*sys.getsizeof(frame2))


