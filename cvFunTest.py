from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class creationTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_add_info(self):
        #stacey wants to make an online cv cos she needs a job (broke af)
        #she goes to a website to start creating
        self.browser.get('http://127.0.0.1:8000/cv')

        #she sees and clicks on a new cv button
        new_cv = self.browser.find_element_by_class_name('new_cv_button').text
        self.assertIn('new', new_cv)


        #she logs in so she knows its her cv shes making

        #she sees a box and enters her personal details,address, email, phone number

        #she sees an objectives box and enters her goal

        #she adds a list of skills and personal qualities

        #she creates a new experience section

        #it asks and she gives a job title, company, years active and a decription of responabilites

        #she adds a list of interests

        #she creates a new education 

        #it asks and she adds name of program, inisition of programme, adds years active and a description

        #she sees a box to add a list of her school and university involvement

        #she sees a box to add a list of awards

        #she creates a new reference

        #she adds name, title, their position, their compamny and a phone number/ email/ other contact
        

if __name__ == '__main__':
    unittest.main(warnings='ignore')