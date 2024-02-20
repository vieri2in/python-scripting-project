from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
chrome_browser = webdriver.Chrome()
# url = "https://demo.seleniumeasy.com/"
url = "https://www.google.com/"
chrome_browser.get(url)
WebDriverWait(chrome_browser, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME,"gLFyf"))
)
input_element = chrome_browser.find_element(By.CLASS_NAME,"gLFyf") #gLFyf
input_element.clear()
input_element.send_keys("tech with tim" + Keys.ENTER)
WebDriverWait(chrome_browser, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"Tech With Tim"))
)
link = chrome_browser.find_element(By.PARTIAL_LINK_TEXT,"Tech With Tim")
link.click()
sleep(3)
chrome_browser.quit()