from selenium import webdriver
from playsound import playsound
from pynput.keyboard import Controller
from datetime import datetime
import pyperclip


import time

link = "URL of the Product"
now = datetime.now()
log = open('Log.txt', 'a')

driver = webdriver.Chrome("chromedriver")
keep_going = True
addtocart = False
captcha = False
buy_now = False
keyboard = Controller()
driver.get(link)
price = 'Price of the product'
Price_2 = "$749.00" # optional if u want to check two prices

while keep_going:
    try:
        captcha = driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/form/div[2]/div/span/span/button')
    except:
        captcha = False
    if not captcha:
            try:
                buy_now = driver.find_element_by_xpath('//*[@id="buy-now-button"]')
            except:
                buy_now = False
            if buy_now:
                keep_going = False
            else:
                driver.refresh()
            try:
                addtocart = driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')

            except:
                addtocart = False

            if addtocart:
                pyperclip.copy(link)
                keep_going = False


    elif captcha:
        playsound('/Sounds/error.mp3')
        time.sleep(3)
        driver.refresh()

    time.sleep(5)

if buy_now:
    if (driver.find_element_by_id('priceblock_ourprice').text == price or driver.find_element_by_id('priceblock_ourprice').text == Price_2):
        playsound('/Sounds/alarm.mp3')
        buy_now.click()


        time.sleep(1)
        driver.find_element_by_xpath('//*[@id = "ap_email"]').send_keys("Your_email")
        driver.find_element_by_xpath('//*[@id = "continue"]').click()
        driver.find_element_by_xpath('//*[@id = "ap_password"]').send_keys("Your_password")
        driver.find_element_by_xpath('//*[@id = "signInSubmit"]').click()
        driver.find_element_by_name('placeYourOrder1').click()
    else:
        driver.refresh()
elif addtocart:
    if (driver.find_element_by_id('priceblock_ourprice').text == price or driver.find_element_by_id('priceblock_ourprice').text == Price_2):
        playsound('/Sounds/alarm.mp3')
        addtocart.click()

        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="hlb-ptc-btn-native"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id = "ap_email"]').send_keys("Your_email")
        driver.find_element_by_xpath('//*[@id = "continue"]').click()
        driver.find_element_by_xpath('//*[@id = "ap_password"]').send_keys("Your_password")
        driver.find_element_by_xpath('//*[@id = "signInSubmit"]').click()
        driver.find_element_by_name('placeYourOrder1').click()

current_time = now.strftime("%c")
log.write("Item drop on " + current_time + "\n")
log.close()
