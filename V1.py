
import os
from selenium import webdriver


from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
cap = DesiredCapabilities.CHROME
cap = {'binary_location': "PATH/TO/CHROMEWEBDRIVER"}
driver = webdriver.Chrome(desired_capabilities=cap, executable_path="PATH/TO/CHROMEWEBDRIVER")

#go to github
driver.get('http://github.com/')

#click sign in btn to go to sign in page
submit_button = driver.find_elements_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')[0]
submit_button.click()

#driver.findElement(By.xpath("//a[@href='/docs/configuration']")).click();

username = "URUSERNAME"
password = "URPASSWORD"
username_element = driver.find_element_by_id("login_field")
username_element.send_keys(username)
password_element = driver.find_element_by_id("password")
password_element.send_keys(password)


#submit email and password
username_element.submit()