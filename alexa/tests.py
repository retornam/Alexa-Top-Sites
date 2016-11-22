import unittest
import coverage
from alexa import top_list


class alexaTest(unittest.TestCase):

    def test_top_list(self):
        a = top_list(10)
        self.assertEqual(len(a), 10, "top_list did not return 10 items")
        self.assertEqual(a[0][0], 1, "first item was not ranked #1")
        self.assertEqual(a[9][0], 10, 
        "tenth item was not ranked #10, rank of %d provided" % a[9][0])



if  __name__ == '__main__':
    unittest.main()