import time

import pyfirmata

from src.servo import Servo

PORT = 'COM3'
THUMB =
INDEX =
MIDDLE =
RING =
LITTLE =
PAUSE = 2


class Hand:
    def __init__(self):
        board = pyfirmata.Arduino(PORT)
        iter8 = pyfirmata.util.Iterator(board)
        iter8.start()
        self.thumb = Servo(board, THUMB)
        self.index = Servo(board, INDEX)
        self.middle = Servo(board, MIDDLE)
        self.ring = Servo(board, RING)
        self.little = Servo(board, LITTLE)

    def show_a(self):
        self.index.turn_cw(1)
        self.middle.turn_cw(1)
        self.ring.turn_cw(1)
        self.little.turn_cw(1)
        time.sleep(2)
        self.index.turn_cw(1)
        self.middle.turn_cw(1)
        self.ring.turn_cw(1)
        self.little.turn_cw(1)

    def show_b(self):
        pass

    def show_c(self):
        pass

    def show_d(self):
        pass

    def show_e(self):
        pass

    def show_f(self):
        pass

    def show_g(self):
        pass

    def show_h(self):
        pass

    def show_i(self):
        pass

    def show_j(self):
        pass

    def show_k(self):
        pass

    def show_l(self):
        pass

    def show_m(self):
        pass

    def show_n(self):
        pass

    def show_o(self):
        pass

    def show_p(self):
        pass

    def show_q(self):
        pass

    def show_r(self):
        pass

    def show_s(self):
        pass

    def show_t(self):
        pass

    def show_u(self):
        pass

    def show_v(self):
        pass

    def show_w(self):
        pass

    def show_x(self):
        pass

    def show_y(self):
        pass

    def show_z(self):
        pass


if __name__ == '__main__':
    hand = Hand()
    hand.show_a()
