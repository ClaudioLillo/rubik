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
        
    def __getitem__(self, key):
         if key == 'up':
             return self.up
         if key == 'down':
             return self.down
         if key == 'front':
             return self.front
         if key == 'back':
             return self.back
         if key == 'left':
             return self.left
         if key == 'right':
             return self.right
         
    def __str__(self):
        faces = ['up','down','front','back', 'left', 'right']
        out = ''
        for face in faces:
            for i in range(3):
                for j in range(3):
                    out += self[face][i][j]
            out += ":"
        return out
    
    def is_solved(self):
        sides = str(self).split(":")
        sides.pop()
        sides.sort()
        print(''.join(sides))
        if ''.join(sides) != 'bbbbbbbbbgggggggggooooooooorrrrrrrrrwwwwwwwwwyyyyyyyyy':
            return False
        arr = (str(self)).split(":")
        arr.pop()
        solved = ['bbbbbbbbb','ggggggggg','ooooooooo','rrrrrrrrr','wwwwwwwww','yyyyyyyyy']
        for i in range(6, 2):
            diff = arr.index(solved[i]) - arr.index(solved[i+1])
            if diff != 1 or diff!= -1:
                return False
        return True

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
        current = copy.deepcopy(self)
        self.up = np.rot90(current.up)
        self.front[0] = current.left[0]
        self.left[0] = current.back[0]
        self.back[0] = current.right[0]
        self.right[0] = current.front[0]

    def disorder(self, n):
        movements = [self.front_to_right,
                     self.front_to_up, self.rotate_upper_ccw]
        for i in range(n):
            move = random.randint(0, len(movements)-1)
            movements[move]()
            
    


# rubik = Rubik()
# rubik.show()
# rubik.front_to_up()
# rubik.front_to_right()
# rubik.rotate_upper_ccw()
# rubik.show()
# rubik.disorder(1000)
# rubik.show()
# print(rubik)
# print(rubik.is_solved())

# rubik2 = Rubik()
# print(rubik2.is_solved())
# rubik2.front_to_up()
# print(rubik2.is_solved())
# rubik2.front_to_right()
# print(rubik2.is_solved())
# rubik2.rotate_upper_ccw()
# print(rubik2.is_solved())

rubik = Rubik()
rubik.disorder(100)
rubik.show()

steps_dict = {}
steps_memo = []
n = 10
paths = {}
for i in range(1000):
    steps = [
        {"id": "ftu", "fn": rubik.front_to_up},
        {"id": "ftr", "fn": rubik.front_to_right},
        {"id": "ruc", "fn": rubik.rotate_upper_ccw},
    ]
    for i in range(n):
        r0 = str(rubik)
        index = random.randint(0, len(steps)-1)
        steps[index]["fn"]()
        r1 = str(rubik)
        steps_dict[f'{r0}-{r1}'] = steps[index]["id"]
        

print("sd: ", steps_dict)