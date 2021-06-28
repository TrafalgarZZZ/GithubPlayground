import unittest
import main

class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(main.say(), "hello git.")
    def test_say(self):
        self.assertEqual(main.bye(), "bye git.")
    
if __name__ == '__main__':
    unittest.main()