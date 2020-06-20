from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class creationTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        #this try/excpets checks for the error page and doesnt close it if its there
        try:
            errorPage = self.browser.find_element_by_id('summary')
            print("no close")
        except:
            #self.browser.quit()
            pass

    def test_can_add_info_not_logged_in(self):
        #stacey wants to make an online cv cos she needs a job (broke af)
        #she goes to a website to start creating
        self.browser.get('http://127.0.0.1:8000/cv')

        #she sees and clicks on a new cv button
        new_cv = self.browser.find_element_by_class_name('new_cv_button').text
        self.assertIn('new', new_cv)
        new_cv_button = self.browser.find_element_by_class_name('new_cv_button')
        new_cv_button.click()
        time.sleep(1)
#-- new page --#
       




        #she logs in so she knows its her cv shes making
        self.assertIn('Login',self.browser.title)
        username = self.browser.find_element_by_name('username')
        password = self.browser.find_element_by_name('password')

        username.send_keys('horatioPistachio')
        password.send_keys('boysarebackintown') #this is just for test, better luck next time
        password.send_keys(Keys.ENTER)
        time.sleep(1)
#-- new page --#        

        #she sees a box and enters her personal details,address, name ,phone number
        #email should already be there from login
        self.assertIn('New CV', self.browser.find_element_by_tag_name('h2').text)

        name = self.browser.find_element_by_name('name')
        address = self.browser.find_element_by_name('address')   #probs should improve for subburb, street thingo   
        phone_number = self.browser.find_element_by_name('phone_number')
        email = self.browser.find_element_by_name('email')


        #she sees an objectives box and enters her goal
        objective = self.browser.find_element_by_name('objective')

        #she adds a list of skills and personal qualities
        skills = self.browser.find_element_by_name('skills') #-- update to a list style, rather that text field-- maybe hit enter between things


        #she adds a list of interests
        interests = self.browser.find_element_by_name('interests')


        #she fills out the form
        name.send_keys("stacey shortcakes")
        address.send_keys("23 bakers avenue, cakelton")
        phone_number.send_keys("0385934811")
        email.send_keys("longcakes@gmail.com")
        objective.send_keys("I would like to become the best baker I can be. I hope you can teach me the art")
        skills.send_keys("baking\neating\nthe double wisk technique\nallround good las")
        interests.send_keys("baking\neggs\nfootball\nshoe making")

       
        #she clicks on submit personal details
        
#-- new page --#
        # she sees shes at the experience part
        self.assertIn('Experience', self.browser.find_element_by_id('experience').text)

        #it asks and she gives a job title, company, years active and a decription of responabilites
        job_title = self.browser.find_element_by_name('job_title')
        company = self.browser.find_element_by_name('company')
        start_year = self.browser.find_element_by_name('start_year')
        end_year = self.browser.find_element_by_name('end_year')
        job_description = self.browser.find_element_by_name('job_description')

        job_title.send_keys('pie eater')
        company.send_keys('pie co')
        start_year.send_keys('1/1/2020')
        end_year.send_keys('2/1/2020')
        job_description.send_keys('i didnt do alot')



        #she has the option to add another experience

        #she clicks add another

        #its askes for stuff and she fills it out
        
#-- new page --#
        #she creates a new education 
        self.assertIn('Education', self.browser.find_element_by_id('education').text)
        #it asks and she adds name of program, inisition of programme, adds years active and a description
        program = self.browser.find_element_by_name('program')
        insitution = self.browser.find_element_by_name('insitution')
        start_year_ed = self.browser.find_element_by_name('start_year_ed')
        end_year_ed = self.browser.find_element_by_name('end_year_ed')
        education_description = self.browser.find_element_by_name('education_description')

        program.send_keys('masters of cake making')
        insitution.send_keys('grandmas house')
        start_year_ed.send_keys('1/1/2019')
        end_year_ed.send_keys('1/1/2020')
        education_description.send_keys('they let us bake a cake AND eat it too')

        #she sees a box to add a list of her school and university involvement
        involvement  = self.browser.find_element_by_name('involvement')
        involvement.send_keys('granny house comp 2020\neating comp\nwake and bake club')

        #she sees a box to add a list of awards
        awards = self.browser.find_element_by_name('awards')
        awards.send_keys('grannys house comp 2020 3rd place\nbest mud cake\ncoolest flambe')
        
        

#-- new page --#
        #she creates a new reference
        ref_name = self.browser.find_element_by_name('ref_name')
        ref_position = self.browser.find_element_by_name('ref_position')
        ref_company = self.browser.find_element_by_name('ref_company')
        ref_contact = self.browser.find_element_by_name('ref_contact')
        #she adds name, title, their position, their compamny and a phone number/ email/ other contact
        ref_name.send_keys('granny')
        ref_position.send_keys('chief')
        ref_company.send_keys('granny wake n bake')
        ref_contact.send_keys('oldNan@wake2Bake.com')
        #she submits the cv

        submitPersonalDetail = self.browser.find_element_by_tag_name('button')
        submitPersonalDetail.click()
        time.sleep(3)
        #she is able to see a nicely formated cv in cv homepage
        self.assertIn(name, self.browser.find_element_by_tag('h2').text)

        

    

if __name__ == '__main__':
    unittest.main(warnings='ignore')