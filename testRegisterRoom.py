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
        print "Register room ... \n" 
        driver = self.driver
        driver.get("http://vodka.xwork.co/#")
        driver.find_element_by_xpath("//div[@id='header']/nav/div/div/a[2]/span").click()
        driver.find_element_by_xpath("//input[@type='text']").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("Megamen")
        driver.find_element_by_xpath("//input[@type='email']").clear()
        driver.find_element_by_xpath("//input[@type='email']").send_keys("megamen@gmail.com")
        driver.find_element_by_xpath("//input[@type='tel']").clear()
        driver.find_element_by_xpath("//input[@type='tel']").send_keys("0217817821")
        driver.find_element_by_xpath("//form[@id='listForm']/div/div[2]/div/textarea").click()
        driver.find_element_by_xpath("//form[@id='listForm']/div/div[2]/div/textarea").clear()
        driver.find_element_by_xpath("//form[@id='listForm']/div/div[2]/div/textarea").send_keys("megamen mendung")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//form[@id='listForm']/div/div[4]/div/div").click()
        driver.find_element_by_xpath("//img[@alt='xwork-logo-header']").click()

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
        print "Testing for register room is Success"

if __name__ == "__main__":
    unittest.main()
