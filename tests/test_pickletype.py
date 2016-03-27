import unittest

import pickletype as pt


class TestPickleType(unittest.TestCase):

    def test_int(self):
        self.assertEqual(pt.get_type(1), int)

    def test_str(self):
        self.assertEqual(pt.get_type('x'), str)

    def test_empty_list(self):
        self.assertEqual(pt.get_type([]), [])

    def test_int_list(self):
        self.assertEqual(pt.get_type([1]), [int])

    def test_long_int_list(self):
        self.assertEqual(pt.get_type([1, 2, 3]), pt.List(int))

    def test_str_list_list(self):
        self.assertEqual(pt.get_type([['x']]), [[str]])

    def test_empty_tuple(self):
        self.assertEqual(pt.get_type(()), ())

    def test_int_tuple(self):
        self.assertEqual(pt.get_type((1,)), (int,))

    def test_str_tuple_tuple(self):
        self.assertEqual(pt.get_type(((1,),)), ((int,),))

    def test_empty_dict(self):
        self.assertEqual(pt.get_type({}), dict)

    def test_dict(self):
        x = {'x': 1, 'y': 2}
        self.assertEqual(pt.get_type(x), pt.Dict(str, int))
