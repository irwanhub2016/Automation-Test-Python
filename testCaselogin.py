# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestVodkaTransaksi(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_vodka_transaksi(self):
        print ("Testing Vodka Xwork ... \n")
        driver = self.driver
        driver.get("https://xwork.co")
        print ("Login Excecution ... \n")
        driver.find_element_by_id("xwork-log-in-button").click()
        driver.find_element_by_id("email-login-1").click()
        driver.find_element_by_id("email-login-1").clear()
        driver.find_element_by_id("email-login-1").send_keys("darahdjoeang@yahoo.com")
        driver.find_element_by_id("password-login-1").click()
        driver.find_element_by_id("password-login-1").clear()
        driver.find_element_by_id("password-login-1").send_keys("halohalo")    
        driver.find_element_by_id("login-go-go-1").click()
        driver.find_element_by_id("phone-and-question").click()
        driver.find_element_by_xpath("//div[@id='header']/div/div[2]/span").click()

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
        print ("Testing for access youraccount is Success")

if __name__ == "__main__":
    unittest.main()
