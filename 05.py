import unittest
import hashlib

id = 'abc'

class TestExample(unittest.TestCase):

    def test_answer(self):
        self.assertEqual(hashed('abc3231929'), '00000')


def hashed(num):
    ans = hashlib.md5(num.encode('utf-8')).hexdigest()
    print(ans)
    return(ans[:5])

if __name__ == '__main__':
    unittest.main()
