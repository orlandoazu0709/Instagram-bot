from selenium import webdriver
from time import sleep

class InstaBot:

    def __init__(self, username, pw, message):

        self.driver = webdriver.Chrome()
        self.username = username

        self.driver.get("https://www.instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
                .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
                .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
                .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a")\
                .click()
        sleep(2)
        self.driver.find_element_by_css_selector("textarea").send_keys(message)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Send')]").click()
        sleep(4)

user = input("Username: ")
password = input("Password: ")
print("")
message = input("Input message: ")

my_bot = InstaBot(user, password, message)

