import re
import unittest
from collections import Counter
from string import ascii_lowercase
from functools import reduce

rooms = ['aaaaa-bbb-z-y-x-123[abxyz]', 'a-b-c-d-e-f-g-h-987[abcde]',
         'not-a-real-room-404[oarel]', 'totally-real-room-200[decoy]']


class TestCode(unittest.TestCase):

    def test_checksum_function(self):
        self.assertEqual(check_sum(rooms[0]), 'abxyz')
        self.assertEqual(check_sum(rooms[1]), 'abcde')
        self.assertEqual(check_sum(rooms[2]), 'oarel')

    def test_checksum_calculation(self):
        self.assertEqual(calculate_checksum(rooms[0]), 'abxyz')
        self.assertEqual(calculate_checksum(rooms[1]), 'abcde')
        self.assertEqual(calculate_checksum(rooms[2]), 'oarel')
        self.assertNotEqual(calculate_checksum(rooms[3]), 'decoy')

    def test_if_room_is_real(self):
        self.assertEqual(is_real_room(rooms[0]), True)
        self.assertEqual(is_real_room(rooms[3]), False)

    def test_getID(self):
        self.assertEqual(get_ID(rooms[0]), 123)
        self.assertEqual(get_ID(rooms[1]), 987)

    def test_sum_values(self):
        self.assertEqual(sum_values([1, 2, 3, 4, 5]), 15)


class TestPuzzle(unittest.TestCase):

    def test_input(self):
        summed = list()
        with open('04.txt', 'r') as file:
            for line in file:
                if is_real_room(line):
                    summed.append(get_ID(line))
        # print(sum_values(summed))


class Decrypt(unittest.TestCase):

    def test_position(self):
        self.assertEqual(position('a'), 0)
        self.assertEqual(position('e'), 4)
        self.assertEqual(position('z'), 25)


class TestDecryption(unittest.TestCase):

    def test_decryption(self):
        thenames = list()
        with open('04.txt', 'r') as file:
            for room in file:
                if is_real_room(room):
                    id = get_ID(room)
                    name = ''.join(
                        [char for char in room if char in ascii_lowercase or char == '-'])
                    newname = rotate(name, id)
                    if 'north' in newname.lower():
                        print(room)
                    thenames.append(newname)
        self.assertEqual(
            thenames[0], 'rampaging projectile rabbit training iragn')


def rotate(name, times):
    newname = list()
    for char in name:
        if char == '-':
            newname.append(' ')
        else:
            start = position(char)
            end = (start + times) % 26
            newname.append(ascii_lowercase[end])
    return ''.join(newname)


def position(char):
    return ascii_lowercase.index(char)


def sum_values(lst):
    return reduce(lambda x, y: x + y, lst)


def is_real_room(room):
    if check_sum(room) == calculate_checksum(room):
        return True
    else:
        return False


def get_ID(room):
    chars = list(room)
    return int(''.join([s for s in chars if s.isdigit()]))


def check_sum(room):
    pattern = r'^.*\[(.*)\].*$'
    matched = re.match(pattern, room)
    return matched.group(1)


def calculate_checksum(room):
    number = room.split('[')

    # count occurrences of each element
    elements = Counter(char for char in number[0] if char in ascii_lowercase)
    return ''.join(char for char, count in sorted(elements.items(), key=lambda item: (-item[1], item[0]))[:5])


if __name__ == '__main__':
    unittest.main()
