from selenium import webdriver
import time

print("Enter repo name: ")
rp = input()

driver = webdriver.Chrome()
driver.get('https://github.com')

signinbtn = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
signinbtn.click()

usernameField = driver.find_element_by_xpath("//*[@id='login_field']")
usernameField.send_keys("theadambyrne")

passwordField = driver.find_element_by_xpath("//*[@id='password']")
passwordField.send_keys("---")

loginbtn = driver.find_element_by_xpath("//*[@id='login']/form/div[4]/input[9]")
loginbtn.click()

newrepo = driver.find_element_by_xpath("/html/body/div[4]/div/aside[1]/div[2]/div[2]/div/h2/a")
newrepo.click()

repotitle = driver.find_element_by_xpath("//*[@id='repository_name']")
repotitle.send_keys(rp)

time.sleep(2)

repobtn = driver.find_element_by_xpath("//*[@id='new_repository']/div[3]/button")
repobtn.click()
