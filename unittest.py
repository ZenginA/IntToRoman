import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_intToRoman(self):
        
        test_cases = [
            (3, "III"),
            (4, "IV"),
            (9, "IX"),
            (58, "LVIII"),
            (1994, "MCMXCIV"),
            
        ]

        for num, expected_result in test_cases:
            with self.subTest(num=num, expected_result=expected_result):
                result = self.solution.intToRoman(num)
                self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
