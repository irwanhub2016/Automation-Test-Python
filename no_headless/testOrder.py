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
        print "Testing Bourbon ... \n"
        driver = self.driver
        driver.get("http://bourbon.xwork.co")
        driver.find_element_by_id("login-btn").click()
        driver.find_element_by_id("email-login-1").click()
        driver.find_element_by_id("email-login-1").clear()
        driver.find_element_by_id("email-login-1").send_keys("an")
        driver.find_element_by_id("email-login-1").clear()
        driver.find_element_by_id("email-login-1").send_keys("anjay@gmail.com")
        driver.find_element_by_id("password-login-1").clear()
        driver.find_element_by_id("password-login-1").send_keys("younglex18")
        driver.find_element_by_xpath("//div[@id='do-login']/span").click()
        driver.find_element_by_id("meeting-area").click()
        driver.find_element_by_xpath("//div[@id='meeting-area-suggestion']/div/div/div/span[2]").click()
        driver.find_element_by_id("search-room").click()
        driver.find_element_by_xpath("//img[@alt='https://s3-ap-southeast-1.amazonaws.com/xwork-gallery-tequila/rooms/images/479/1508730523.23/479_1508730523.23.md.JPEG']").click()
        driver.find_element_by_xpath("//div[4]/div/div/div/div[2]").click()
        driver.find_element_by_xpath("//tr[4]/td[2]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[11]").click()
        driver.find_element_by_xpath("//li[2]/a/span").click()
        Select(driver.find_element_by_id("hourly-start")).select_by_visible_text("8:00")
        driver.find_element_by_xpath("(//button[@type='button'])[12]").click()
        driver.find_element_by_xpath("//div[3]/div[2]/div/ul/li[3]/a/span").click()
        Select(driver.find_element_by_id("hourly-end")).select_by_visible_text("10:00")
        driver.find_element_by_xpath("//div[2]/div[7]").click()
        driver.find_element_by_xpath("//div[7]/p").click()
        driver.find_element_by_xpath("//div[3]/div[2]/span").click()
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