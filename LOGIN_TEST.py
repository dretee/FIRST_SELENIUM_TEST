# Import other needed libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image


# This part of the script is used to
# open the url that we are meant to run our
# automation code to test for the log-in capacities


def Browser():
    # opening the browser
    driver = webdriver.Chrome()
    url = "https://www.nopcommerce.com/en/login?returnUrl=%2Fen"
    driver.get(url)
    driver.maximize_window()

    return driver


# Create a function to perform login tests
def perform_login(username, password, x_path, message):
    driver = Browser()

    # Fill in the username and password fields
    driver.find_element(By.XPATH, '//*[@id="Username"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="Password"]').send_keys(password)

    # Click the login button
    driver.find_element(By.XPATH, "//input[@value='Log in']").click()
    # Check for successful or unsuccessful login
    page_top_text = driver.find_element(By.XPATH, x_path).text
    expected_text = message

    if page_top_text == expected_text:
        print("Test successful")
    else:
        print("Test failed")
        driver.save_screenshot('screenshot.png')  # Specify a valid file path for the screenshot
        screenshot = Image.open('screenshot.png')
        screenshot.show()

    driver.quit()


# Perform login tests with different scenarios
# correct credentials
perform_login("ubongpp", "password123",
              "//h1[normalize-space()='Free and open-source eCommerce platform']",
              "Free and open-source eCommerce platform")
# # correct password and incorrect email
perform_login("ubonngphi", "password123",
              '//*[@id="login-page"]/body/div[7]/section/div/div/div/div/div/div[2]/div[1]/div[2]/form/div[2]/ul/li',
              "No customer account found")
# # correct password and blank username
perform_login("", "password123",
              '//*[@id="login-page"]/body/div[7]/section/div/div/div/div/div/div[2]/div[1]/div[2]/form/div[2]/ul/li',
              "No customer account found")
# # correct username and blank password
# from the test a correct username and blank password space
# will give a different message of the credentials provided are incorrect
perform_login("ubongpp", "",
              '//*[@id="login-page"]/body/div[7]/section/div/div/div/div/div/div[2]/div[1]/div[2]/form/div[2]/ul/li',
              "The credentials provided are incorrect")
# # incorrect username and blank password
perform_login("ubongpii", "",
              '//*[@id="login-page"]/body/div[7]/section/div/div/div/div/div/div[2]/div[1]/div[2]/form/div[2]/ul/li',
              "No customer account found")
# Add more test scenarios as needed
