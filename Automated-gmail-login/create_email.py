from time import sleep
from selenium import webdriver

# insert path to the crhome driver
driver = webdriver.Chrome("chromedriver")

# open up gmail
driver.get("https://www.gmail.com/mail/help/intl/es/about.html?iframe")


# look for the button to create an account
create_account_button = driver.find_element_by_id('gmail-create-account')
create_account_button.click()


# look for the firstName field
nombre = driver.find_element_by_id('firstName')
nombre.send_keys("your name here")

# look for the lastName field
nombre = driver.find_element_by_id('lastName')
nombre.send_keys("your lastName here")

# look for the userName field
nombre = driver.find_element_by_id('username')
nombre.send_keys("yyourlastnamehere")

# look for the password field
password = driver.find_element_by_name('Passwd')
password.send_keys("your pass here")

# look for the confirmPassword field
password = driver.find_element_by_name('ConfirmPasswd')
password.send_keys("your pass here")

# click on next button
driver.find_element_by_xpath('//*[@id="accountDetailsNext"]').click()

# After doing this steps google requieres you to confirm your identity with a phone number wich
# we are not doing on this exorcise
