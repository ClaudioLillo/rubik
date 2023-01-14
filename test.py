import unittest
import copy

from main import Rubik

faces = ['up','down','front','back', 'left', 'right']

class TestRubikMethods(unittest.TestCase):
    def test_front_to_up(self):
        rubik = Rubik()
        rubik_copy = copy.deepcopy(rubik)
        rubik.front_to_up()
        rubik.front_to_up()
        rubik.front_to_up()
        rubik.front_to_up()
        self.assertEqual(str(rubik), str(rubik_copy))
        
    def test_front_to_right(self):
        rubik = Rubik()
        rubik_copy = copy.deepcopy(rubik)
        rubik.front_to_right()
        rubik.front_to_right()
        rubik.front_to_right()
        rubik.front_to_right()
        self.assertEqual(str(rubik), str(rubik_copy))
        
    def test_rotate_upper_ccw(self):
        rubik = Rubik()
        rubik_copy = copy.deepcopy(rubik)
        rubik.rotate_upper_ccw()
        rubik.rotate_upper_ccw()
        rubik.rotate_upper_ccw()
        rubik.rotate_upper_ccw()
        self.assertEqual(str(rubik), str(rubik_copy))



# rubik.rotate_upper_ccw()
# rubik.show()

if __name__ == '__main__':
    unittest.main()
