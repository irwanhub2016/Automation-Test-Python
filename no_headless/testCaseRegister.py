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
        print "Testing Vodka Xwork ... \n"
        driver = self.driver
        driver.get("http://vodka.xwork.co")
        driver.find_element_by_id("xwork-sign-up-button").click()
        driver.find_element_by_xpath("//div[@id='modal-daftar']/div/div/div[3]/div/form/div/div").click()
        driver.find_element_by_id("first-name-daftar").click()
        driver.find_element_by_id("first-name-daftar").clear()
        driver.find_element_by_id("first-name-daftar").send_keys("Aqua")
        driver.find_element_by_id("last-name-daftar").clear()
        driver.find_element_by_id("last-name-daftar").send_keys("Cisalak")
        driver.find_element_by_id("email-daftar").clear()
        driver.find_element_by_id("email-daftar").send_keys("darahdjoeang@yahoo.com")
        driver.find_element_by_id("phone-number-daftar").clear()
        driver.find_element_by_id("phone-number-daftar").send_keys("08561712998")
        driver.find_element_by_id("password-daftar").clear()
        driver.find_element_by_id("password-daftar").send_keys("halohalo")
        driver.find_element_by_id("confirm-password-daftar").clear()
        driver.find_element_by_id("confirm-password-daftar").send_keys("halohalo")
        driver.find_element_by_id("daftar-go-go").click()
        assert "Not Found" not in driver.page_source
        
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
        print "Testing Success !"


if __name__ == "__main__":
    unittest.main()
