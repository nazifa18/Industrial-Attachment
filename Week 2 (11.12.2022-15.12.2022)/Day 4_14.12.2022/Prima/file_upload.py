from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.freepdfconvert.com/word-to-pdf")
time.sleep(10)
driver.find_element(By.CLASS_NAME, 'file-upload-input').send_keys("C://Users/DELL/Documents/07.-Cover-Page-for-Assignments.docx")
time.sleep(10)
driver.quit()