from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import unittest

class MainPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.delete_all_cookies()
        self.driver.get("http://www.lasy.gov.pl/")
        confirm = WebDriverWait(self.driver,10).until(lambda driver: self.driver.find_element_by_css_selector("#impliedsubmit"))
        confirm.click()
        assert "Lasy" in self.driver.title
        forests = WebDriverWait(self.driver,10).until(lambda driver: self.driver.find_element_by_css_selector("ul[id='menu_top'] >.skin_standard :nth-child(1)"))
        forests.click()




    def test_Toolbar_nasze_lasy(self):
        driver = self.driver
        menu_css = "div#bg_menu"
        toolbar_id = "ul[id='menu']"
        nasze_lasy_css = "#content_wrap li#portaltab-nasze-lasy.plain"
        polskie_lasy_css ="#content_wrap li#portaltab-nasze-lasy.plain>ul>li:first-of-type>a"
        lesn_komp="#content_wrap li#portaltab-nasze-lasy.plain>ul>li:nth-of-type(1)>a"

        #menu = WebDriverWait(driver,15).until(lambda driver: driver.find_element_by_css_selector(menu_css))
        #nasze_lasy = WebDriverWait(driver,15).until(lambda driver: driver.find_element_by_css_selector(nasze_lasy_css))
        #polskie_lasy = driver.find_element_by_css_selector(polskie_lasy_css)
        driver.implicitly_wait(2)  # seconds
        lasyy = driver.find_element_by_css_selector(nasze_lasy_css)
        lasyy.click()
        driver.implicitly_wait(2)  # seconds
        #self.assertRegex(lasyy.text, "NASZE LASY")
        try:
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, polskie_lasy_css))
            )
        finally:
            #driver.implicitly_wait(3)  # seconds
            element.click()
        title= driver.current_url
        driver.implicitly_wait(2)  # seconds
        self.assertEqual(title,"http://www.lasy.gov.pl/nasze-lasy/polskie-lasy","Current url correct")
        driver.implicitly_wait(2)  # seconds
        driver.back()
        main_url ="http://www.lasy.gov.pl/"
        self.assertEqual(main_url,"http://www.lasy.gov.pl/", "Back to main page")
        driver.implicitly_wait(2)  # seconds
        lasyy2 = driver.find_element_by_css_selector(nasze_lasy_css)
        lasyy2.click()
        #self.assertRegex(lasyy.text, "NASZE LASY")
        try:
            element2 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, lesn_komp))
            )
        finally:
            driver.implicitly_wait(3)  # seconds
            element2.click()
        title2 = driver.current_url
        driver.implicitly_wait(2)  # seconds
       # self.assertEqual("http://www.lasy.gov.pl/nasze-lasy/lesne-kompleksy-promocyjne",title2, "Current url correct")
        driver.implicitly_wait(2)  # seconds
        driver.back()


    def test_toolbar_nasza_praca(self):
        driver = self.driver
        nasza_praca_css="#content_wrap ul>li[id='portaltab-nasza-praca']>a"
        pgl_css="#content_wrap ul>li[id='portaltab-nasza-praca']>ul[class='submenu']>li:nth-of-type(1)>a"
        opgl_css="#content_wrap ul>li[id='portaltab-nasza-praca']>ul[class='submenu']>li:nth-of-type(1)>ul li:first-of-type>a"
        driver.implicitly_wait(2)  # seconds
        nasza_praca = driver.find_element_by_css_selector(nasza_praca_css)
        nasza_praca.click()
        self.assertRegex(nasza_praca.text, "NASZA PRACA")
        pgl = driver.find_element_by_css_selector(pgl_css)
        driver.implicitly_wait(2)  # seconds
        pgl.click()
        opgl = driver.find_element_by_css_selector(opgl_css)
        driver.implicitly_wait(3)
        opgl.click()
        pgl_url = "http://www.lasy.gov.pl/nasza-praca/pgl-lasy-panstwowe"
        driver.implicitly_wait(2)  # seconds
#        self.assertEqual(pgl_url, driver.current_url,"pgl url error")
        action_chains = ActionChains(driver)
        zasoby_le_css = "#content_wrap ul>li[id='portaltab-nasza-praca']>ul[class='submenu']>li:nth-of-type(2)>a"
        zasoby_le = WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_css_selector(zasoby_le_css))
        zasoby_le.click()
        driver.implicitly_wait(2)  # seconds
        zasoby_url = "http://www.lasy.gov.pl/nasza-praca/zasoby-lesne"
        self.assertEqual(zasoby_url, driver.current_url, "pgl url error")

    def search_bar(self):
        driver = self.driver
        search_b_css = "#content_wrap #main #bg_menu .container >div>form .btn_search>input"
        search_input_css = "#content_wrap #main #bg_menu .container >div>form .box_input_text>input"
        action_chains = ActionChains(driver)
        action_chains.move_to_element(search_b_css).click_and_hold(search_b_css).click(search_input_css).perform()



    def test_find_logo_location(self):
        driver = self.driver
        element =  driver.find_element_by_id('logo')
        location =  element.location
        size = element.location
        print(location)
        print(size)


    def tearDown(self):
        self.driver.quit()

    #def tearDownClass(self):
       # self.driver.quit()

if __name__ == '__main__':
    unittest.main()


