import unittest

distance = 0


def new_direction(current, turned):
    next_direction = {
        'N': {'R': 'E', 'L': 'W'},
        'E': {'R': 'S', 'L': 'N'},
        'W': {'R': 'N', 'L': 'S'},
        'S': {'R': 'W', 'L': 'E'}
    }
    return next_direction.get(current, {}).get(turned, {})


class TestDirection(unittest.TestCase):

    def test_newdirection(self):
        self.assertEquals(new_direction('N', 'R'), 'E')
        self.assertEquals(new_direction('E', 'L'), 'N')
        self.assertEquals(new_direction('S', 'R'), 'W')
        self.assertEquals(new_direction('W', 'L'), 'S')


if __name__ == '__main__':
    unittest.main()
