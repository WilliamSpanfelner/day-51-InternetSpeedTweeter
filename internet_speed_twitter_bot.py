import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        url = "https://www.speedtest.net"
        driver = self.driver
        driver.get(url)

        # Click "I Consent" button
        consent_button = driver.find_element(By.CSS_SELECTOR, "button#_evidon-banner-acceptbutton")
        consent_button.click()

        # Click the "GO" button to start speed test
        go_button = driver.find_element(By.CSS_SELECTOR, "a span.start-text")
        go_button.click()

        # driver.implicitly_wait(180)
        time.sleep(60)

        # Read download speed
        down_result = driver.find_element(By.CSS_SELECTOR, "span.download-speed")
        up_result = driver.find_element(By.CSS_SELECTOR, "span.upload-speed")
        # print(f"down speed: {down_result.text}")
        # print(f"up speed: {up_result.text}")

        self.down = float(down_result.text)
        self.up = float(up_result.text)

        driver.quit()


    def tweet_at_provider(self, username, password):
        url = "https://twitter.com/i/flow/login"
        driver = self.driver
        driver.get(url)

        time.sleep(10)

        # Find text field and send username
        username_input = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input")
        username_input.click()
        username_input.send_keys(username)

        # Locate and click the "next" button
        username_input.send_keys(Keys.TAB + Keys.ENTER)

        time.sleep(10)

        # Send password
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(password)

        # Locate and click the "login" button
        password_input.send_keys(Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER)

