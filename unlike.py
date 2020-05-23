import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


drive = webdriver.Firefox(executable_path="/Users/banana/PycharmProjects/unlike_this/geckodriver")

drive.get("https://twitter.com/login")

login = drive.find_element_by_xpath("""//input[@type="text"]""")
# login.click()
login.send_keys("")  # Insert your username here

password = drive.find_element_by_xpath("""//input[@type="password"]""")

password.send_keys("")  # Insert your password here

drive.find_element_by_xpath("""//div[@data-testid="LoginForm_Login_Button"]""").click()

drive.get("https://twitter.com/ojdjo/likes")

time.sleep(4)

current_len = 10
unlikes = 0
are_you_sure = False
while current_len or not are_you_sure:
    for i in range(current_len):
        try:
            target_button = drive.find_element_by_xpath("""//div[@data-testid="unlike"]""")
            target_button.click()
            unlikes += 1
        except NoSuchElementException:
            are_you_sure = True
            drive.get("https://twitter.com/ojdjo/likes")
            time.sleep(3)

    try:
        drive.get("https://twitter.com/ojdjo/likes")

        time.sleep(2)

        current_len = len(drive.find_elements_by_xpath("""//div[@data-testid="unlike"]"""))

    except Exception as exc1:
        break
print(f"total_unlikes{unlikes}")

