import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 150
PROMISED_UP = 10


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        url = "https://www.speedtest.net"
        self.driver.get(url)

        # Click "I Consent" button
        consent_button = self.driver.find_element(By.CSS_SELECTOR, "button#_evidon-banner-acceptbutton")
        consent_button.click()

        # Click the "GO" button to start speed test
        go_button = self.driver.find_element(By.CSS_SELECTOR, "a span.start-text")
        go_button.click()

        # driver.implicitly_wait(180)
        time.sleep(60)

        # Read download speed
        self.down = self.driver.find_element(By.CSS_SELECTOR, "span.download-speed").text
        self.up = self.driver.find_element(By.CSS_SELECTOR, "span.upload-speed").text
        # print(f"down: {self.down} up: {self.up}")

    def tweet_at_provider(self, username, password):
        url = "https://twitter.com/i/flow/login"
        self.driver.get(url)

        time.sleep(10)

        # Find text field and send username
        username_input = self.driver.find_element(By.XPATH,
                                                  "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input")
        username_input.click()
        username_input.send_keys(username)

        # Locate and click the "next" button
        username_input.send_keys(Keys.TAB + Keys.ENTER)

        time.sleep(15)

        # Send password
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(password)

        # Locate and click the "login" button
        password_input.send_keys(Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER)

        time.sleep(10)

        # Target the message input and enter a message
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up, " \
                f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"

        tweet_input = self.driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Tweet text"]')
        tweet_input.click()
        tweet_input.send_keys(tweet)

        # Locate the Tweet button and tweet the message
        tweet_button = self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetButtonInline"]')
        tweet_button.click()

        time.sleep(5)
        self.driver.quit()
