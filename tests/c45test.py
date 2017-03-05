import json
import unittest

from c45 import gain, info, info_x


class TestC45(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('table.json') as f:
            cls.table = json.loads(f.read())
    
    def test_info(self):
        self.assertEqual(info(self.table, 'result'), 1)
    
    def test_info_x(self):
        self.assertEqual(info_x(self.table, 'arg1', 'result'), 1)
    
    def test_gain(self):
        self.assertEqual(gain(self.table, 'arg1', 'result'), 0)


if __name__ == '__main__':
    unittest.main()
