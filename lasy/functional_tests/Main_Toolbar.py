from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
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
        try:
            zasoby_le = WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_css_selector(zasoby_le_css))
            zasoby_le.click()
        except TimeoutException:
            print("Zasoby page unavaible timeout")

        driver.implicitly_wait(2)  # seconds
        zasoby_url = "http://90lat.lasy.gov.pl/#0"
        self.assertEqual(zasoby_url, driver.current_url, "pgl url error")
        polski_css = "div[id='loadingScreen']>div>div[id='loading-progress']>a[href*='pl']"
        driver.implicitly_wait(2)
        polski =  driver.find_element_by_css_selector(polski_css)
        polski.click()


    def test_search_bar(self):
        driver = self.driver
        search_b_css = "#content_wrap #main #bg_menu .container >div>form .btn_search>input"
        search_input_css = "#content_wrap #main #bg_menu .container >div>form .box_input_text>input"
        action_chains = ActionChains(driver)
        search_b = driver.find_element_by_css_selector(search_b_css)
        search_input = driver.find_element_by_css_selector(search_input_css)
       # driver.save_screenshot('screenshot.png')
        driver.implicitly_wait(2)  # seconds
        action_chains.move_to_element(search_b).click(search_b).move_to_element(search_input).perform()
        driver.implicitly_wait(2)  # seconds
        search_input.send_keys("drewno")
        drewno_url = "http://www.lasy.gov.pl/@@search?q=drewno"
        search_b.click()
        self.assertEqual(driver.current_url, drewno_url)
        driver.back()
        lasy_url = "http://www.lasy.gov.pl/"
        self.assertEqual(lasy_url, driver.current_url)

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


