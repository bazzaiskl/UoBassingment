from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def test_can_view_blog_post_in_detail(self):
        #stacey decides to go to my blog cos she wants to be cool like me (chad)
        self.browser.get('http://127.0.0.1:8000')

        #she notices that the title says blog, which is what she wants
        self.assertIn('blog',self.browser.title)
        self.fail('Finish Test!')

        #she looks to see if there are submited blog posts

        #then she decides to click on one to see it bigger

        #she likes the post cos it made her cool

if __name__ == '__main__':
    unittest.main(warnings='ignore')

