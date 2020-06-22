import unittest
import fileeight
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
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
       self.driver.get("https://test.arjith.net/aktivitet/id/72590")
       self.driver.maximize_window()
       self.driver.implicitly_wait(1)


    def test_Add_Users(self):
        wait = WebDriverWait(self.driver, 30)
        self.driver.find_element_by_xpath("//input[@placeholder='Sök och lägg till artikel']").send_keys("A")
        #wait.until(EC.element_to_be_clickable((By.ID, "emailId"))).send_keys("arjith@kylslaget.se")
        wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys("ilovearjith")
        #wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='fal fa-sign-in-alt']"))).click()
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
        wait.until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[4]/div[12]/form[1]/table[1]/tbody[1]/tr[2]/td[14]/select[1]/option[47]"))).click()
        #self.driver.find_element_by_xpath("//tr[@class='new active border product-border']//option[contains(text(),'Kylmästarna i Stockholm AB')]").click()
        self.driver.find_element_by_name("newData").click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='chooseCustomer']"))).click()
        self.driver.find_element_by_xpath("//button[@class='btn btn-danger btn-sm far fa-times']").click()
        #self.driver.find_element_by_css_selector("[type='checkbox']").click()
        #self.driver.find_element_by_xpath("/html/body/div[4]/div[29]/div/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/label/input").click()
        #self.driver.find_element_by_css_selector("#doubleHandling > div > div > div.modal-footer.d-flex > div:nth-child(2) > button").click()
    def test_schedule(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='nav-link'][contains(text(),'Schema')]"))).click()
        select = Select(self.driver.find_element_by_name('users[]'))

        for index in range(len(select.options)):
            select = Select(self.driver.find_element_by_name('users[]'))
            select.select_by_index(20)
        wait = WebDriverWait(self.driver, 30)
        self.driver.find_element_by_partial_link_text("prakt").click()
        #wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "prakt"))).click()
        self.driver.find_element_by_css_selector("#invoiceRecipientTogglerButton").click()
        #wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#invoiceRecipientTogglerButton"))).click()
        self.driver.find_element_by_xpath("//input[contains(@name,'INVOICE_FOR_COMPANY')]").click()
        self.driver.find_element_by_name("for_company_address").click()
        self.driver.find_element_by_id("createNewInvoice").click()
        self.driver.find_element_by_xpath("//tr[contains(@class,'un-sortable new')]//input[contains(@placeholder,'Sök och lägg till artikel')]").send_keys("A")
        #wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".switch-button"))).click()
        userName = self.driver.find_element_by_xpath(".switch-button")
        self.driver.execute_script(userName)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.taLnk.ulBlueLinks"))).click()
        #self.driver.find_element_by_css_selector("[onclick='add_article_to_invoice(event)']").click()

        #wait = WebDriverWait(self.driver, 30)
        #wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-color='bg-dark']"))).click()
            #print(select.select_by_index(index-2))
        #dataset_drop_down_element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'users[]')))
        #dataset_drop_down_element = Select(dataset_drop_down_element)
        #mySelectElm = self.driver.find_element_by_xpath("//select[@name = 'users[]'/option[contains(text()= 'Daniel Rudberg']").click()
        #self.driver.find_element_by_xpath("//font[contains(text(),'Daniel Rudberg')]").click()
        #try:
        #wait = WebDriverWait(self.driver, 30)
        #wait.until(EC.element_to_be_clickable((By.XPATH, "//select/option[@value='148']"))).click()
        #wait.until(EC.element_to_be_clickable((By.XPATH, "//select[contains(text(),'Daniel Rudberg')]"))).click()
        #except TimeoutException as ex:
         #"777"
         #wait.until(EC.visibility_of_element_located((By.XPATH, "//select[contains(text(),'Daniel Rudberg')]"))).click()
        #self.driver.find_element_by_xpath("//select[contains(text(),'Daniel Rudberg')]").click()


    #// select[ @ name = 'passCount'] // option[contains(text(), '2')]
    #// select[ @ name = 'users[]'/option[text()= 'Daniel Rudberg']


    @classmethod
    def earDownClass(self):
        self.driver.close()
        self.driver.quit()