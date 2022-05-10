import time

CW = 10
CCW = 170
OFF = 90


class Servo:
    def __init__(self, board, pin_number: int):
        self.board = board
        self.pin_number = pin_number
        self.pin = self.board.get_pin('d:' + str(self.pin_number) + ':s')

    def turn_cw(self, t=None):
        self.pin.write(CW)
        if t is not None:
            time.sleep(t)
            self.pin.write(OFF)

    def turn_ccw(self, t=None):
        self.pin.write(CCW)
        if t is not None:
            time.sleep(t)
            self.pin.write(OFF)

    def turn_off(self, t=None):
        if t is not None:
            time.sleep(t)
            self.pin.write(OFF)
        else:
            self.pin.write(OFF)


if __name__ == '__main__':
    servo = Servo(9)
    servo.turn_cw(2)
    servo.turn_ccw(2)
