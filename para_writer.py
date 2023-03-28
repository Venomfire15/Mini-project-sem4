from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Set up path and chrome
str = "C:\Program Files\BraveSoftware\Brave-Browser\Application\chromedriver.exe"
driver = webdriver.Chrome(executable_path = str)

#searching needed site
driver.get("https://www.neuraltext.com/ai/paragraph-generator")
driver.maximize_window()
print(driver.title)
time.sleep(2)

#Entering the text to convert into paragraph
driver.execute_script('window.scrollBy(0,300)',"")
time.sleep(2)

s = "Branded Sneakers"
#Entering inside frame
driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@src="https://api.neuraltext.com/api/v1/ai/public/paragraph-generator/"]'))
driver.find_element(By.XPATH, '//input[@id="product-name-input"]').send_keys(s)
driver.find_element(By.XPATH, '//button[@id="generate-btn"]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//button[@class="btn btn-light"]')


driver.switch_to.default_content() #to go to main page from selected frame
time.sleep(2)