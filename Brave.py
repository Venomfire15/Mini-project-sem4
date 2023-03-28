from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

option = webdriver.ChromeOptions()
option.binary_location = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
driver = webdriver.Chrome(executable_path= r'C:\Program Files\BraveSoftware\Brave-Browser\Application\chromedriver', options=option)

driver.get("https://getbootstrap.com/docs/5.3/getting-started/introduction/")
driver.maximize_window()

#searching element
driver.find_element(By.CLASS_NAME, 'DocSearch-Button-Container').click()
driver.find_element(By.CLASS_NAME, 'DocSearch-Input').send_keys("navbar")
time.sleep(2)
driver.find_element(By.CLASS_NAME, 'DocSearch-Input').send_keys(Keys.ENTER)
time.sleep(2)
#driver.execute_script("window.scrollBy(0,500)","")
element = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div[2]/div[1]')
driver.execute_script("arguments[0].scrollIntoView();",element)
time.sleep(1)
#copy the code
driver.find_element(By.CLASS_NAME, 'container-fluid mt-4').click()


#creating html file
f = open('Web.txt', 'w')


print(driver.title)

time.sleep(5)
driver.quit()