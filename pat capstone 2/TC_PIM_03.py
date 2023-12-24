from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrangeHRMActions:
    def __init__(self):
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def login(self):
        self.driver.get(self.url)
        sleep(4)
        self.driver.find_element(by=By.XPATH, value='//form/div[1]/div/div[2]/input[@name="username"]').send_keys("Admin")
        self.driver.find_element(by=By.XPATH, value='//form/div[2]/div/div[2]/input').send_keys("admin123")
        self.driver.find_element(by=By.XPATH, value='//form/div[3]/button').click()
        
    def validation(self):
        sleep(3)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span').click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span').click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span').click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span').click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span').click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span').click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span').click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a/span').click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span').click()

    def administrator_access(self):
        sleep(2)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/form/div[3]/div/div[2]/input').send_keys('admin123')
        sleep(2)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/form/div[4]/button[2]').click()

    def close_browser(self):
        sleep(3)
        self.driver.quit()

SK = OrangeHRMActions()

SK.login()

SK.validation()

SK.administrator_access()

SK.close_browser()