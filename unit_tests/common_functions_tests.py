import unittest
from common_tools.common_functions import title_case


class CommonFunctionsTest(unittest.TestCase):

    def test_title_case(self):
        self.assertEquals('Testing', title_case('testing'))
        self.assertEquals('Testing', title_case('Testing'))
        self.assertEquals('Testing', title_case('TESTING'))
        self.assertEquals('This Is A Test', title_case('this is a test'))


if __name__ == '__main__':
    unittest.main()
