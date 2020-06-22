import unittest
import time
import selenium.webdriver.support.ui as ui
#import fileone
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
# declare variable to store the URL to be visited
class AdderTest (unittest.TestCase):

    @classmethod
    def setUpClass(self):
       self.driver = webdriver.Chrome("C:/Users/urmil/PycharmProjects/scratches/chromedriver")
       #base_url= "https://test.arjith.net/login"
       self.driver.get("HTTP://NEWTOURS.DEMOAUT.COM/")
       self.driver.maximize_window()
       self.driver.implicitly_wait(1)


    def test_Add_User(self):
       self.driver.find_element_by_css_selector("[name='userName']").send_keys("urmilaJyothula")
       self.driver.find_element_by_name("password").send_keys("meghana@")
       self.driver.find_element_by_name("login").click()
       self.driver.find_element_by_xpath("//body//b//input[2]").click()
       self.driver.find_element_by_xpath("//select[@name='passCount']//option[contains(text(),'2')]").click()
       self.driver.find_element_by_xpath("//select[@name='fromPort']//option[contains(text(),'London')]").click()
       self.driver.find_element_by_xpath("//select[@name='fromMonth']//option[contains(text(),'April')]").click()
       self.driver.find_element_by_xpath("//select[@name='fromDay']//option[2]").click()
       self.driver.find_element_by_xpath("//select[@name='toPort']//option[contains(text(),'Zurich')]").click()
       self.driver.find_element_by_xpath("//select[@name='toDay']//option[contains(text(),'10')]").click()
       self.driver.find_element_by_css_selector("[value='Business']").click()
       self.driver.find_element_by_xpath("//option[contains(text(),'Unified Airlines')]").click()
       self.driver.execute_script("window.open('http://thedemosite.co.uk/');")
       self.driver.switch_to.window(window_name=self.driver.window_handles[0])
    """def test_login_valid(self):
        self.driver.get("http://thedemosite.co.uk/login.php")
        self.driver.find_element_by_name("username").send_keys("test")
        self.driver.find_element_by_name("password").send_keys("test")
        self.driver.find_element_by_name("FormsButton2").click()
        e = self.driver.find_element_by_xpath("//b[contains(text(),'**Failed Login**')]")
        print(e.get_attribute('innerText'))"""


    @classmethod
    def earDownClass(self):
        self.driver.close()
        self.driver.quit()
