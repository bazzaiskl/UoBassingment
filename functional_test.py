from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        #self.browser.quit()
        print('not quit')
    
    def test_can_view_blog_post_in_detail(self):
        #stacey decides to go to my blog cos she wants to be cool like me (chad)
        self.browser.get('http://127.0.0.1:8000/post/new/')

        #she notices that the title says blog, which is what she wants
        self.assertIn('Blog',self.browser.title)
        

        #she checks to see im there are place to submit post
        header_text = self.browser.find_element_by_tag_name('h2').text
        #print(header_text)
        self.assertIn('New Post', header_text)

        #she writes in the boxes
        title_box = self.browser.find_element_by_name('title')
        blog_box = self.browser.find_element_by_name('text')
        save_button = self.browser.find_element_by_tag_name('button')
        title = 'the test to rule all tests'
        title_box.send_keys(title)
        blog_box.send_keys('thy test shall pass')
        save_button.click()
        time.sleep(2)

        new_post_title = self.browser.find_element_by_tag_name('h2')
        self.assertIn(title, new_post_title)

        self.fail('finish test')
if __name__ == '__main__':
    unittest.main(warnings='ignore')

