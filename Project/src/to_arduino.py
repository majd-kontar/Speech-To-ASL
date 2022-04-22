import serial
import time


class Arduino:
    def __init__(self):
        self.ardu = serial.Serial(port='COM7', baudrate=9600, timeout=.1)

    def send(self, x):
        self.ardu.write(bytes(x, 'utf-8'))
        time.sleep(0.05)
        data = self.ardu.readline()
        return data


if __name__ == '__main__':
    arduino = Arduino()
    while True:
        num = input("Enter a character: ")
        value = arduino.send(num)
        print(value)
