import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from plyer import notification
from creds import *


def messenger(msg, member_list):

    """ This function receives a message and a list of tuples- each tuple includes a name and a phone number as \
    strings. The function sends the message to everyone on the list with the intro Hello, -name-. """

    try:
        base_url = "https://web.whatsapp.com"

        # Where chromedriver is located on your computer
        path = r"/usr/local/bin/chromedriver"
        options = webdriver.ChromeOptions()

        # Open your Chrome profile
        options.add_argument(chromedriver_profile)
        # Open browser
        driver = webdriver.Chrome(executable_path=path, options=options)
        driver.minimize_window()
        # Open Whatsapp
        driver.get(base_url)

        # Send message to every person in member_list
        for member_name, member_phone in member_list:
            new_chat = WebDriverWait(driver, 50).until(
                lambda driver: driver.find_element(By.XPATH, "//div[@title='New chat']"))
            new_chat.click()

            input_box_search = WebDriverWait(driver, 50).until(
                 lambda driver: driver.find_element(By.XPATH, "//div[@title='Search input textbox']"))
            input_box_search.send_keys(member_phone + Keys.ENTER)

            type_it = WebDriverWait(driver, 50).until(
                lambda driver: driver.find_element(By.XPATH, "//div[@title='Type a message']"))
            type_it.send_keys('Hello, ' + member_name + '! ' + msg + Keys.ENTER)
            time.sleep(1)
        time.sleep(5)
        driver.quit()
    except Exception as e:
        notification.notify(
            title="Whatsapp message not sent",
            message="Error while sending!",
            app_icon=r"<Your icon file>",
            app_name="Whatsapp Message error",
            toast=True,
        )

