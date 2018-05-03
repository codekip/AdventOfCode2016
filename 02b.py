import unittest

keypad = '''   1
             2 3 4
           5 6 7 8 9
             A B C
               D 
    '''
testcase = '''ULL
              RRDDD
              LURDL
              UUUUD '''


input = '''RLRDDRLLDLRLUDDULLDRUUULDDLRLUDDDLDRRDUDDDLLURDDDLDDDRDURUDRDRRULUUDUDDRRRLRRRRRLRULRLLRULDRUUDRLRRURDDRLRULDLDULLLRULURRUULLRLLDDDDLLDURRUDLDLURDRDRDLUUUDDRDUUDDULLUURRDRLDDULURRRUDLLULULDLLURURUDRRRRUDRLRDLRRLDDRDDLULDLLLURURDUDRRRRUULURLRDULDRLUDRRUDDUULDURUDLDDURRRDLULLUUDRLLDUUDLDRUDDRLLLLLLDUDUDDLRDLRRDRUDDRRRLLRRDLLRLDDURUURRRDDLDUULLDLDLRURDLLLDDRUUDRUDDDDULRLLDUULRUULLLULURRRLLULDLDUDLDLURUDUDULLDLLUUDRRDRLUURURURURDLURUUDLDRLUDDUUDULDULULLLDLDDULLULLDULRRDRULLURRRULLDDDULULURLRDURLLURUDDULLRUDLRURURRDRDUULDRUUDURDURDDLRDUUULDUUDRDURURDRRRURLLDDLLLURURULULUDLRDLDRDRURLRLULRDLU
UDLDURRULDRDDLDUULUDLDUULUURDDRUDRURRRUDRURLLDDRURLDLRDUUURDLLULURDDUDDDRRRURLLDLDLULRDULRLULDLUUDLLRLDLRUUULDDUURDLDDRRDLURLDUDDRURDRRURDURRRLUULURDDLRDLDRRRLDUDRLRLLRLDDUULDURUUULLLRRRRRRRDRRRDRLUULDLDDLULDRDUDLLUDRRUDRUUDULRLUURDDDDRRUUDLURULLLURDULUURDRDDURULRUDRRDLRDUUUUUDDDRDRDDRUDRDDDRLRUUDRDRDDDLUDRDRLDRDDRULURDRLDRUDUDRUULRLLUDRDRLLLLDUDRRLLURDLLLDRRUDDUDRLRLDUDRLURRUUULURDDRUURRLDRLRRRUUDLULDDDRDLDUUURLLUULDDRRUDLDDRUDUDUURURDDRDULLLLLULRRRDLRRRDDDLURDDDDLUULLLRDDURRRRLURRLDDLRUULULRDRDDDDLDUUUUUUDRRULUUUDD
UURDRRUDLURRDDDLUDLRDURUDURDLLLLRDLRLRDDRDRDUUULRDLLDLULULRDUDDRRUUDURULDLUDLRDRUDLDDULLLDDRDLLDULLLURLLRDDLDRDULRRDDULRDURLLRUDRLRRLUDURLDRDLDLRLLLURLRRURDLDURDLUDULRDULLLDRDDRDLDRDULUULURDRRRLDRRUULULLDDRRLDLRUURLRUURLURRLLULUUULRLLDDUDDLRLDUURURUDLRDLURRLLURUDLDLLUDDUULUUUDDDURDLRRDDDLDRUDRLRURUUDULDDLUUDDULLDDRRDDRRRUDUDUDLDLURLDRDLLLLDURDURLRLLLUUDLRRRRUDUDDLDLRUURRLRRLUURRLUDUDRRRRRRRLDUDDRUDDLUDLRDDDRLDUULDRDRRDLDRURDLDRULRLRLUDRDLRRUURUUUUDLDUUULLLRRRRRDLRRURDDLLLLUULDLLRULLUDLLDLLUDLRLRRLRURDDRRL
URDRDLLRDDDLLLDDLURLRURUURRRLUURURDURRLLUDURRLRLDLUURDLULRRDRUDDLULDLDRLDLRLRRLLLDDDUDDDLRURURRLLDRRRURUDLRDDLLDULDDLDRLUUUDRRRULDUULRDDDLRRLLURDDURLULRDUDURRLLDLLRLDUDDRRDDLRLLLDUDRLUURRLLDULRLDLUUUUUDULUDLULUDDUURRURLDLDRRLDLRRUDUDRRDLDUDDLULLDLLRDRURDRDRRLDDDDRDDRLLDDDLLUDRURLURDRRRRRUDDDUDUDDRDUUDRRUDUDRLULDDURULUURUUUURDRULRLRULLDDRRRUULRRRRURUDLDLRDLLDRLURLRUULLURDUDULRRURLRLLRRLLLURULRRRLDDUULLUUULRRDRULUUUUDRDRRDLRURLRLLRLRRRDRDRLDLUURUURULLDLULRRLRRDRULRRLLLDDURULLDLDLDLUUURDLDLUUDULRLLUDDRRDLLDLDLDURLUURRDDRRURDRLUDRLUUUDLDULDLUDRLDUDDLLRUDULLLLLDRRLLUULLUUURRDDUURDLLRDDLRLLU
LDUDRRDLUUDDRLLUUULURLDUDLUDLRLDRURLULRLLDDLRRUUUDDDDRDULDDUUDLRUULDRULLRDRUDDURLDUUURRUDUDRDRDURRDLURRRDRLDLRRRLLLRLURUURRDLLRDLDDLLRDUDDRDUULRULRRURLUDDUDDDUULLUURDULDULLLLRUUUDDRRRLDDDLDLRRDRDRDLUULRLULDRULDLRDRRUDULUDLLUDUULRDLRRUUDDLLDUDDRULURRLULDLDRRULDDRUUDDLURDLRDRLULRRLURRULDUURDLUDLLDRLDULLULDLLRDRDLLLUDLRULLRLDRDDDLDDDLRULDLULLRUUURRLLDUURRLRLDUUULDUURDURRULULRUUURULLLRULLURDDLDRLLRDULLUDLDRRRLLLLDUULRRLDURDURDULULDUURLDUDRLRURRDLUUULURRUDRUUUDRUR
'''

def get_position(current,line):
    letters = list(line)
    func = {
        'U': up,
        'L': left,
        'D': down,
        'R': right
    }
    for char in letters:
        next = func[char]
        current = next(current,char)
    return current

def up(current, letter):
    if current in [1, 2, 4, 5, 9]:
        return current
    elif current in [6, 7, 8]:
        return current - 4
    elif current == 3:
        return 1
    elif current == 'A':
        return 6
    elif current == 'B':
        return 7
    elif current == 'C':
        return 8
    elif current == 'D':
        return 'B'

def left(current, letter):
    if current in [1, 2, 5, 'A', 'D']:
        return current
    elif current in [3, 4, 6, 7, 8, 9]:
        return current - 1
    elif current == 'B':
        return 'A'
    elif current == 'C':
        return 'B'

def down(current, letter):
    if current == 1:
        return 3
    if current in [2, 3, 4]:
        return current + 4
    elif current in [5, 9, 'A', 'C', 'D']:
        return current
    elif current == 6:
        return 'A'
    elif current == 7:
        return 'B'
    elif current == 8:
        return 'C'
    elif current == 'B':
        return 'D'

def right(current,letter):
    if current in [1,4,9,'C','D']:
        return current
    elif current in [2,3,5,6,7,8]:
        return current + 1
    elif current == 'A':
        return 'B'
    elif current == 'B':
        return 'C'


class TestAnswer(unittest.TestCase):
    code = list()
    digit = 5
    lines = input.split('\n')

    for line in lines:
        digit = get_position(digit, line)
        print(digit)
        code.append(digit)
    #print(code)


class TestKeypad(unittest.TestCase):

    def test_up(self):
        self.assertEqual(up(1, 'U'), 1)
        self.assertEqual(up(2, 'U'), 2)
        self.assertEqual(up(4, 'U'), 4)
        self.assertEqual(up(3, 'U'), 1)
        self.assertEqual(up(5, 'U'), 5)
        self.assertEqual(up(6, 'U'), 2)
        self.assertEqual(up(9, 'U'), 9)
        self.assertEqual(up('A', 'U'), 6)
        self.assertEqual(up('B', 'U'), 7)
        self.assertEqual(up('C', 'U'), 8)

    def test_left(self):
        self.assertEqual(left(5, 'L'), 5)
        self.assertEqual(left(7, 'L'), 6)
        self.assertEqual(left(9, 'L'), 8)
        self.assertEqual(left(1, 'L'), 1)
        self.assertEqual(left(4, 'L'), 3)
        self.assertEqual(left('B', 'L'), 'A')
        self.assertEqual(left('C', 'L'), 'B')

    def test_down(self):
        self.assertEqual(down(1, 'D'), 3)
        self.assertEqual(down(2, 'D'), 6)
        self.assertEqual(down(5, 'D'), 5)
        self.assertEqual(down(9, 'D'), 9)
        self.assertEqual(down(6, 'D'), 'A')
        self.assertEqual(down('A', 'D'), 'A')
        self.assertEqual(down('B', 'D'), 'D')

    def test_right(self):
        self.assertEqual(right(1, 'R'), 1)
        self.assertEqual(right(2, 'R'), 3)
        self.assertEqual(right(5, 'R'), 6)
        self.assertEqual(right(6, 'R'), 7)
        self.assertEqual(right(9, 'R'), 9)
        self.assertEqual(right('C', 'R'), 'C')
        self.assertEqual(right('A', 'R'), 'B')
        self.assertEqual(right('B', 'R'), 'C')

    def test_get_position(self):
        self.assertEqual(get_position(5, 'ULL'), 5)
        self.assertEqual(get_position(5, 'RRDDD'), 'D')
        self.assertEqual(get_position('D', 'LURDL'), 'B')
        self.assertEqual(get_position('B', 'UUUUD'), 3)


if __name__ == '__main__':
    unittest.main()