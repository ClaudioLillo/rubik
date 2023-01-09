import numpy as np
import copy
import random


def fill_face(color):
    return np.full((3, 3), color)


class Rubik:

    def __init__(self):
        self.up = fill_face('w')
        self.down = fill_face('y')
        self.front = fill_face('b')
        self.back = fill_face('g')
        self.left = fill_face('r')
        self.right = fill_face('o')

    def show(self):
        print('up: \n', self.up)
        print('down: \n', self.down)
        print('front: \n', self.front)
        print('back: \n', self.back)
        print('left: \n', self.left)
        print('right: \n', self.right)
        print('-----------------')

    def front_to_up(self):
        current = copy.copy(self)
        self.up = current.front
        self.front = current.down
        self.down = current.back
        self.back = current.up
        self.left = np.rot90(current.left)
        self.right = np.rot90(current.right, 3)

    def front_to_right(self):
        current = copy.copy(self)
        self.up = np.rot90(current.up)
        self.down = np.rot90(current.down, 3)
        self.front = current.left
        self.left = current.back
        self.back = current.right
        self.right = current.front

    def rotate_upper_ccw(self):
        current = copy.copy(self)
        self.up = np.rot90(current.up)
        self.front[0] = current.left[0]
        self.left[0] = current.back[0]
        self.back[0] = current.right[0]
        self.right[0] = current.front[0]

    def disorder(self, n):
        movements = [self.front_to_right,
                     self.front_to_up, self.rotate_upper_ccw]
        for i in range(n):
            print(i)
            move = random.randint(0, len(movements)-1)
            movements[move]()


rubik = Rubik()
rubik.show()
rubik.front_to_up()
rubik.front_to_right()
rubik.rotate_upper_ccw()
rubik.show()
rubik.disorder(1000)
rubik.show()
