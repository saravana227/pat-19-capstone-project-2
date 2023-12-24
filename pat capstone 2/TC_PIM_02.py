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

    def admin_module(self):
        sleep(3)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click()

    def validation(self):
        sleep(3)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span').click()
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span').click()
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span').click()
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span').click()
        sleep(3)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a').click()
        sleep(3)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a').click()
        sleep(3)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span').click()

    def close_browser(self):
        sleep(3)
        self.driver.quit()


SK = OrangeHRMActions()

SK.login()

SK.admin_module()

SK.validation()

SK.close_browser()