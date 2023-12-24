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

    def forget_password(self):
        self.driver.get(self.url)
        sleep(4)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p').click()

    def reset_password(self):
        sleep(4)
        self.driver.find_element(by=By.XPATH, value= '/html/body/div/div[1]/div[1]/div/form/div[1]/div/div[2]/input').send_keys('Admin')
        self.driver.find_element(by=By.XPATH, value= '/html/body/div/div[1]/div[1]/div/form/div[2]/button[2]').click()

    def close_browser(self):
        sleep(5)
        self.driver.quit()

SK = OrangeHRMActions()

SK.forget_password()

SK.reset_password()

SK.close_browser()