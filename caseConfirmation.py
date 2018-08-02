# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class ResetPassword(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_reset_password(self):
        driver = self.driver
        driver.get("https://mail.google.com/mail/u/0/")
        time.sleep(3)
        driver.find_element_by_css_selector("div.aCsJod.oJeWuf").click()
        driver.find_element_by_id("identifierId").click()
        driver.find_element_by_id("identifierId").clear()
        driver.find_element_by_id("identifierId").send_keys("cobaan.xwork@gmail.com")
        driver.find_element_by_xpath("//div[@id='identifierNext']/content").click()
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("xwork123")
        driver.find_element_by_xpath("//div[@id='passwordNext']/content").click()
        driver.get("https://mail.google.com/mail/u/0/")
        driver.find_element_by_id(":36").click()
        driver.find_element_by_css_selector("img.ajT").click()
        driver.find_element_by_link_text("Confirm Your Email").click()

  
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    

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
    	time.sleep(3)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
    	print 'Testing for confirmation is success !'

if __name__ == "__main__":
    unittest.main()