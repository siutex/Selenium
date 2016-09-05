from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest

class PageLayout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.lasy.gov.pl/")
        confirm = WebDriverWait(self.driver,10).until(lambda driver: self.driver.find_element_by_css_selector("#impliedsubmit"))
        confirm.click()

        forests = WebDriverWait(self.driver,10).until(lambda driver: self.driver.find_element_by_css_selector("ul[id='menu_top'] >.skin_standard :nth-child(1)"))
        forests.click()

    def find_id(self):
        try:
            driver = self.driver
            driver.find_element_by_id('logo')
            print('Test Pass: ID found')
        except Exception as e:
            print("Exception found", format(e))
        #try:
          #  driver = self.driver
         #   driver.find_element_by_id('main')
         #   print('Test Pass: ID found')
        #except Exception as e:
         #   print("Exception found", format(e))



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()