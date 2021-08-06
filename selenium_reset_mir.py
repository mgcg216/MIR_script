"""
Since we are getting a "Low Current Error" everytime we charge and Mir is no longer helping with our support,
Automating the Mir reset is used every morning at 6 am

"""

import time
# importing webdriver from selenium
from selenium import webdriver



# URL of website
url = "http://192.168.15.102/"
usr = 'distributor'
pwd = 'distributor'


def mir_reset():
    # Here Chrome  will be used
    driver = webdriver.Chrome("chromedriver.exe")

    # Opening the website
    driver.get(url)

    # getting the button by class name
    username = driver.find_element_by_id("login_username")
    password = driver.find_element_by_id("login_password")
    submit = driver.find_element_by_id("submit")

    # send keys
    username.send_keys(usr)
    password.send_keys(pwd)

    # submit
    submit.click()

    time.sleep(7.5)
    # div.topbar_desktop>ul.tabs>li.status>div.button>span>strong.error
    error = driver.find_element_by_xpath(
        "/html/body/div[@class='topbar_desktop']/ul[@class='tabs']/li[@class='status']/div[@class='button']/span/strong[@class='error']")

    click_timeout(driver, error)
    time.sleep(7.5)

    # div.topbar_desktop>ul.tabs>li.status>div.topbar_desktop_tab_foldout>div.bottom>ul.buttons>li>div
    reset = driver.find_element_by_xpath(
        "/html/body/div[@class='topbar_desktop']/ul[@class='tabs']/li[@class='status']/div[@class='topbar_desktop_tab_foldout']/div[@class='bottom']/ul[@class='buttons']/li/div")

    click_timeout(driver, reset)
    time.sleep(7.5)

    # div.topbar_mobile>ul.tabs>li.state_continue>div.button, div.topbar_mobile>ul.tabs>li.state_stop>div.button
    contin = driver.find_element_by_xpath(
        "/html/body/div[@class='topbar_desktop']/div[@class='playbar']/div[@data-type='continue']")
    click_timeout(driver, contin)


    # pause = driver.find_element_by_xpath(
    #         "/html/body/div[@class='topbar_desktop']/div[@class='playbar']/div[@data-type='pause']")


def click_timeout(driver, button, secs=10):
    timout = 0
    while not button.is_displayed() or timout >= secs:
        time.sleep(1)

    button.click()
    driver.implicitly_wait(10)

if __name__ == '__main__':
    mir_reset()