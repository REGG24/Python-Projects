from time import sleep
from selenium import webdriver

# insert path to the crhome driver
driver = webdriver.Chrome("chromedriver")

# open up gmail page
driver.get("https://www.google.com/intl/es/gmail/about/")

# Before clicking the link first store the window handle as
window_before = driver.window_handles[0]

# look for the button to login, this button opens a new window
login_button = driver.find_element_by_xpath(
    "/html/body/div[1]/div[1]/div[5]/ul/li[2]/a")
driver.execute_script("arguments[0].click();", login_button)

# This is an easier way to do it, but since the login button is an element not interactable and raises an error we cannot use it
# login_button = driver.find_element_by_xpath(
#    '/html/body/div[1]/div[1]/div[5]/ul/li[2]/a')
# login_button.click()


# allow some time for the page to load before moving on
sleep(2)

# after clicking the link store the window handle of newly opened window a
window_after = driver.window_handles[1]
# then execute the switch to window method to move to newly opened window
driver.switch_to_window(window_after)

# look for the email field
email_field = driver.find_element_by_name('identifier')
email_field.send_keys("rubenesau.gg@gmail.com")

sleep(1)

# click on the next button to continue
next_button = driver.find_element_by_xpath(
    '//*[@id="identifierNext"]')
next_button.click()

# After doing this steps a message appears "Login Failed" because either the application or the navigator is not safe
# So most likely this is because we are using an automated script and google is very smart, but next step would be to find the password
# field, send the keys and finally log in. Something like this:

"""
# look for the password field
email_field = driver.find_element_by_xpath(
    '//*[@id = "password"]/div[1]/div/div[1]/input')
email_field.send_keys("passwordhere")

# click on the next button to continue
next_button2 = driver.find_element_by_xpath(
    '//*[@id="passwordNext"]/div/button')
next_button2.click()
"""
