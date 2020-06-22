import unittest
from selenium.webdriver.support.ui import WebDriverWait
import time
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
        self.driver.find_element_by_css_selector("[href='/databas']").click()
        #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='open-button']//font//font"))).click()
        #self.driver.find_element_by_xpath("//ul[@class='nav navbar-nav mai-top-nav']//a[@class='nav-link'][contains(text(),'Aktivitetsdatabas')]").click()
        self.driver.find_element_by_name("ad_cn").send_keys("urmila")
        self.driver.find_element_by_name("ad_pn").send_keys("199504020083")
        self.driver.find_element_by_name("mn").send_keys("0725655744")
        self.driver.find_element_by_name("ad_ei").send_keys("urmila7842@gmail.com")
        self.driver.find_element_by_name("st").send_keys("nykarlabygatan 114")
        self.driver.find_element_by_name("zc").send_keys("16442")
        self.driver.find_element_by_name("cy").send_keys("stockholm")
        self.driver.find_element_by_name("ad_wd").send_keys("urmilagkjhlhg")
        self.driver.find_element_by_name("ad_agt").click()
        self.driver.find_element_by_xpath("//input[@placeholder='Sök och lägg till ny artikel']").send_keys("hjjhj")
        self.driver.find_element_by_name("pdkt_na").send_keys("aaaa")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#updateProducts"))).click()
        #self.driver.find_element_by_css_selector("#updateProducts").click()
        #wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/divåå4]/div[12]/form[1]/table[1]/tbody[1]/tr[2]/td[14]/select[1]/option[47]"))).click()
        #self.driver.find_element_by_xpath("//tr[@class='new active border product-border']//option[contains(text(),'Kylmästarna i Stockholm AB')]").click()
        #self.driver.find_element_by_name("newData").click()
        #wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='chooseCustomer']"))).click()
        #self.driver.find_element_by_xpath("//button[@class='btn btn-danger btn-sm far fa-times']").click()
        #self.driver.find_element_by_css_selector("[type='checkbox']").click()
        #self.driver.find_element_by_xpath("/html/body/div[4]/div[29]/div/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/label/input").click()
        #self.driver.find_element_by_css_selector("#doubleHandling > div > div > div.modal-footer.d-flex > div:nth-child(2) > button").click()"""
    def test_schedule(self):
        self.driver.find_element_by_partial_link_text("Schema").click()
        select = Select(self.driver.find_element_by_name('users[]'))

        for index in range(len(select.options)):
            select = Select(self.driver.find_element_by_name('users[]'))
            select.select_by_index(20)
        wait = WebDriverWait(self.driver, 30)
        self.driver.find_element_by_partial_link_text("Föräldrarled").click()
        #wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "prakt"))).click()
        self.driver.find_element_by_css_selector("#invoiceRecipientTogglerButton").click()
        #wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#invoiceRecipientTogglerButton"))).click()
        self.driver.find_element_by_xpath("//input[@name='invoice_for_company']").click()
        self.driver.find_element_by_name("for_company_address").click()
        self.driver.find_element_by_id("createNewInvoice").click()
        self.driver.find_element_by_xpath("//tr[contains(@class,'un-sortable new')]//input[contains(@placeholder,'Sök och lägg till artikel')]").send_keys("A")
        self.driver.find_element_by_xpath("//div[contains(text(),'Daikin Vibration #3656')]").click()
        #self.driver.find_element_by_css_selector(".mt-3").click()
        #self.driver.find_element_by_xpath("//div[contains(@class,'row no-gutters my-2 invoice-table-container p-0')]//div[2]//div[1]//div[1]//span[1]//label[1]").click()
        #wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[4]/div[9]/div[3]/div[1]/div[1]/div[1]/form[3]/div[3]/div[1]/div[2]/div[3]/div[2]/div[133]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[1]/div[1]/span[1]/label[1]"))).click()
        #self.driver.find_element_by_xpath("/html[1]/body[1]/div[4]/div[9]/div[3]/div[1]/div[1]/div[1]/form[3]/div[3]/div[1]/div[2]/div[3]/div[2]/div[133]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[3]/div[1]/div[1]/span[1]/label[1]").click()
        self.driver.find_element_by_xpath("//div[contains(@class,'col-md-2 p-1')]//div[3]//div[1]//div[1]//span[1]//label[1]").click()
        #self.driver.find_element_by_xpath("//div[contains(@class,'col-md-2 p-1')]//div[4]//div[1]//div[1]//span[1]//label[1]").click()
        original_price = self.driver.find_element_by_xpath("//div[70]//div[1]//div[2]//div[1]//div[1]//button[1]//div[2]//span[2]").text
        print(original_price)
        a = original_price.split()
        d = a[0]+a[1]
        #print(d.replace(',','.', 1))
        op = d.replace(',','.', 1)
        print(op)
        real_price = self.driver.find_element_by_xpath("//div[@class='row no-gutters d-flex border-top border-dark invoice-prices']//div[1]//div[1]//span[2]").text
        b = real_price.split()
        e = b[0] + b[1]
        rp = d.replace(',', '.', 1)
        print(rp)

        add = float(op) + float(rp)*25/100
        print(add)
        self.assertEqual(rp, op)
        #Add = str(original_price) + str(discount_price)

        #print("Difference is:" + difference)"""

    @classmethod
    def earDownClass(self):
        self.driver.close()
        self.driver.quit()