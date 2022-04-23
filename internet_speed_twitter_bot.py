import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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


    def tweet_at_provider(self):
        url = "https://twitter.com/i/flow/login"
        driver = self.driver
        driver.get(url)


