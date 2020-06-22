from selenium.webdriver.support.ui import WebDriverWait
import fileeight
import time
import unittest
#from practicee import AddTest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
#import fileone
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
# declare variable to store the URL to be visited
class JackTest (unittest.TestCase):

    @classmethod
    def setUpClass(self):
       self.driver = webdriver.Chrome("C:/Users/urmil/PycharmProjects/scratches/chromedriver")
       #base_url= "https://test.arjith.net/login"
       self.driver.get("https://iva.arjith.net/databas")
       self.driver.maximize_window()
       self.driver.implicitly_wait(1)


    def test_login_User(self):
        wait = WebDriverWait(self.driver, 30)
        a=self.driver.find_element_by_css_selector("#emailId").send_keys("urmila7842@gmail.com")
        #wait.until(EC.element_to_be_clickable((By.ID, "emailId"))).send_keys("arjith@kylslaget.se")
        wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys("ilovearjith")
        #wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='loginButton']"))).click()
        self.driver.find_element_by_xpath("//i[@class='fal fa-sign-in-alt']").click()
        self.driver.find_element_by_css_selector("#sideNavigationButton").click()
        self.driver.find_element_by_partial_link_text("Uppföljning").click()
        self.driver.find_element_by_xpath("//div[@class='d-md-flex p-0 new']//select[@name='f_c']//option[1]").click()
        self.driver.find_element_by_xpath("//div[@class='d-md-flex p-0 new']//select[@name='f_s']//option[5]").click()
        self.driver.find_element_by_xpath("//select[@name='f_p']//option[contains(text(),'Hög')]").click()
        self.driver.find_element_by_name("f_m").send_keys("enter something", Keys.ENTER)
        self.driver.find_element_by_css_selector(".fa-chevron-circle-down").click()
        self.driver.find_element_by_partial_link_text("Kund").click()
        #self.driver.find_element_by_name("c_n").send_keys("Jonas Hög")
        self.driver.find_element_by_name("c_p_n").send_keys("abc")
        self.driver.find_element_by_name('c_p_n').clear()
        self.driver.find_element_by_name("c_p_n").send_keys("19950402")
        self.driver.find_element_by_xpath("//option[contains(text(),'Pansonic Nordic')]").click()
        self.driver.find_element_by_name("c_c").send_keys("344556667777")
        self.driver.find_element_by_name("c_c").clear()
        self.driver.find_element_by_name("c_c").send_keys("typing for testing")
        self.driver.find_element_by_xpath("//div[@class='row no-gutters my-2']//div[2]//div[1]//select[1]//option[5]").click()
        self.driver.find_element_by_name("cp_m_pn").send_keys("urmila")
        page_text = self.driver.find_element_by_xpath("//div[@class ='flex-fill p-1 w17'] // span[@ class ='form-control-placeholder font-weight-bold invalid-feedback error-label'][contains(text(), 'Ange ett giltigt nummer')]").text
        expected_results = "Ange ett giltigt nummer"
        assert page_text == expected_results, "exception"
        self.driver.find_element_by_name("cp_m_pn").clear()
        self.driver.find_element_by_name("cp_m_pn").send_keys("70226547777")
        self.driver.find_element_by_name("cp_m_ft").send_keys("abcdef")
        self.driver.find_element_by_xpath("//div[@class='row no-gutters my-1 ks-child-customer-containers']//div[2]//div[2]//div[1]//div[2]//div[4]//select[1]//option[2]").click()
        self.driver.find_element_by_xpath("//div[@class='row no-gutters my-2']//div[2]//div[5]//select[1]//option[2]").click()
        self.driver.find_element_by_xpath("//div[@class='flex-fill p-1 w14']//button[@name='newData']").click()
        self.driver.find_element_by_xpath("//div[3]//div[2]//div[1]//div[2]//div[1]//select[1]//option[2]").click()
        self.driver.find_element_by_name("cp_e_e").send_keys("jcc,zc")
        mail_text = "Ange ett giltigt E-post"
        expected_mail = self.driver.find_element_by_xpath(
            "//span[@class='form-control-placeholder font-weight-bold invalid-feedback error-label']").text
        assert mail_text == expected_mail, "exception"
        self.driver.find_element_by_name("cp_e_e").clear()
        self.driver.find_element_by_name("cp_e_e").send_keys("urmi@gmail.com")
        self.driver.find_element_by_name("cp_e_ft").send_keys("123abc")
        self.driver.find_element_by_xpath("//div[3]//div[2]//div[1]//div[2]//div[4]//select[1]//option[2]").click()
        self.driver.find_element_by_xpath("//div[@class='flex-fill p-1 w8']//button[@name='newData']").click()
        self.driver.find_element_by_xpath("//div[@class='flex-fill p-1 w8']//button[@class='btn btn-sm btn-secondary p-2 fal fa-trash-alt trash-button']").click()
        self.driver.find_element_by_name("cp_a_n").send_keys("76Abb")
        self.driver.find_element_by_name("cp_a_p").send_keys("abc")
        self.driver.find_element_by_name("cp_a_p").clear()
        self.driver.find_element_by_name("cp_a_p").send_keys("123")
        self.driver.find_element_by_xpath("//select[@name='cp_a_vt']//option[contains(text(),'Företag omvänd moms')]").click()
        self.driver.find_element_by_xpath("//input[@placeholder='Sök för adress']").send_keys("kista, 88887")
        self.driver.find_element_by_xpath("//input[@placeholder='Sök för postnummer']").send_keys("1986")
        self.driver.find_element_by_xpath("//input[@placeholder='Sök och lägg till ort']").send_keys("cy")
        self.driver.find_element_by_xpath("//select[@name='cp_a_at']//option[contains(text(),'Kolonistuga')]").click()
        self.driver.find_element_by_name("cp_a_ft").send_keys("hjgjhg")
        self.driver.find_element_by_name("cp_a_pg").send_keys("cvcv")
        self.driver.find_element_by_name("cp_a_ghn").send_keys("gdhd")
        self.driver.find_element_by_xpath("//div[@class='flex-fill p-1 w4']//button[@name='newData']").click()


    if __name__ == '__main__':
       unittest.main()
       fileeight.test_schedule()