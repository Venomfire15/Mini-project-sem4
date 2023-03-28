#For creating website only for already created account


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Set up path and chrome
str = "C:\Chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=str)

#searching needed site
driver.get("https://app.site123.com/manager/login")
#maximizing window
driver.maximize_window()

#login account
email = "firevenom15@gmail.com"
pswd = "123@fire"

driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(email)
time.sleep(2)
driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(pswd)
time.sleep(2)
driver.find_element(By.XPATH, '//button[@id="login-submit"]').click()
time.sleep(2)

#creating site
driver.find_element(By.XPATH, '//button[@class="btn btn-light btn-sm dropdown-toggle"]').click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, 'Create a website').click()
time.sleep(2)

#Entering inside frame 
#Creativity
driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@src="/manager/login/sign_up.php?fromInterface=1&l=en&s_kind=1&agencyID="]'))
driver.find_element(By.XPATH, '//div[@data-cat-id="108"]').click()
time.sleep(2)
#Enter Site name
n = "Youtuber paradise"
driver.find_element(By.XPATH, '//input[@id="websiteName"]').send_keys(n)
driver.find_element(By.XPATH, '//button[@class="forceSubmit btn btn-lg btn-success"]').click()
time.sleep(5)
#Exit to main frame
driver.switch_to.default_content()
time.sleep(10)