from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the URL
driver.get("https://www.nopcommerce.com/en/login?returnUrl=%2Fen")

# Maximize the window
driver.maximize_window()

# Find and interact with web elements
# Locators using ID LOCATORS
driver.find_element(By.ID, 'Username').send_keys("asas")

# Locators using NAME LOCATORS
# FIRST ASSIGN THE FIND ELEMENT METHOD TO A VARIABLE
# CLEAR THE INPUT BOX
# SEND KEYS TO THE BOX
input_box = driver.find_element(By.NAME, 'Username')
input_box.clear()
input_box.send_keys("ncnc")


time.sleep(5)

# Locators using LINK_TEXT
driver.find_element(By.LINK_TEXT, 'Forgot username or password?').click()
driver.back()
time.sleep(5)

# Locators using PARTIAL LINK_TEXT
driver.find_element(By.PARTIAL_LINK_TEXT, 'username').click()
driver.back()
time.sleep(5)

# Locators using RELATIVE/PARTIAL XPATH
# FIRST ASSIGN THE FIND ELEMENT METHOD TO ANOTHER VARIABLE
# CLEAR THE INPUT BOX USING THE ASSIGNED METHOD FOR THE FUNCTION
# SEND KEYS TO THE BOX
same_box = driver.find_element(By.XPATH, "//input[@id='Username']")
same_box.clear()
same_box.send_keys("akaka")
time.sleep(5)
# Locators using ABSOLUTE/FULL XPATH
driver.find_element(By.XPATH,
    '//html/body/div[7]/section/div/div/div/div/div/div[2]/div[1]/div[2]/form/div[2]/div[2]/input').send_keys('wwwuw')
time.sleep(5)

# Close the browser
driver.quit()
