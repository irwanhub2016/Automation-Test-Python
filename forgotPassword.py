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
        driver.get("http://vodka.xwork.co/id/forgot-password")
        # ERROR: Caught exception [unknown command []]
        driver.find_element_by_id("email-to-reset").click()
        driver.find_element_by_id("email-to-reset").clear()
        driver.find_element_by_id("email-to-reset").send_keys("irwansyarifudin16@gmail.com")
        driver.find_element_by_xpath("//button[@onclick='sendResetEmail()']").click()
		
    
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
    	print 'Testing for forgot-password is success !'

if __name__ == "__main__":
    unittest.main()