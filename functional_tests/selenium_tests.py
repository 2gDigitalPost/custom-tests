import unittest
import time

from selenium import webdriver

from ConfigParser import SafeConfigParser


# TODO: Come up with a better name than 'WebTest'...
class WebTest(unittest.TestCase):
    """
    Selenium based tests to make sure the front end looks and acts the way it should.

    A work in progress (obviously)
    """

    def setUp(self):

        # TODO: Maybe switch to Chrome?
        self.browser = webdriver.Firefox()

        parser = SafeConfigParser()
        parser.read('config.ini')

        self.target_website = parser.get('url', 'test')

        username = parser.get('login', 'username')
        password = parser.get('login', 'password')

        self.login(username, password)

    def tearDown(self):
        self.browser.close()

    def login(self, username, password):
        self.browser.get(self.target_website)

        username_field = self.browser.find_element_by_name('login')
        password_field = self.browser.find_element_by_name('password')
        submit_field = self.browser.find_element_by_name('Submit')

        username_field.send_keys(username)
        password_field.send_keys(password)

        submit_field.submit()

    def test_hot_list(self):
        self.browser.get(self.target_website)

        # If you don't sleep for a few seconds, the page won't load fast enough and the test will fail
        time.sleep(5)

        # Assert that the header tab contains 'Welcome!'
        # TODO: Remove this test, it's just for my initial setup and really isn't very interesting
        hot_list_table_header = self.browser.find_element_by_class_name('spt_tab_header_label')
        self.assertIn('Welcome!', hot_list_table_header.text)

    # TODO: More tests!


if __name__ == '__main__':
    unittest.main()
