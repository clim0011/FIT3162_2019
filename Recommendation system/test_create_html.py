import unittest
from create_html import create_html

class Test(unittest.TestCase):
    def test_create_html(self):
        self.assertEqual(create_html("Hotel_Austria_Business.txt","Austria_Business.csv","Austria"),[1839, 1840, 1842])

if __name__ == '__main__':
    unittest.main()
