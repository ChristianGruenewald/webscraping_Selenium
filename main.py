#Selenium imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import time

#Other imports here
import os
import wget

#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
 #   print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.



driver= webdriver.Chrome('C:/Users/g1007/chromedriver_win32/chromedriver.exe')
driver.get('https://www.instagram.com/')

WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[tabindex='0']"))).click() #wait until page is loaded and field username is ready

username= WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']"))) #wait until page is loaded and field username is ready
password= WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']"))) #wait until page is loaded and field password is ready

username.clear()
password.clear()
username.send_keys("")
password.send_keys("")

log_in=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

not_now=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Jetzt nicht')]"))).click()

not_now2=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Jetzt nicht')]"))).click()

searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Suchen']")))
searchbox.clear()
keyword='#cat'
searchbox.send_keys(keyword)

# Wait for 5 seconds
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)


#scroll down to scrape more images
driver.execute_script("window.scrollTo(0, 4000);")

#target all images on the page
images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]
images = images[:-2]

print('Number of scraped images: ', len(images))

path = os.getcwd()
path = os.path.join(path, keyword[1:] + "s")

#create the directory
os.mkdir(path)


#download images
counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1

#logout = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Abmelden')]")))
driver.close()


#if __name__ == '__main__':
