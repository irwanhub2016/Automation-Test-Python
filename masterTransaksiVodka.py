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
        driver = self.driver
        driver.get("http://vodka.xwork.co/id/room-detail/ruang-meeting-di-talavera-office-suite-moselle-room,-lt-18-175")
        driver.find_element_by_id("xwork-date-perjam").click()
        driver.find_element_by_xpath("//div[12]/div[3]/ul[3]/li[25]").click()
        driver.find_element_by_xpath("//div[@id='xwork-side-panel']/div[3]/div[3]/div[4]/div[2]/div/div[2]/div[2]/button/span").click()
        driver.find_element_by_link_text("9:00").click()
        Select(driver.find_element_by_id("date-perjam-start")).select_by_visible_text("9:00")
        driver.find_element_by_xpath("(//button[@type='button'])[14]").click()
        driver.find_element_by_xpath("//div[@id='xwork-side-panel']/div[3]/div[3]/div[4]/div[2]/div/div[3]/div[2]/div/ul/li[5]/a/span").click()
        Select(driver.find_element_by_id("date-perjam-end")).select_by_visible_text("13:00")
        driver.find_element_by_xpath("//button[@onclick=\"pesanSekarang('perjam')\"]").click()
        driver.find_element_by_xpath("//button[@onclick='continueAsGuest()']").click()
    
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
