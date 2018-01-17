import numpy as np


class Cube:
    """ state is a 6x3x3 array with the colors as integers.
    order of the arrays are rot_f B U D L R
    turns are all clockwise
    (0,0) index in each of the arrays is in the top-left corner when
    viewed from the angle shown in the following diagram
    +---+
    | U |
    +---+---+---+---+
    | F | R | B | L |
    +---+---+---+---+
    | D |
    +---+
    """
    def __init__(self):
        self.state = np.zeros((6, 3, 3), np.int8)
        for i in range(6):
            self.state[i, ...] = i

    def rot_f(self, n=1):
        _cycle_params = [(4, Ellipsis, 2), (2, 2, Ellipsis), (5, Ellipsis, 0), (3, 0, Ellipsis)]
        self._cycle(_cycle_params, n)

    def rot_b(self, n=1):
        _cycle_params = [(5, Ellipsis, 2), (2, 0, Ellipsis), (4, Ellipsis, 0), (3, 2, Ellipsis)]
        self._cycle(_cycle_params, n)

    def rot_u(self, n=1):
        _cycle_params = [(4, 0, Ellipsis), (1, 0, Ellipsis), (5, 0, Ellipsis), (0, 0, Ellipsis)]
        self._cycle(_cycle_params, n)

    def rot_d(self, n=1):
        _cycle_params = [(4, 2, Ellipsis), (0, 2, Ellipsis), (5, 2, Ellipsis), (1, 2, Ellipsis)]
        self._cycle(_cycle_params, n)

    def rot_l(self, n=1):
        _cycle_params = [(1, Ellipsis, 2), (2, Ellipsis, 0), (0, Ellipsis, 0), (3, Ellipsis, 0)]
        self._cycle(_cycle_params, n)

    def rot_r(self, n=1):
        _cycle_params = [(0, Ellipsis, 2), (2, Ellipsis, 2), (1, Ellipsis, 0), (3, Ellipsis, 2)]
        self._cycle(_cycle_params, n)

    def _cycle(self, x, n):
        for _ in range(n):
            start_state = self.state.copy()
            for i in range(4):
                j = (i-1) % 4
                self.state[x[i]] = start_state[x[j]]

    def __eq__(self, other):
        return np.array_equal(self.state, other.state)


if __name__ == '__main__':
    cube = Cube()

