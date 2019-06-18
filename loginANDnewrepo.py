

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import os
username = "your username"
password = "your password"


# getting repo name
reponame = input("Name of repo: ")

cap = DesiredCapabilities.CHROME
cap = {'binary_location': "PATHTPCHROMEDRIVER/chromedriver"}
driver = webdriver.Chrome(desired_capabilities=cap,
                          executable_path="PATHTPCHROMEDRIVER/chromedriver")

# go to github
driver.get('http://github.com/')

# click sign in btn to go to sign in page
submit_button = driver.find_elements_by_xpath(
    '/html/body/div[1]/header/div/div[2]/div[2]/a[1]')[0]
submit_button.click()

# logging  in
username_element = driver.find_element_by_id("login_field")
username_element.send_keys(username)
password_element = driver.find_element_by_id("password")
password_element.send_keys(password)


# submit email and password
username_element.submit()

# clicking new repo btn
submit_button = driver.find_elements_by_xpath(
    '/html/body/div[4]/div/aside[1]/div[2]/div/div/h2/a')[0]
submit_button.click()

# entering repo name

repo_name_form = driver.find_element_by_id("repository_name")
repo_name_form.send_keys(reponame)

# making repo private

driver.find_element_by_xpath(
    ".//input[@type='radio' and @value='private']").click()


# making a readme.md file
driver.find_element_by_id("repository_auto_init").click()


# will not the repo(clicking the make repo btn)
# it will leave on the final window as a check
