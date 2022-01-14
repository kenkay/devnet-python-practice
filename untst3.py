import unittest

from clifnh2 import flow, downProc

x = print(flow.passDown())

y = downProc.prPoc()

class test_fx(unittest.TestCase):
    def same(self):
        self.assertAlmostEqual(x,y)

if __name__ == '__main__':
    unittest.main()