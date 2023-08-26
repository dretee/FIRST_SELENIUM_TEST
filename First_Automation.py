# 1) open web browser(chrome)
# 2) open URL https://www.rvarhl.com/rrhladultdivision
# 3) click on the sign in element to sign in
# 4) enter username and click on the continue button
# 5) enter password and click the submit button
# 6) capture the title for the inspect section of the code
# 7) compare it to the displayed title on the open page by our test
# 8) close the browser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import service


driver = webdriver.Edge()


driver.get("https://www.rvarhl.com/rrhladultdivision")
driver.maximize_window()
driver.find_element(By.ID, "nb-sign-in-link").click()

driver.find_element(By.NAME, "user[login]").send_keys("ubongphilip2200@gmail.com")
driver.find_element(By.NAME, "commit").click()

driver.find_element(By.NAME, "user[password]").send_keys("Admin1234")
driver.find_element(By.NAME, "commit").click()

display_title = driver.title
actual_title_on_the_page = "RRHL Adult Division"
if display_title == actual_title_on_the_page:
    print("The test passed")
    print(f"This is the title of the page {display_title}")
else:
    print("the test failed")
driver.close()

