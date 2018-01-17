import unittest
from cube import Cube


class TestMain(unittest.TestCase):
    def test_rot_f(self):
        cube = Cube()
        res = Cube()
        cube.rot_f(4)
        self.assertEqual(res, cube)

    def test_rot_b(self):
        cube = Cube()
        res = Cube()
        cube.rot_b(4)
        self.assertEqual(res, cube)

    def test_rot_u(self):
        cube = Cube()
        res = Cube()
        cube.rot_u(4)
        self.assertEqual(res, cube)

    def test_rot_d(self):
        cube = Cube()
        res = Cube()
        cube.rot_d(4)
        self.assertEqual(res, cube)

    def test_rot_l(self):
        cube = Cube()
        res = Cube()
        cube.rot_l(4)
        self.assertEqual(res, cube)

    def test_rot_r(self):
        cube = Cube()
        res = Cube()
        cube.rot_r(4)
        self.assertEqual(res, cube)


if __name__ == '__main__':
    unittest.main()
