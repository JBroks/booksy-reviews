import unittest
import app

class TestApp(unittest.TestCase):
    """
    Test suit for app
    """

    def test_can_create_amazon_link(self):
        """
        Test to see if it creates a links correctly
        """
        link1 = app.generate_amazon_link('Once upon a time', 'John Smith')
        link2 = app.generate_amazon_link('Once upon & time', 'John Smith')
        link3 = app.generate_amazon_link('Once upon a time', 'John smith')
        self.assertEqual(link1, 'https://www.amazon.co.uk/s?k=Once+upon+a+time+John+Smith')
        self.assertEqual(link2, 'https://www.amazon.co.uk/s?k=Once+upon+and+time+John+Smith')
        self.assertNotEqual(link3, 'https://www.amazon.co.uk/s?k=Once+upon+a+time+John+Smith')

if __name__ == '__main__':
    unittest.main()