from time import sleep
from selenium import webdriver

# insert path to the crhome driver
driver = webdriver.Chrome()

# open up gmail page
driver.get("https://www.gmail.com")


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
email_field = driver.find_element_by_xpath(
    '//*[@id = "password"]/div[1]/div/div[1]/input')
email_field.send_keys("passwordhere")
"""
