import unittest
import Lab_3

class test_Lab_3(unittest.TestCase):
    def test_conditionals(self):
        self.assertEqual(Lab_3.conditionals(3), '3: Odd.')
        self.assertEqual(Lab_3.conditionals(2), 'Even and less than 25.')
        self.assertEqual(Lab_3.conditionals(24), 'Even and less than 25.')
        self.assertEqual(Lab_3.conditionals(25), '25: Odd.')
        self.assertEqual(Lab_3.conditionals(26), 'Even.')
        self.assertEqual(Lab_3.conditionals(59), '59: Odd.')
        self.assertEqual(Lab_3.conditionals(60), 'Even.')
        self.assertEqual(Lab_3.conditionals(62), '62: Even.')
        self.assertEqual(Lab_3.conditionals(63), 'Odd and over 60.')
    
if __name__ == '__main__':
    unittest.main()
