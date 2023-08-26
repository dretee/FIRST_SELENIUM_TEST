# FIRST_SELENIUM_TEST
AUTOMATION OF A LOGIN PAGE
# Selenium Automation Test for RRHL Adult Division Website

This is a simple automation test script using Selenium WebDriver to perform automated testing on the RRHL Adult Division website. The script opens a web browser, navigates to the specified URL, performs various actions including signing in, and validates the displayed title on the page.

## Prerequisites

- Python (3.6 or later)
- Selenium library (`pip install selenium`)

## Instructions

1. Clone the repository or download the code.

2. Make sure you have Python and the Selenium library installed.

3. Open the script file `rrhl_automation.py` using any code editor or IDE of your choice.

4. Update the script with your own credentials (email and password) in the relevant fields.

5. Save the changes.

6. Open a terminal or command prompt.

7. Navigate to the directory where the `rrhl_automation.py` script is located.

8. Run the script using the command:

   
## Steps Performed by the Script

1. Open a web browser (Microsoft Edge and chrome branch in this case).

4. Navigate to the URL `https://www.rvarhl.com/rrhladultdivision`.

5. Click on the "Sign In" element to initiate the sign-in process.

6. Enter the username/email and click the "Continue" button.

7. Enter the password and click the "Submit" button.

8. Capture the title of the inspect section of the code.

9. Compare the captured title with the actual displayed title on the open page.

10. Display whether the test passed or failed along with the page title.

11. Close the web browser.

## Note

- The script uses Microsoft Edge WebDriver. Make sure you have the Microsoft Edge browser installed on your system and the WebDriver executable available in your PATH.

- This script serves as a basic example of Selenium automation and can be extended or modified for more complex testing scenarios.

- Remember not to share sensitive information like passwords in your code repositories.


