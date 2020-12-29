"""
This module has the code for work as a bot video downloader;
Opens a chrome window and goes to a page that allow us to download a video
with just a link, therefore, the downloads are limited by the page.
"""

from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

# open up downloader page
driver.get("https://www.y2mate.com/es18")

#link = "https://www.youtube.com/watch?v=imN-vhi5ZWQ&ab_channel=KalleHallden"
#link = "https://www.youtube.com/watch?v=00hbcQ8aUjU&list=RD00hbcQ8aUjU&start_radio=1&ab_channel=iamAURORAVEVO"
link = "https://www.youtube.com/watch?v=5tcs2qXP3Pg&ab_channel=CodeDripbyAaronJack"

# look for the input link field
input = driver.find_element_by_id('txt-url')
input.send_keys(link)

sleep(2)

# look for the button "Empezar"
begin = driver.find_element_by_id('btn-submit')
begin.click()

sleep(10)


# look for the button to download
download_button = driver.find_element_by_xpath(
    '//*[@id="mp4"]/table/tbody/tr[1]/td[3]/a')
driver.execute_script("arguments[0].click();", download_button)

# wait 5 seconds for the new button to appear
sleep(5)

count = 0
while True:
    try:
        # if the button appeared
        element_by_path = '//*[@id="process-result"]/div/a'
        # look for the second button to download
        download_button2 = driver.find_element_by_xpath(
            element_by_path)
        driver.execute_script("arguments[0].click();", download_button2)
        break
    except NoSuchElementException:
        # if the button did not appear
        print('Unable to locate element: '+element_by_path +
              ', wating 10 seconds and try again')
        sleep(10)
        if count > 5:
            break
        count += 1
