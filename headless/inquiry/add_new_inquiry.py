# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
import unittest, time, re
import progressbar
import os
from dotenv import load_dotenv
load_dotenv()
from pathlib import Path  # python3 only
env_path = Path('../login/staging_tcr') / '.env'
load_dotenv(dotenv_path=env_path)
from time import sleep

class AddNewInquiry(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        options.headless = True
        self.driver = webdriver.Chrome(chrome_options=options)
        # self.driver = webdriver.Chrome()
        self.verificationErrors = []
        self.accept_next_alert = True

        print('\n')
        print("Automation Testing with mode headless is starting ... ")
        bar = progressbar.ProgressBar(maxval=20, \
            widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        bar.start()
        for i in range(20):
            bar.update(i+1)
            sleep(0.1)
        bar.finish()
        print('\n')
        
    def test_add_new_inquiry(self):
        driver = self.driver
        driver.get("https://staging-tcr.bamms.co/#!/login")
        driver.implicitly_wait(5)

        #inizialize
        secret_username = os.getenv("EMAIL")
        secret_password = os.getenv("PASSWORD")

        # Login
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(secret_username)
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(secret_password)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='remove_red_eye'])[1]/following::button[1]").click()
        driver.implicitly_wait(5)

        try:

        # Add New Inquiry
            driver.find_element_by_xpath("(.//*[@id='app']/div[3]/div/div[1]/div[1]/a)").click()
            time.sleep(2)
            print("-> Successfully login")
            driver.find_element_by_xpath("(.//*[@id='fs-form-wrap']/div[3]/button[1])").click()
            time.sleep(3)
            print("-> Try to add new inquiry")
 
        # Choose Tower
            driver.find_element_by_xpath("(.//*[@id='myform']/ol/li[2]/div/div[1]/div[2]/div/div[2]/input)").send_keys("1")
            time.sleep(3)
            driver.find_element_by_xpath("(.//*[@id='myform']/ol/li[2]/div/div[1]/div[2]/div/div[2]/input)").send_keys(Keys.ENTER)            
            print("-> Choose Tower")
            time.sleep(3)

        # Choose Floor
            driver.find_element_by_xpath("(.//*[@id='myform']/ol/li[2]/div/div[2]/div[2]/div/div[2]/input)").send_keys("1")
            time.sleep(3)
            driver.find_element_by_xpath("(.//*[@id='myform']/ol/li[2]/div/div[2]/div[2]/div/div[2]/input)").send_keys(Keys.ENTER)
            print("-> Choose Floor")
            time.sleep(3)

        # Choose Unit
            driver.find_element_by_xpath("(.//*[@id='myform']/ol/li[2]/div/div[3]/div[2]/div/div[2]/input)").send_keys("1.1.A")
            time.sleep(3)
            driver.find_element_by_xpath("(.//*[@id='myform']/ol/li[2]/div/div[3]/div[2]/div/div[2]/input)").send_keys(Keys.ENTER)
            print("-> Choose Unit")
            time.sleep(3)

        # Choose inquiry Engineering
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Please choose category'])[1]/following::span[1]").click()
            time.sleep(1)
            driver.find_element_by_xpath("(.//*[@id='fs-form-wrap']/div[3]/button[1])").click()
            time.sleep(3)
            print("-> Choose inquiry Engineering")

        # Choose Sub Engineering
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Electrical'])[1]/following::span[1]").click()        
            time.sleep(3)
            driver.find_element_by_xpath("(.//*[@id='fs-form-wrap']/div[3]/button[1])").click()
            time.sleep(3)
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='AC Temperature'])[1]/following::span[1]").click()
            time.sleep(3)
            driver.find_element_by_xpath("(.//*[@id='fs-form-wrap']/div[3]/button[1])").click()
            time.sleep(3)
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Master Bedroom'])[1]/following::span[1]").click()
            time.sleep(3)
            driver.find_element_by_xpath("(.//*[@id='fs-form-wrap']/div[3]/button[1])").click()
            print("-> Choose Sub Engineering")
            time.sleep(3)

        # Choose Date
            driver.find_element_by_id("engineering_hour").click()
            driver.find_element_by_id("engineering_hour").clear()
            time.sleep(1)
            driver.find_element_by_id("engineering_hour").send_keys("23")
            time.sleep(3)
            driver.find_element_by_id("engineering_minute").click()
            driver.find_element_by_id("engineering_minute").clear()
            time.sleep(1)
            driver.find_element_by_id("engineering_minute").send_keys("55")
            time.sleep(1)
            driver.find_element_by_xpath("(.//*[@id='fs-form-wrap']/div[3]/button[1])").click()
            print("-> Choose Time")
            time.sleep(3)

        # Fill Notes
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Please review your inquiry'])[1]/preceding::input[1]").click()
            time.sleep(3)
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='>'])[11]/following::input[1]").send_keys("halo")
            time.sleep(3)
            # driver.find_element_by_xpath("(.//*[@id='q48']/div/div)").send_keys("halo")
            # driver.find_element_by_id("q48").click()
            # driver.find_element_by_id("q48").send_keys("halo")
            driver.find_element_by_xpath("(.//*[@id='fs-form-wrap']/div[3]/button[1])").click()
            print("-> Fill notes")
            time.sleep(3)

        # Submit Inquiry
            driver.find_element_by_xpath("(.//*[@id='fs-form-wrap']/div[2]/button)").click()
            time.sleep(3)
            alert = driver.switch_to.alert
            alert.accept()
            print("-> Submit Inquiry")
            time.sleep(3)

        except:
            print("Error, because something in testing !")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()