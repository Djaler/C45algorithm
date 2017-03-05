import json
import unittest

import utils


class TestDataMining(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('table.json') as f:
            cls.table = json.loads(f.read())
    
    def test_is_all_equals(self):
        testlist = ['yes', 'yes', 'yes', 'yes']
        self.assertTrue(utils.is_all_equals(testlist))
        testlist = ['yes', 'no', 'yes', 'yes']
        self.assertFalse(utils.is_all_equals(testlist))
    
    def test_get_subtables(self):
        expected = [
            {'result': ['yes', 'no'],
             'arg1': ['left', 'left'],
             'arg2': ['down', 'up'],
             'arg3': ['no', 'yes'],
             },
            {'result': ['yes', 'no'],
             'arg1': ['right', 'right'],
             'arg2': ['down', 'down'],
             'arg3': ['yes', 'no'],
             }]
        self.assertEqual(utils.get_subtables(self.table, 'arg1'), expected)


if __name__ == '__main__':
    unittest.main()
