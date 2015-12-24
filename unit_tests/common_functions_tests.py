import unittest
from common_tools.common_functions import abbreviate_text, title_case


class CommonFunctionsTest(unittest.TestCase):

    def test_title_case(self):
        self.assertEquals('Testing', title_case('testing'))
        self.assertEquals('Testing', title_case('Testing'))
        self.assertEquals('Testing', title_case('TESTING'))
        self.assertEquals('This Is A Test', title_case('this is a test'))

    def test_abbreviate_text(self):
        self.assertEquals('Test...', abbreviate_text('Testing this function.', 4))
        self.assertEquals('Testing...', abbreviate_text('Testing this function.', 8))
        self.assertEquals('Testing', abbreviate_text('Testing', 10))
        self.assertEquals('This is my...', abbreviate_text('This is my example', 10))


if __name__ == '__main__':
    unittest.main()
