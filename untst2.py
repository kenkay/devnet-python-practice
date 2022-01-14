from types import NoneType
import unittest

from clifnh import flow, downProc

z = flow.passDown()

y = downProc.prPoc()

class test_fx(unittest.TestCase):
    def test_ret(self):
        self.assertIsNot(z,y)

if __name__ == '__main__':
    unittest.main()