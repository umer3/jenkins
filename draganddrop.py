from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import re
import unittest
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
time.sleep(2)
source = driver.find_element_by_xpath("//*[@id='box2']")
target = driver.find_element_by_xpath("//*[@id='box105']")

actions = ActionChains(driver)

actions.drag_and_drop(source,target).perform()
