from   selenium import webdriver
from   selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
  
browser = webdriver.Firefox()
browser.get( "http://bourbon.xwork.co" )


browser.find_element_by_id("login-btn").click()  
username = browser.find_element_by_id( "email-login-1" )
username.click()
username.clear()
username.send_keys( "anjay@gmail.com" )

password = browser.find_element_by_id( "password-login-1" )
password.click()
password.clear()  
password.send_keys( "younglex18" )

submit   = browser.find_element_by_id("do-login")  
submit.click()
  

wait = WebDriverWait( browser, 5 )
  
try:
	page_loaded = wait.until_not(lambda browser: browser.current_url == "http://bourbon.xwork.co")
except TimeoutException:
	self.fail( "Loading timeout expired" )
	  
	self.assertEqual(
	browser.current_url,
	correct_page,
	msg = "Successful Login"
)