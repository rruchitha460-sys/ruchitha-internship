from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("Program started")

driver = webdriver.Chrome()   # Let selenium handle driver automatically
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")
time.sleep(2)

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(3)
print("Login successful")

driver.quit()

